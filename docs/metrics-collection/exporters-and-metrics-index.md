This document describes all exporters from which the Monitoring stack can collect metrics or juts a list of metrics
available to collect from some tools.

# Table of Content

* [Table of Content](#table-of-content)
* [Types](#types)
  * [Applications](#applications)
  * [Big Data](#big-data)
  * [Databases](#databases)
  * [Distributes Caches](#distributes-caches)
  * [Kubernetes](#kubernetes)
  * [Observability](#observability)
    * [Components](#components)
    * [Exporters](#exporters)
    * [Public Cloud Exporters](#public-cloud-exporters)
  * [Queues](#queues)

# Types

## Applications

* Java
  * Micrometer
  * JMX exporter
* Golang
* Python
* Nginx

## Big Data

* Airflow
* Apache Spark

## Databases

* ArangoDB
* Cassandra
* ClickHouse
* ElasticSearch
* Greenplum
* MongoDB
* PostgreSQL

## Distributes Caches

* [Consul](metrics/consul-metrics.md)
* Redis
* ZooKeeper

## Kubernetes

* Calico
* [Etcd](metrics/etcd-metrics.md)
* Ingress Nginx
* Kube APIServer
* Kube Scheduler
* Kube-state-metrics
* [Kubelet](metrics/kubelet-metrics.md)

## Observability

### Components

* [Alertmanager](metrics/alertmanager-metrics.md)
* FluentBit
* FluentD
* Graylog
* [Prometheus](metrics/prometheus-metrics.md)
* Jaeger

### Exporters

* [Blackbox-exporter](exporters/blackbox-exporter.md)
* Cert-exporter
* [JSON-exporter](exporters/json-exporter.md)
* Network-latency-exporter
* Version-exporter

### Public Cloud Exporters

* AWS - Cloudwatch-exporter
* Azure - Promitor
* Google Cloud - Stackdriver-exporter

## Queues

* Apache Kafka
* RabbitMQ
