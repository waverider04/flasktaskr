# project/test.py


import os
import unittest


from views import app, db
from _config import basedir
from models import User


TEST_DB = 'test.db'



class AllTests(unittest.TestCase):

	############################
	#### setup and teardown ####
	############################

	# execute prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
			os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()


	# executed after each test
	def tearDown(self):
		db.session.remove()
		db.drop_all()


	# each test should start with 'test'
	def test_user_setup(self):
		new_user = User("waverider", "waverider04@gmail.com", "waverider04")
		db.session.add(new_user)
		db.session.commit()


if __name__ == "__main__":
	unittest.main()