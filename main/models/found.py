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
	picked_card_number = db.Column(db.String(6), primary_key=True,nullable=False)
	picker_name = db.Column(db.String(50), nullable=True)
	picker_phone = db.Column(db.String(11), nullable=True)
	picker_email = db.Column(db.String(50), nullable=True)
	deposit_location = db.Column(db.String(50), nullable=True)
		
	def __init__(self, fid, picked_card_number, picker_name, picker_phone, picker_email, deposit_location):
		self.fid = fid
		self.picked_card_number = picked_card_number
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