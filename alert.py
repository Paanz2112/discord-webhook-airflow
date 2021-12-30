import requests
from datetime import datetime
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

url = env["DISCORD_PTB_API"]+env["WEBHOOKS_ID"]+"/"+env["DISCORD_TOKEN"]

def sendAlert(**kwargs):
    ## dag_id,task_id,dag_state,exec_date,end_date,job_id_,dag_duration

    json_payload = {
                "username":"Airflow Dags Notification",
                "content": "<@&ROLE_ID GOES HERE>",
                "allowed_mentions": {
                    "parse": ["users", "roles"],
                    "users": []
                },
                "embeds": [
                    {
                    "author": {
                        "name": "Baby vm etl server",
                        "url": "https://www.SOME-URL-GOES-HERE.co.th/",
                        "icon_url": env["COMPANY_PROFILE_IMAGE"]
                    },
                    "title": f"""{kwargs["dag_id"]}""",
                    "description": f"""Airflow notification of dag [{kwargs["dag_id"]}]({env["AIRFLOW_WEBSERVER_URL"]}/tree?dag_id={kwargs["dag_id"]})""",
                    "type":"rich",
                    "fields": [
                            {
                            "name": "Dag Name",
                            "value": f"""{kwargs["dag_id"]}""",
                            "inline": True
                            },
                            {
                            "name": "Task Id",
                            "value": f"""{kwargs["task_id"]}""",
                            "inline": True
                            },
                            {
                            "name": "Job Id",
                            "value": f"""{kwargs["job_id_"]}""",
                            "inline": True
                            },
                            {
                            "name": "Dag Status",
                            "value": f"""{kwargs["dag_state"]}""",
                            "inline": False
                            },
                            {
                            "name": "Execution Date",
                            "value": f"""{kwargs["exec_date"].strftime('%Y-%m-%d %H:%M:%S')}""",
                            "inline": True
                            },
                            {
                            "name": "End Execution Date",
                            "value": f"""{kwargs["end_date"].strftime('%Y-%m-%d %H:%M:%S')}""",
                            "inline": True
                            },
                            {
                            "name": "Dag duration",
                            "value": f"""{kwargs["dag_duration"]}""",
                            "inline": True
                            },
                    ],
                    "thumbnail": {
                            "url": env["AIRFLOW_ICO"]
                        },
                    "footer": {
                            "text": str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        }
                    }
                ],
            }
    x = requests.post(url, json=json_payload)
    print("Alert messess status: ",x)
