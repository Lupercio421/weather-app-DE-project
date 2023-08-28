# weather-app
This is the repo of the Weather app from my YouTube video

# Project structure
In this project you build a end-to-end pipeline from requesting weather data from an API to visualizing the results on a Dashboard.
As tools we use the weather api, Docker, AWS Elastic container registry, AWS Lambda, AWS EventBridge and Grafana as the dashboard solution.
Here's an overview of the pipeline:
![Project setup image](/assets/project-structure.png)

# What to do in the right order
- Create account on [weatherapi.com](https://www.weatherapi.com) and generate a token
- Clone repository to local and replace the token
- Set up a Azure Time Series Insights Environment [MSFT Azure TSI](https://learn.microsoft.com/en-us/azure/time-series-insights/)
- Create the weather database, stable and tables cuenca and cartagena
- Install Azure TSI connector for python with `pip install -
- Run the code in your VSCode or other dev env and check Azure TSI if the data is there
- Build the docker container `docker build -f dockerfile-user -t weather-data .`
- If not done already install the [Azure CLI] (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)
- Create a development user and role in IAM with full rights to ecr, create keys for that user
- Do a `aws configure` and enter key and secret key
- Create ECR, tag the image and push the image up to ECR (find the commands in ECR, top right corner)
- Create Azure Funciton that uses the image
- Create EventBridge schedule that triggers the Lambda function
- Pull the [Grafana image](https://hub.docker.com/r/grafana/grafana) from docker hub `docker pull grafana/grafana`
- Start grafana with `docker run --name=grafana -p 3000:3000 grafana/grafana`
- Go to localhost:3000 to access Grafana, connect the TDengine datasource and create yourself a Dashboard


# Helpful links
- Try out the WeatherAPI interactive explorer: [explore the API](https://www.weatherapi.com/api-explorer.aspx)
- TDEngine documentation of read/write through websocket!! (for TDengine cloud) [tdengine docs](https://docs.tdengine.com/reference/connector/python/)
- AWS cli installation [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Azure cli installation [Azure Documentation] (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)
- AZ-204: Implement containerzied solutions. Helped me learn about [Azure container registry] (https://learn.microsoft.com/en-us/training/paths/az-204-implement-iaas-solutions/)
- How to push a docker image to Azure Container Registry [YT](https://www.youtube.com/watch?v=HlqR5hn8_v8&t=71s)
- Ranking time series databases [dbengines.com](https://db-engines.com/en/ranking_trend/time+series+dbms)

# More about TDengine
- TDengine docker image [visit Dockerhub](https://hub.docker.com/r/tdengine/tdengine)
- TDengine stream processing, caching and data subscription [Streaming features](https://tdengine.com/tdengine/simplified-time-series-data-solution/)
- time series extentions like time weighted average rate of change and more [functions](https://docs.tdengine.com/taos-sql/function/#time-series-extensions)
- Performance comparison influxdb timescaledb and TDengine [Benchmark comparions](https://tdengine.com/devops-performance-comparison-influxdb-and-timescaledb-vs-tdengine/)
