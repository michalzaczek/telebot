FROM python:3.11-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
