# Documentation

## Public documents

This section contains documents of directories which may be provided to customers.

Guides:

* [Installation](public/installation.md)
* [Maintenance](public/maintenance.md)
* [Troubleshooting](public/troubleshooting.md)

Documents described custom resources:

* [PlatformMonitoring](public/apis/platform-monitoring.md)
* [PrometheusAdapter](public/apis/prometheus-adapter.md)
* [CustomScaleMetricRule](public/apis/custom-scale-metric-rule.md)

Documents described metrics, alerts, dashboards which deploy with monitoring out-of-box (OOB):

* [Metrics](public/metrics-oob.md)
* [Alerts](public/alerts-oob.md)
* [Dashboards](public/dashboards-oob)

Examples:

* [Custom resources](public/examples/custom-resources)

## Internal documents

This section contains documents or directories which should not provide to customers and should use only internal in
company.

### Configuration

* [Cookbook](internal/cookbook/cookbook.md)
* [Configuration](internal/configuration/setup-service-monitoring.md)
* [Migration](internal/migration/README.md)

### Development

* [Developer Guide](internal/development/developer-guide.md)
* [Operator design](internal/development/design.md)
* [Work with Helm charts](internal/development/work-with-helm-chart.md)
* [SVT results](internal/development/prometheus-svt-results.md)

## Images and them sources

All images store into directory [docs/public/images](public/images).

And all sources of these images store into directories:

* [docs/sources/drawio](sources/drawio) - for diagrams which made into [https://draw.io](https://draw.io)
* [docs/sources/plantuml](sources/plantuml) - for diagrams which made with using PlantUML syntax
