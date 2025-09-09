from peewee import Model, UUIDField, DoubleField, CharField


# TODO: Enforce acceptable values for the database entries
# TODO: Split the database model into seperate models
class EmployeeModel(Model):
    id: UUIDField = UUIDField(primary_key=True)
    name: CharField = CharField()
    surname: CharField = CharField()
    fte: DoubleField = DoubleField()
    utilization_rate: DoubleField = DoubleField()
    username: CharField = CharField(unique=True)
    acronym: CharField = CharField(unique=True)
