# Getting Started with Apache Airflow

## 1 - Setup

Apache Airflow can be run from Docker using the docker compose script ./docker-compose.yaml. This file was copied from the Airflow guide here: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html. The guide provides additional details that you should read prior to running the environment. 

Run the following command to start up Airflow with Flower:

```
docker compose --profile flower up
```

Server startup will take "minutes" to complete, The web server will be started when the following message is output:

```
getting-started-apache-airflow-airflow-webserver-1  | [2023-05-02 19:28:26 +0000] [17] [INFO] Listening at: http://0.0.0.0:8080 (17)
```

To verify the server started correctly, open a browser to: 

```
http://localhost:8080
```

You should be prompted with an Airflow login page, which you can use the default user/pass of airflow/airflow to log in. 

Flower will be running at the following URL: 

```
http://localhost:5555/
```

You can also run the following command to get full information about the Airflow environment:

```
docker compose run airflow-worker airflow info
```

To stop the server, run the following command:

```
docker compose down --volumes --remove-orphans
```

## 2 - Teardown and Restart

Read the Airflow guide for options to teardown and restart Airflow from scratch: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

## 3 - Developing a Hello World Workflow

1. For development, you will need Python 3.10+ installed. Your IDE should be configured to use the python interpreter that you've downloaded and installed. Once the installation is complete, run the following command to install airflow packages: 
    ```
    pip install "apache-airflow==2.6.0" --ignore-installed
    ```
2. 