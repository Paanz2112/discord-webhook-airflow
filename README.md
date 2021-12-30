# Airflow Notification using discord webhook
this project use Discord webhook to send notification about airflow dags to specific discord server

How to use this script  
1. create discord account and discord server
2. create server's webhook (see [Intro to Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for more infomation)
3. create .env file and add DISCORD_TOKEN, DISCORD_API, WEBHOOKS_ID in your .env
4. use pip install -r req.txt to install lib
> (I'm using Python 3.7 if you using other version please see pypi for more compatible version of library)
5. create airflow dag file see example in example_dag.py
>you can custom your message to whatever you want. See [doc](https://discord.com/developers/docs/resources/webhook) for more infomation about message customization
