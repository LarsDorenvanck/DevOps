FROM ubuntu:latest
LABEL authors="worpg00"

ENTRYPOINT ["top", "-b"]

FROM python:3.8-slim

COPY * / devops-git/

WORKDIR /devops-git

CMD ["python", "main.py"]