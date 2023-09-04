# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:4-python3.10-appservice
FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r /requirements.txt

#COPY . /home/site/wwwroot

COPY ./src/writer_json.py /src/writer_json.py

ENTRYPOINT ["python","./src/writer_json.py"]