FROM python:latest

# Install and upgrade pip
RUN pip install --upgrade pip
	
COPY call-endpoints.py ./
ENTRYPOINT [ "python", "call-endpoints.py"]
