from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import logging
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

log_dir = os.getenv("LOG_PATH", "/var/log/app")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "app.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return "Hello from PortOne!"

@app.route("/error")
def error():
    app.logger.error("Error endpoint triggered")
    return "Something went wrong!", 500

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
