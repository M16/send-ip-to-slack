#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import logging
import configparser
import requests
import pathlib

logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()

ip_refelctor_response = requests.get('http://ip.fyr.io/', timeout=10)

config_path = str(pathlib.Path(__file__).parent.absolute()) + '/config.ini'

config.read(config_path)

message = str(config['device']['name']) + " is connected with IP:" + str(ip_refelctor_response.content)

slackQueryData = '''{
    "channel": "#''' + config['slack']['channel'] + '''",
    "username": "''' + config['slack']['username'] + '''",
    "icon_emoji": ":''' + config['slack']['icon_emoji'] + ''':",
    "type": "''' + config['slack']['type'] + '''",
    "text": "''' + message + '''",
    }'''

response = requests.post(config['slack']['url'], data=slackQueryData)
