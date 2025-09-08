from peewee import Model, UUIDField, DoubleField, CharField


# TODO: Enforce acceptable values for the database entries
# TODO: Split the database model into seperate models
class EmployeeModel(Model):
    id = UUIDField(primary_key=True)
    name = CharField()
    surname = CharField()
    fte = DoubleField()
    utilization_rate = DoubleField()
    username = CharField(unique=True)
    acronym = CharField(unique=True)
