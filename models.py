from mongoengine import Document, ListField, StringField, URLField
from mongoengine.fields import BooleanField


class Todo(Document):
    content = StringField(required=True, max_length=70)
    complete = BooleanField(default=False)
