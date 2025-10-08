FROM docker.elastic.co/beats/filebeat:7.17.10

USER root

# Copy config file into container
COPY filebeat.yml /usr/share/filebeat/filebeat.yml

# Set strict permissions required by Filebeat
RUN chmod 600 /usr/share/filebeat/filebeat.yml
