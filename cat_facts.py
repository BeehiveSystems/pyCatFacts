#!/usr/bin/python3

import random
import string
import json
import time
import boto3
import aws_credentials as config


list_of_contacts = [] #Insert phone numbers as +12223334444
facts = json.loads(open("facts.json").read())

client = boto3.client(
    "sns",
    aws_access_key_id = config.aws_credentials["aws_access_key_id"],
    aws_secret_access_key = config.aws_credentials["aws_secret_access_key"],
    region_name="us-east-1"
)

topic = client.create_topic(Name="fucking-cat-facts")
topic_arn = topic['TopicArn']

for number in list_of_contacts:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol="sms",
        Endpoint=number
    )

def send_cat_fact(client, facts):
    client.publish(
        TopicArn=topic_arn,
        Message = f"{random.choice(facts)}"
    )

for fact in facts:
    send_cat_fact(client, facts)
    break
