from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///sql_alchemy_lenteles_sasajos_05-15/m2m.db')
Base = declarative_base()

class Customer(Base):
    __tablename__= 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column("name"), String
    l_name = Column("last_name"), String
    email = Column("email"), String
    orders = relationship("Order_", back_populates="customers")

    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def __repr__(self):
        return f"{self.id}, {self.f_name}, {self.l_name}, {self.email}, {self.orders}"
    

class Order_(Base):
    __tablename__ = 'order_'
    id = Column(Integer, primary_key=True)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.id"))
    date_ = Column("date", String)
    status_id = Column("status_id", Integer, ForeignKey("status.id"))
    customers = relationship("Customer", back_populates="orders")
    products = relationship("Product", back_populates="order")
    status = relationship("Status", back_populates="orders" )

    def __init__(self, customer_id, date, status_id):
        self.customer_id = customer_id
        self.date = date
        self.status_id = status_id
    
    def __repr__(self):
        return f"{self.id}, {self.customer_id}, {self.date_}, {self.customers}, {self.products}, {self.status}"
    


class Status(Base):
    __tablename__ = 'status'
    id = Column( Integer, primary_key=True)
    name = Column('name', String)
    orders = relationship("Order_", back_populates="status")

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.orders}"

class Product(Base):
    __tablename__ = 'product'
    id = Column( Integer, primary_key=True)
    name = Column("name", String)
    price = Column('price', Integer)
    orders = relationship("Product_order", back_populates='product')

    def __init__(self, name, price, orders):
        self.name = name
        self.price = price
        self.orders = orders

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.orders}"


class Product_order(Base):
    __tablename__ = 'product_order'
    id = Column(Integer, primary_key=True)
    order_id = Column('order_id', Integer, ForeignKey("order_.id"))
    product_id = Column('product_id', Integer, ForeignKey("product.id"))
    quantity = Column('quantity', Integer)
    order = relationship("Order", back_populates="products")
    product = relationship("Product", back_populates="orders")

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"{self.id}, {self.order_id}, {self.product_id}, {self.order}, {self.product}"

Base.metadata.create_all(engine)
 
    
