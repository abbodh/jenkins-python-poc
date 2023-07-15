FROM python:latest

RUN pip install requests

COPY args.py ./
COPY call-endpoints.py ./
ENTRYPOINT [ "python", "call-endpoints.py"]
