# 🚀 PortOne DevOps Engineer Take-Home Assignment

This project demonstrates containerization, observability, and infrastructure-as-code using a simple Flask API, ELK stack for logging, and Prometheus + Grafana for monitoring. Everything is orchestrated with Docker Compose and configured via a `.env` file for easy customization.

---

## 🧰 Tech Stack

- **Flask** (Python): Lightweight backend API with logging and metrics
- **Docker & Docker Compose**: Container orchestration
- **ELK Stack**: Elasticsearch, Filebeat, Kibana for centralized logging
- **Prometheus & Grafana**: Metrics scraping and visualization

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SudeshnaSaha-97/stack-watch.git
   cd stack-watch


---

## ✨ Rewrite or Modify .env File

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
