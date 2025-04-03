import base64
import json
import re

import yaml
from PlatformLibrary import PlatformLibrary


def get_object_data(response):
    return response.json()['data']


def get_prometheus_target(response, target_name):
    json_object = get_object_data(response)
    for item in json_object.get('activeTargets'):
        labels = item.get('labels')
        if target_name in labels.get('job'):
            return item
    return False


def target_state_and_not_empty(target, health):
    if not str(target.get('scrapeUrl')).isspace() and str(target.get('scrapeUrl')).count('/metrics'):
        if health in target.get('health'):
            return True
    return False


def check_labels_in_target(prometheus_json_target, namespace, service, job):
    list_of_labels = prometheus_json_target.get('labels')
    if namespace in list_of_labels.get('namespace'):
        if service in list_of_labels.get('service'):
            if job in list_of_labels.get('job'):
                return True
    return False


def get_metrics_of_test_app(response, job, namespace):
    if 'success' in response.json()['status']:
        json_object = get_object_data(response)
        for item in json_object.get('result'):
            metrics = item.get('metric')
            if job in metrics.get('job'):
                if namespace in metrics.get('namespace'):
                    return item
        return False


def get_metrics_by_job(response, job):
    if 'success' in response.json()['status']:
        json_object = get_object_data(response)
        for item in json_object.get('result'):
            metrics = item.get('metric')
            if job in metrics.get('job'):
                return item
        return False


def check_metrics_is_not_empty(metrics):
    if len(metrics.get('value')) != 0:
        return True


def check_cr_label_updated(response, label):
    labels = response.get('labels')
    if label in labels.get('app.kubernetes.io/component'):
        return True
    return False


def check_cr_service_exists(response, service, parentservice=None):
    if service in response.keys():
        service_child = response.get(service)
        if 'install' in service_child.keys():
            if service_child.get('install'):
                return True
        if service == 'route' or service == 'ingress':
            if 'host' in service_child.keys():
                if service_child.get('host') != '':
                    return True
    elif parentservice:
        if parentservice in response.keys():
            service_child = response.get(parentservice)
            if service in service_child.keys():
                return True
    return False


def check_route_or_ingress(response, service_in_cr, service, namespace, parentservice=None):
    k8s_lib = PlatformLibrary()
    sub_service = ''
    if parentservice:
        sub_service = response.get('spec').get(parentservice).get(service_in_cr)
    else:
        sub_service = response.get('spec').get(service_in_cr)
    if (check_cr_service_exists(sub_service, 'route')):
        return k8s_lib.get_route_url(service, namespace)
    if (check_cr_service_exists(sub_service, 'ingress')):
        return k8s_lib.get_ingress_url(service, namespace)


def get_list_length(list_for_check):
    return len(list_for_check)


def get_dashboard_from_status(dictionary, namespace, name):
    status = dictionary.get('status')
    dashboards = status.get('dashboards')
    for i in dashboards:
        if (i.get('namespace') == namespace) and (i.get('name') == name):
            return i


def parse_yaml_file(file_path):
    return yaml.safe_load(open(file_path))


def get_dashboard_value_from_file(file_path, value):
    dict_dashboard = json.loads(parse_yaml_file(file_path).get('spec').get('json'))
    return dict_dashboard.get(value)


def update_dashboard_parameter(body: dict, key: str, updated_value: str) -> dict:
    body.get('metadata').update({key: updated_value})
    return body


def get_object_in_namespace_by_mask(list, mask):
    masked_objects = []
    pattern = mask + '-operator-*'
    for object in list:
        if mask in object.metadata.name:
            if re.search(pattern, object.metadata.name) is None:
                masked_objects.append(object)
    return masked_objects


def get_value_from_prometheus_query(response):
    metrics = get_object_data(response)
    for i in metrics['result']:
        if i['metric']['service'] == 'autoscaling-example-service':
            return i['value'][1]


def convert_to_json(str_body):
    return json.loads(str_body)


def compare_two_jsons(body_a, body_b):
    body_a, body_b = json.dumps(body_a, sort_keys=True), json.dumps(body_b, sort_keys=True)
    if body_a == body_b:
        return True


def check_tags_contain_value(tags, value):
    if value in tags:
        return True
    return False


def add_security_context_to_deployment(path_to_file, namespace):
    k8s_lib = PlatformLibrary()
    deployment = parse_yaml_file(path_to_file)
    pods = k8s_lib.get_pods(namespace)
    for pod in pods:
        if 'monitoring-operator' in pod.metadata.name:
            fs_group = pod.spec.security_context.fs_group
            run_as_user = pod.spec.security_context.run_as_user
            break
    if fs_group == None and run_as_user == None:
        return deployment
    deployment['spec']['template']['spec']['securityContext'] = dict(fsGroup=fs_group, runAsUser=run_as_user)
    return deployment


def get_pass_from_secret(secret):
    password = base64.b64decode(secret.data.get('password')).decode()
    return password


def get_username_from_secret(secret):
    username = base64.b64decode(secret.data.get('username')).decode()
    return username
