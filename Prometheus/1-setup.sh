
#install__________________
wget -c https://github.com/prometheus/prometheus/releases/download/v2.42.0/prometheus-2.42.0.linux-amd64.tar.gz
tar xvf ~/prometheus-2.42.0.linux-amd64.tar.gz
mv ~/prometheus-2.42.0.linux-amd64 ~/prometheus
prometheus/prometheus --config.file=prometheus/prometheus.yml

#Node_Exporter__________________
wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
tar -xvf ~/node_exporter-1.0.1.linux-amd64.tar.gz
mv ~/node_exporter-1.0.1.linux-amd64 ~/node_exporter

node_exporter/node_exporter

##
sudo nano /etc/systemd/system/node_exporter.service
--- # add
[Unit]
Description=Node Exporter
After=network.target
[Service]
User=root
ExecStart=/path/to/node_exporter
[Install]
WantedBy=default.target
---
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter




# Config Prom to real values
nano prometheus/prometheus.yml

---
- job_name: server_monitor
  scrape_interval: 5s
  static_configs:
    - targets: ["3.251.6.163:9100"]
---













.