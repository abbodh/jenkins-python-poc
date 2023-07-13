FROM python:3.9.10-slim-buster

COPY sample.py

CMD python sample.py --env ${ENVIRONMENT}