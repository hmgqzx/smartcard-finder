from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123456@127.0.0.1/SmartCard'
db = SQLAlchemy(app)


class Users(db.Model):
	__tablename__ = 'USERS'
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_charset': 'utf8mb4'
	}
	
	pub_date = db.Column(db.DateTime)
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	wc_openid = db.Column(db.String(50), primary_key=True, nullable=False)
	wc_username = db.Column(db.String(50), nullable=False)
	
	name = db.Column(db.String(50),nullable=False)
	roll_number = db.Column(db.String(10), nullable=False)
	card_number = db.Column(db.String(6), nullable=False, unique=True)  #唯一性
	
	phone = db.Column(db.String(11), nullable=False)
	email = db.Column(db.String(50), nullable=False)

	card_status = db.Column(db.Integer, nullable=False)
	
	def __init__(self, id, wc_openid, wc_username, name, roll_number, card_number, phone, email, card_status, pub_date=None):
		self.id = id
		self.wc_openid = wc_openid
		self.wc_username = wc_username
		
		self.name = name
		self.roll_number = roll_number
		self.card_number = card_number
		
		self.phone = phone
		self.email = email
		
		self.card_status = card_status
		
		if(pub_date is None):
			self.pub_date = datetime.utcnow()
		self.pub_data = pub_date
		

		
	def __repr__(self):
		return '<USERS userid %r>' % self.id
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
	
	def updata(self):
		db.session.commit()
		return self
		
		