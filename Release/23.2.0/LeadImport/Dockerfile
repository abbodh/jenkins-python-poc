FROM python:latest

RUN pip install requests

COPY call-endpoints.py ./
ENTRYPOINT [ "python", "call-endpoints.py"]
