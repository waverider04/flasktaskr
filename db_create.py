# db_crreate.py

from project import db
#from project.models import Task, User
#from datetime import date



# create the database and the db tables
db.create_all()

# # insert data
# db.session.add(
# 	Task("Finish this tutorial", date(2018, 2, 1), 10, date(2018, 2, 1), 1, 1)
# )
# db.session.add(
# 	Task("Finish Real Python", date(2018, 2, 1), 10, date(2018, 2, 1), 1, 1)
# )

# commit the changes
db.session.commit()