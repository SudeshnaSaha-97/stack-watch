# 🚀 DevOps Engineer Assignment on Stack Watch

A containerized Flask application with full-stack observability using ELK, Prometheus, and Grafana. Built for the PortOne DevOps assignment, this project demonstrates infrastructure-as-code, environment-driven configuration, and real-time monitoring — all orchestrated via Docker Compose. Everything is orchestrated with Docker Compose and configured via a `.env` file for easy customization.

---

## 🧰 Tech Stack

- **Flask** (Python): Lightweight backend API with logging and metrics
- **Docker & Docker Compose**: Container orchestration
- **ELK Stack**: Elasticsearch, Filebeat, Kibana for centralized logging
- **Prometheus & Grafana**: Metrics scraping and visualization

---

## 📁 Project Structure

stack-watch/
├── app/                  # Flask app with logging
├── elk/                  # Filebeat config and Dockerfile
├── monitoring/           # Prometheus and Grafana setup
├── logs/                 # Runtime logs (excluded via .gitignore)
├── .env                  # Environment variables
├── docker-compose.yml    # Orchestration
└── README.md             # You're reading it!

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SudeshnaSaha-97/stack-watch.git
   cd stack-watch

---

## ✨ Edit .env to match your local setup

- FLASK_PORT=5000
- ELASTICSEARCH_PORT=9200
- KIBANA_PORT=5601
- PROMETHEUS_PORT=9090
- GRAFANA_PORT=3000
- LOG_PATH=./logs

---

## 🚀 Quick Start the Full Stack

```bash
    docker-compose --env-file .env up --build
```

---

## 🔍 Observability Features

- **Structured Logging:** Flask logs routed via Filebeat to Elasticsearch
- **Log Visualization:** Kibana dashboards with index pattern filebeat-*
- **Metrics Collection:** Prometheus scrapes Flask metrics endpoint
- **Grafana Dashboards:** Prebuilt dashboard for request latency, error rates, and uptime

---

## 📊 Screenshots

- **Grafana**
  <img width="1414" height="928" alt="image" src="https://github.com/user-attachments/assets/528389fd-4452-46c7-93a4-d54f9bb86556" />

- **Prometheus**
  <img width="1855" height="1007" alt="image" src="https://github.com/user-attachments/assets/bfe82f64-c35a-4f77-8c57-2bee305b8105" />

- **Kibana**
  <img width="1886" height="986" alt="image" src="https://github.com/user-attachments/assets/fbcf7303-06fb-4ad4-90d9-07d711946be9" />

---

## 🧪 Testing the App

Visit:
- http://localhost:5000 → Home endpoint
- http://localhost:5000/error → Triggers error log
- http://localhost:5000/metrics → Prometheus metrics

---

## 🧠 Author
Sudeshna Saha DevOps Engineer | Cloud Practitioner [LinkedIn](https://www.linkedin.com/in/sudeshnasaha97/) • [GitHub](https://github.com/SudeshnaSaha-97)



