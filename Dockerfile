FROM python:3.10
EXPOSE 5000
RUN mkdir -p/opt/services/bot/falbot
WORKDIR /opt/services/bot/falbot
COPY . /opt/services/bot/falbot
RUN pip insrall -r reqirements.txt
CMD ["python", "/opt/services/bot/falbot/main.py"]