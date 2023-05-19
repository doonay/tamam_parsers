from peewee import *
from playhouse.postgres_ext import ArrayField
from config import db_name, user, password, host, port

# Установка параметров подключения к базе данных
db = PostgresqlDatabase(
    db_name,
    user=user,
    password=password,
    host=host,
    port=port
)

class Game(Model):
    game_id = CharField()
    title = CharField()
    platforms = ArrayField(CharField)
    base_price = DecimalField(decimal_places=2)
    discounted_price = DecimalField(decimal_places=2, null=True)
    discount = IntegerField(null=True)
    img = CharField()
    last_modified = TimestampField()

    class Meta:
        database = db

    @classmethod
    def table_name(cls, company):
        return f'{cls._meta.database}_{company}_games'