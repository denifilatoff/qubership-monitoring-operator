non_operator_managed = ['BLACKBOX-EXPORTER', 'CERT-EXPORTER', 'CLOUDWATCH-EXPORTER',
                        'CONFIGURATIONS-STREAMER', 'GRAPHITE-REMOTE-ADAPTER',
                        'NETWORK-LATENCY-EXPORTER', 'PROMETHEUS-ADAPTER',
                        'PROMETHEUS-ADAPTER-OPERATOR', 'PROMITOR-AGENT-SCRAPER',
                        'PROMXY', 'VERSION-EXPORTER', 'GRAFANA']


def check_that_parameters_are_presented(environ, *variable_names) -> bool:
    exclude_tags = []
    for variable in non_operator_managed:
        if (environ.get(variable) == 'false' or environ.get(variable) is None):
            exclude_tags.append((variable).lower())
    operator = environ.get('OPERATOR')
    if operator == 'prometheus-operator':
        exclude_tags.append(('smoke-test-vm').lower())
    elif operator == 'victoriametrics-operator':
        exclude_tags.append(('smoke-test-prometheus').lower())
    return exclude_tags


def get_excluded_tags(environ) -> list:
    return check_that_parameters_are_presented(environ, non_operator_managed)
