# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:4-python3.10-appservice
FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r /requirements.txt

#COPY . /home/site/wwwroot

COPY ./src/function_app.py /home/site/wwwroot/function_app.py

ENTRYPOINT ["python", "/home/site/wwwroot/function_app.py"]