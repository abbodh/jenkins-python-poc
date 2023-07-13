FROM python:latest
RUN pip install requests
COPY call-endpoints.py ./
ENTRYPOINT [ "python"]
CMD call-endpoints.py --env ${ENVIRONMENT}
