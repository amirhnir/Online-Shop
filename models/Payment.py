from sqlalchemy import *
from extentions import db


class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    status = Column(String, default='pending')
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    cart = db.relationship("Cart", backref='payments')