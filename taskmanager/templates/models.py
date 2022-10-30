from taskmanager import db


class Category(db.Model):
    # schema for the Category Model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string



class Task(db.Model):
    # scchema foor the Task model
    id = db.Column(db.Integer, primary_key=True)
