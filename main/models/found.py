from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123456@127.0.0.1/SmartCard'
db = SQLAlchemy(app)


class Found(db.Model):
	__tablename__ = 'FOUND'
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_charset': 'utf8mb4'
	}
	
	fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	
	card_owner = db.Column(db.String(50),nullable=False)
	card_number = db.Column(db.String(6), nullable=False, primary_key=True,)
	roll_number = db.Column(db.String(10), nullable=False)
	acamedy = db.Column(db.String(50), nullable=False)
	
	#二选一：联系我
	picker_name = db.Column(db.String(50), nullable=True)
	picker_long = db.Column(db.String(11), nullable=True)
	picker_short = db.Column(db.String(6), nullable=True)
	#二选一：暂存地点
	deposit_location = db.Column(db.String(50), nullable=True)
		
	def __init__(self, fid, card_owner, card_number, roll_number, picker_name, picker_long, picker_short, deposit_location):
		self.fid = fid
		self.card_owner = picked_card_number
		self.picker_name = picker_name
		self.picker_phone = picker_phone
		self.picker_email = picker_email
		self.deposit_location = deposit_location
		
		
	def __repr__(self):
		return '<LOST %r' % self.fid
		
	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
	
	def updata(self):
		db.session.commit()
		return self