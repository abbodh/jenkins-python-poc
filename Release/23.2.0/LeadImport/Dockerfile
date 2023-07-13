FROM python:latest

# Install and upgrade pip
RUN pip install --upgrade pip
	
# Collect pip requirements
COPY requirements.txt .
	
# Install pip requirements
RUN pip install -r requirements.txt
	
COPY src/ .

COPY call-endpoints.py ./
ENTRYPOINT [ "python", "call-endpoints.py"]
