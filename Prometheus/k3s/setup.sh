
#######################
# 2. Deploy Prometheus Manually:
kubectl create namespace monitoring
kubectl apply -f promet-comb.yml
(change Service to NodePort)
kubectl get pods -n monitoring
kubectl port-forward -n monitoring svc/prometheus 9090:9090

#######################
# 3. Configure Prometheus to Scrape Application Metrics
# Expose Application Metrics: Ensure that your application is exposing metrics. 
# For most applications, you will use a library like prometheus-client for Python, or micrometer for Java to expose a /metrics endpoint.
# Service Discovery: In the prometheus.yml file, configure Prometheus to scrape your application's service. 
# Here is an example of adding a scrape config for your application:
# Check directories in manifests to prometheus-configs
kubectl apply -f prometheus-config.yaml

#######################
# 4. Monitor Your Database
# MySQL Exporter:
kubectl apply -f https://raw.githubusercontent.com/prometheus/mysqld_exporter/main/examples/mysqld_exporter.yaml
# or PostgreSQL Exporter:
kubectl apply -f https://raw.githubusercontent.com/prometheus-community/helm-charts/main/charts/prometheus-postgres-exporter/templates/postgres-exporter-deployment.yaml
# Then, add the exporter services to your prometheus.yml scrape configuration.

#######################
# Expose Prometheus Metrics for Scraping:
---
scrape_configs:
  - job_name: 'mysql-exporter'
    static_configs:
      - targets: ['<mysql-exporter-service>:9104']

  - job_name: 'postgres-exporter'
    static_configs:
      - targets: ['<postgres-exporter-service>:9187']
---

#######################
# 6. Set Up Grafana (Optional)
# Deploy Grafana:
kubectl apply -f https://raw.githubusercontent.com/grafana/grafana/master/deploy/kubernetes/grafana.yaml
# Access the Grafana UI by forwarding the Grafana service:
kubectl port-forward svc/grafana 3000:3000
# Then, navigate to http://localhost:3000, log in, and add Prometheus as a data source.

#######################
# 7. Add Alerts (Optional)
# configure alerts by modifying the prometheus.yml
---
rule_files:
  - "alert.rules.yml"

groups:
- name: alert.rules
  rules:
  - alert: HighMemoryUsage
    expr: node_memory_Active_bytes / node_memory_MemTotal_bytes > 0.8
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High Memory Usage"
---
kubectl apply -f prometheus-config.yaml






.