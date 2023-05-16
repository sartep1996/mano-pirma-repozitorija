from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from m2m import Base, Customer, Order_, Status, Product, Product_order

engine = create_engine('sqlite:///sql_alchemy_lenteles_sasajos_05-15/m2m.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_customer (f_name, l_name, email):
    customer = Customer(f_name=f_name, l_name=l_name, email=email)
    session.add(customer)
    session.commit()

def add_product(name, price):
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()

def add_status(name):
    status = Status(name=name)
    session.add(status)
    session.commit()

def add_order(customer_id, date_, status_id):
    order = Order_(customer_id, date_, status_id)
    session.add(order)
    session.commit()

def show_order_by_id(entered_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    order_id = session.query(Order_).filter_by(product=entered_id).first().id
    print (order_id)

def change_order_status(order_id, updated_status):
    Session = sessionmaker(bind=engine)
    session = Session()
    order_ = session.query(Order_).filter_by(Order_.id == order_id).one()
    order_.status_id = updated_status
    session.commit()
    new_status = session.query(Status).get(updated_status)
    return new_status

def add_order_with_quantities(order_id, product_id, quantity):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    order_id = session.query(Order_).filter(Order_.id == order_id).one()
    product_id = session.query(Product_order).filter(Product.id == product.id).one()

    if product_id and order_id:
        product_order = Product_order(order_id=order_id, product_id=product_id, quantity=quantity)
        session.add(product_order)
        session.commit()


while True:
    print("Choose what you would like to do: \n 1 - Add customer \n 2 - Add product \n 3 - Add status \n 4 - Add order id \n 5 - Show order by id \n 6 - Change order status \n 7 - Add order with quantities")

    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        f_name = input("Enter customer's name: ")
        l_name = input("Enter customer's last name: ")
        email = input("Enter customer's email: ")
    
    add_customer(f_name, l_name, email)


    if choice == 2:
        name = input("Enter product's name: ")
        price = input ("Enter product's price: ")

    add_product(name, price)

    if choice == 3:
        name = input("Please enter status name: ")

    add_status(name)

    if choice == 4:
        customer_id = int(input("Please enter customer'd id: "))
        date_ = input("Please enter date")
        status_id = int(input("Please enter status id"))

    add_order(customer_id, date_, status_id)
        
    if choice == 5:
        entered_id = int(input("Please enter order's id: "))

    show_order_by_id(entered_id)

    if choice == 6: 
        order_id = int(input("Please enter order's id"))
        updated_status = int("Please enter updated status")

    change_order_status(order_id, updated_status)
    
    if choice == 7:
        order_id = int(input("Please enter oder id: "))
        product = input("Please enter product: ")
        quantity = int(input("Please enter quantity: "))
    
    add_order_with_quantities(order_id, product, quantity)

    if choice ==8:
        order_id = int(input("Please enter your order id: "))
        product_id = int(input("Please enter your product id: "))
        quantity = int(input("Please enter your quantity: "))
    