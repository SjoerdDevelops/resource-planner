from peewee import SqliteDatabase, Model, IntegerField, DoubleField, CharField

db = SqliteDatabase("database.db")


# TODO: Enforce acceptable values for the database entries
# TODO: Split the database model into seperate models
class EmployeeModel(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    surname = CharField()
    fte = DoubleField()
    utilization_rate = DoubleField()
    username = CharField(unique=True)
    acronym = CharField(unique=True)

    class Meta:
        database = db


db.create_tables([EmployeeModel])
