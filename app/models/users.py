from tortoise import fields
from tortoise.models import Model


class Users(Model):
    id = fields.IntField(pk=True)

    email = fields.CharField(max_length=255, null=False)
    hashed_password = fields.CharField(max_length=255, null=False)
