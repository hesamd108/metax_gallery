import os

import py_eureka_client.eureka_client as eureka_client
from dotenv import load_dotenv

load_dotenv()


def eureka_init():
    if os.environ.get("RUN_MAIN"):
        eureka_client.init(eureka_server=os.getenv('EUREKA_SERVER'),
                           app_name=os.getenv('EUREKA_APP_NAME'),
                           instance_port=int(os.getenv('GATEWAY_PORT')))
        print("Eureka client is running")


def stop_eureka():
    if os.environ.get("RUN_MAIN"):
        eureka_client.stop()
        print("Stopping Eureka client")
