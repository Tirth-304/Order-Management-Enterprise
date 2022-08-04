import pandas as pd
import random

# Customer
data = pd.read_csv(r'../DummyData/Customer.csv')
for i in data.index:
    print("('{}' , '{}' , '{}' , '{}' , '{}')".format(data['first_name'][i], data['last_name'][i], data['email'][i], data['phone'][i], data['address'][i]))

# Supplier Data
data = pd.read_csv(r'../DummyData/Supplier.csv')

for i in data.index:
    print("('{}' , '{}' , '{}' , '{}' , ".format(data['company_name'][i] , data['address'][i] , data['phone'][i] , data['email'][i]) , end = "")
    if(pd.isna(data['fax'][i])):
        print("NULL".format() , end = " , ")

    else:
        print("'{}'".format(int(data['fax'][i])) , end = " , ")

    if(pd.isna(data['other'][i])):
        print("NULL".format() , end = "),\n")

    else:
        print("'{}'".format(data['other'][i]) , end = "),\n")

# Product Data
data = pd.read_csv(r'../DummyData/Product.csv')

for i in data.index:
    print("('{}' , '{}' , '{}' , 'speed - {}, fuel - {}'".format(data['product_name'][i] , data['discount'][i] , data['supplier_id'][i] , data['speed'][i], data['fuel'][i]) , end = " , ")
    if(pd.isna(data['other'][i])):
        print("NULL".format() , end = "),\n")

    else:
        print("'{}'".format(data['other'][i]) , end = "),\n")

# Category Data
data = pd.read_csv(r'../DummyData/Category.csv')
for i in data.index:
    print("('{}' , '{}' , '{}' , '{}'),".format(data['category_price'][i], data['quantity'][i], data['product_id'][i], data['color'][i]))

# Orders
data = pd.read_csv(r'../DummyData/Order.csv')
for i in data.index:
    print("('{}' , '{}') , ".format(data['date_of_order'][i] , data['customer_id'][i]))

OrderDetails = pd.read_csv(r'../Dummy Data/OrderDetails.csv')
Order = pd.read_csv(r'../Dummy Data/Order.csv')
Category = pd.read_csv(r'../Dummy Data/Category.csv')
Product = pd.read_csv(r'../Dummy Data/Product.csv')

# OrderDetails
for i in OrderDetails.index:
    # print(i)
    print("('{}' , '{}' , '{}' , '{}'".format(OrderDetails['order_id'][i] , OrderDetails['bill_id'][i] , OrderDetails['Quantity'][i] , OrderDetails['category_id'][i]) , end = " , ")
    print("'{}'".format(Category['category_price'][OrderDetails['category_id'][i] - 1]) , end = " , ")
    # print("'{}'".format(Category['color'][OrderDetails['category_id'][i] - 1]) , end = " , ")
    print("'{}'".format(Order['date_of_order'][OrderDetails['order_id'][i] - 1]) , end = " , ")
    print("'{}' ),".format(Product['discount'][Category['product_id'][OrderDetails['category_id'][i] - 1] - 1]))

# Payment
list = ['DebitCard' , 'CreditCard' , 'Banking', 'UPI' , 'Cash On Delivery']
total = [0.0] * 35
for i in OrderDetails.index:
    total[OrderDetails['bill_id'][i] - 1] +=  (Category['category_price'][OrderDetails['category_id'][i] - 1] * (100.0 - Product['discount'][Category['product_id'][OrderDetails['category_id'][i] - 1] - 1]) / 100.0)

temp = 0
for i in OrderDetails.index:
    print("('{}' , '1' , '{}'),".format(random.choice(list) , round(total[OrderDetails['bill_id'][i] - 1]) , 3))