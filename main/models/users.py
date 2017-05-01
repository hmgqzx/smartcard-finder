from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123456@127.0.0.1/SmartCard'
db = SQLAlchemy(app)


class Users(db.Model):
	__tablename__ = 'USERS'
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_charset': 'utf8mb4'
	}
	
	userid = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	wc_openid = db.Column(db.String(50), primary_key=True, nullable=False)
	wc_username = db.Column(db.String(50), nullable=False)
	
	name = db.Column(db.String(50),nullable=False)
	roll_number = db.Column(db.String(10), nullable=False)
	card_number = db.Column(db.String(6), nullable=False)
	
	phone = db.Column(db.String(11), nullable=False)
	email = db.Column(db.String(50), nullable=False)

	card_status = db.Column(db.Integer(1), nullable=False, default=0)
	
	def __init__(self, userid, wc_openid, wc_username, name, roll_number, card_number, phone, email, card_status):
		self.userid = userid
		self.wc_openid = wc_openid
		self.wc_username = wc_username
		
		self.name = name
		self.roll_number = roll_number
		self.card_number = card_number
		
		self.phone = phone
		self.email = email
		
		self.card_status = card_status
		
		

		
	def __repr__(self):
		return '<USERS userid %r>' % self.userid
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
	
	def updata(self):
		db.session.commit()
		return self
		
		