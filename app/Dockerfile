FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_PORT=5000
ENV LOG_PATH=/var/log/app
EXPOSE $FLASK_PORT
CMD ["python", "app.py"]
