from decouple import config
import boto3

import os
AWS_ACCESS_KEY_ID     = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = os.environ.get("REGION_NAME")
TABLE_NAME = os.environ.get("TABLE_NAME")


client = boto3.client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)
resource = boto3.resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)
todo_list = resource.Table(TABLE_NAME)

def addItemToBook(id, todo):
    resp = todo_list.put_item(
        Item = {
            'id'     : id,
            'todo': todo
        }
    )
    return resp

def GetItemFromBook(id):
    response = todo_list.get_item(
        Key = {
            'id'     : id
        },
        AttributesToGet=[
            'todo'
        ]
    )
    return response


def UpdateItemInBook(id, data:dict):
    response = todo_list.update_item(
        Key = {
            'id': id
        },
        AttributeUpdates={
            'title': {
                'Value'  : data['todo'],
                'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
            }
        },
        ReturnValues = "UPDATED_NEW" # returns the new updated values
    )
    return response



def DeleteAnItemFromBook(id):
    response = todo_list.delete_item(
        Key = {
            'id': id
        }
    )
    return response