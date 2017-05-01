from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123456@127.0.0.1/SmartCard'
db = SQLAlchemy(app)


class Feedback(db.Model):
	__tablename__ = 'Feedback'
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_charset': 'utf8mb4'
	}
	
	pub_date = db.Column(db.DateTime)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	wc_openid = db.Column(db.String(50), primary_key=True, nullable=False)
	feedback = db.Column(db.String(100), nullable=False)
	
	def __init__(self, id, wc_openid, feedback, pub_date=None):
		self.id = id
		self.wc_openid = wc_openid
		self.feedback = feedback
		self.wc_username = wc_username
		if(pub_date is None):
			self.pub_date = datetime.utcnow()
		self.pub_data = pub_date
		

		
	def __repr__(self):
		return '<USERS id %r>' % self.id
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
	
	def updata(self):
		db.session.commit()
		return self
		

db.create_all()
	