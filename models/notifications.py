from flask_restx import Model, fields
from peewee import SQL, CharField, DateTimeField, IntegerField

from .base import BaseModel


class Notifications(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    type = CharField()
    url = CharField()
    username = CharField(null=True)
    password = CharField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])

NotificationsPostModel = Model('NotificationsPostModel', {
    "name": fields.String(required=True, description="The name of the notification"),
    "type": fields.String(required=True, description="The type of the notification"),
    "url": fields.String(required=True, description="The URL of the notification"),
    "username": fields.String(required=False, description="The username of the notification"),
    "password": fields.String(required=False, description="The password of the notification")
})

NotificationsGetModel = Model('NotificationsGetModel', {
    "id": fields.Integer(required=True, description="The ID of the notification"),
    "name": fields.String(required=True, description="The name of the notification"),
    "type": fields.String(required=True, description="The type of the notification"),
    "url": fields.String(required=True, description="The URL of the notification"),
    "username": fields.String(required=False, description="The username of the notification"),
    "password": fields.String(required=False, description="The password of the notification"),
    "created": fields.DateTime(required=True, description="The date the notification was created")
})