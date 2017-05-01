from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123456@127.0.0.1/SmartCard'
db = SQLAlchemy(app)


class Lost(db.Model):
	__tablename__ = 'LOST'
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_charset': 'utf8mb4'
	}
	pub_date = db.Column(db.DateTime)
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	card_owner = db.Column(db.String(50), nullable=False)
	card_number = db.Column(db.String(11), nullable=False)
	
	def __init__(self, id, card_owner, card_number, pub_date=None):
		self.id = id
		self.card_owner = card_owner
		self.card_number = card_number
		if pub_date is None:
			pub_date = datetime.utcnow()
		self.pub_date = pub_date
		
	
	def __repr__(self):
		return '<LOST %r' % self.lostid
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
	
	def updata(self):
		db.session.commit()
		return self
		
