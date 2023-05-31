from sqlalchemy import *
from extentions import db, get_current_time


class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    status = Column(String, default='pending')
    price = Column(Integer)
    date_created = Column(String(15), default=get_current_time)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    cart = db.relationship("Cart", backref='payments')