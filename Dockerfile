FROM python:3.12.4-slim-bookworm

RUN apt-get update -y && apt-get install -y awscli && apt-get clean
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]