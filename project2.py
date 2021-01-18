#-----------------------------------------------------------------------------
#Seelam J Sidhu - XII A - Project: Sales Managment - Final
#-----------------------------------------------------------------------------

import random
import os
import csv
import datetime

#-----------------------------------------------------------------------------
# items file ---> [item code, item name, item price, item quantity]
#                      0           1        2              3
# sales file ---> [item code, item name, item price, item quantity needed, item amount]
#                      0           1        2              3                   4

# menu :
# 1  --> display items
# 2  --> add items
# 3  --> delete items
# 4  --> update items price         --> increase or decrease
# 5  --> update items quantity      --> increase
# 5  --> search items               --> name or code
# 6  --> sort by quantity less than
# 7  --> sort by quantity more than
# 8  --> sort by price less than
# 9  --> sort by price more than
# 10 --> sell items                 --> bill and sales         --> bill for costumers and sales for statiscs purpose and record 
# 11 --> daily statistics 
# 12 --> monthly 
# 13 --> yearly
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
fn1 = 'items.csv'
#-----------------------------------------------------------------------------

def Create_items():
    f1 = open(fn1,'w')
    f1.close()

#-----------------------------------------------------------------------------

def add_items():
    # -----------------------------------------
    # This function is used to add more items in the items file ---- csv
    # -----------------------------------------
    f1 = open(fn1,'a',newline='')
    csv_wo = csv.writer(f1)
    while True:
        while True:
            code = input("Enter code of the item: ")
            if len(code) != 4:
                print("Invalid code. Please reenter")
            else:
                break
        item = input("Enter name of item (max 50 characters long): ")
        item = f'{item:.50}'
        price = float(input("Enter unit price: "))
        qty = int(input("Enter quantity (in stock): "))
        rec = [code, item, price, qty]
        csv_wo.writerow(rec)
        more=input("More data (y/n)?")
        if more in 'Nn':
            break
    f1.close()
    
#-----------------------------------------------------------------------------

def display_items():
    # -----------------------------------------
    # this function displays the items of the items file --- csv
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    f1 = open(fn1 , 'r')
    print('-' * 82)
    rec = f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^15}"
    print(rec)
    print('-' * 82)
    csv_reader = csv.reader(f1)
    for rec in csv_reader:
        rec = f"{rec[0]:^5s} {rec[1]:50s} {float(rec[2]):^7.3f} {int(rec[3]):^15}"
        print(rec)
    print('-' * 82)
    print()

#-----------------------------------------------------------------------------

def delete_items():
    # -----------------------------------------
    # this function deleted items from the items file --- csv
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    f1 = open(fn1, 'r+', newline='')
    csv_reader = csv.reader(f1)
    newrec = []
    code = input("Enter code of the item which has to be deleted: ")
    found = 0
    for rec in csv_reader:
        if code == (rec[0]):
            found = 1
        else:
            newrec += [rec]
    if found == 1:
        f1.seek(0)
        csv_writer = csv.writer(f1)
        csv_writer.writerows(newrec)
        f1.close()
        print('Record has been deleted')
    else:
        print(code, 'is not found in the record')
    f1.close()

#-----------------------------------------------------------------------------
    
def update_items_price_inc():
    # -----------------------------------------
    # this function increases the price of the item
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    f1 = open(fn1, 'r+', newline='')
    csv_reader = csv.reader(f1)
    newlist = []
    rec_found = 0
    code = int(input('Enter the code of the item which has to be updated: '))
    n = float(input('Enter the amount of price you want to increase: '))
    for rec in csv_reader:
        if code == int(rec[0]):
            rec[2] = str(float(rec[2]) + n)
            rec_found = 1
        newlist += [rec]
    if rec_found == 1:
        f1.seek(0)
        t1 = csv.writer(f1)
        t1.writerows(newlist)
        print('record have been edited')
    else:
        print(code,'has not been found in the list')
    f1.close()

#-----------------------------------------------------------------------------
    
def update_items_price_dec():
    # -----------------------------------------
    # this function increases the price of the item
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    f1 = open(fn1, 'r+', newline='')
    csv_reader = csv.reader(f1)
    newlist = []
    rec_found = 0
    code = int(input('Enter the code of the item which has to be updated: '))
    n = float(input('Enter the amount of price you want to decrease: '))
    for rec in csv_reader:
        if int(rec[0]) == code:
            rec[2] = str(float(rec[2]) - n)
            rec_found = 1
        newlist += [rec]
    if rec_found == 1:
        f1.seek(0)
        t1 = csv.writer(f1)
        t1.writerows(newlist)
        print('record have been edited')
    else:
        print(code,'has not been found in the list')
    f1.close()


#-----------------------------------------------------------------------------
    
def update_items_quantity_inc():
    # -----------------------------------------
    # this function increases the quantity of the item      --- by default it increases by 20
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    f1 = open(fn1, 'r+', newline='')
    csv_reader = csv.reader(f1)
    newlist = []
    rec_found = 0
    n = 20
    for rec in csv_reader:
        if int(rec[0]) <= n:
            rec[3] = str(int(rec[3]) + n)
            rec_found = 1
        newlist += [rec]
    if rec_found == 1:
        f1.seek(0)
        t1 = csv.writer(f1)
        t1.writerows(newlist)
        print('record have been edited')
    else:
        print(code,'has not been found in the list')
    f1.close()
    
#-----------------------------------------------------------------------------

def search_name():
    # -----------------------------------------
    # this function seaches for the item from item file  ---- you must write the exact name of the item
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_name = input('Enter the item to be searched: ')
    found = 0
    f1 = open(fn1, 'r')
    csv_reader = csv.reader(f1)
    for rec in csv_reader:
        if rec[1] == search_name:
            print('-' * 82)
            print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
            print('-' * 82)
            rec = f"{rec[0]:^5s} {rec[1]:50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            print()
            found = 1
            break
    f1.close()
    if found == 0:
        print(search_name , 'is not found in the list')

#-----------------------------------------------------------------------------
def search_code():
    # -----------------------------------------
    # this function seaches for the item from item file  ---- you must write the exact code of the item
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_code = input('Enter the code to be searched: ')
    found = 0
    f1 = open(fn1 , 'r')
    csv_reader = csv.reader(f1)
    for rec in csv_reader:
        if rec[0] == search_code:
            print('-' * 82)
            print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
            print('-' * 82)
            rec = f"{rec[0]:^5s} {rec[1]:^50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            print()
            found = 1
            break
    f1.close()
    if found == 0:
        print(search_code, 'is not found in the list')
    print()
    
#-----------------------------------------------------------------------------

def quantity_less_than():
    # -----------------------------------------
    # sorts the items less than the quantity user enters
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_qty = int(input('Enter the quantity of whose items you need: '))
    found = 0
    f1 = open(fn1 , 'r')
    csv_reader = csv.reader(f1)
    print('-' * 82)
    print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
    print('-' * 82)
    for rec in csv_reader:
        if int(rec[3]) <  search_qty:
            rec = f"{rec[0]:^5s} {rec[1]:^50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            found = 1
    if found == 0:
        print(search_qty, 'is not found in the list')
    f1.close()
    print()

#-----------------------------------------------------------------------------

def quantity_more_than():
    # -----------------------------------------
    # sorts the items more than the quantity user enters
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_qty = int(input('Enter the quantity of whose items you need: '))
    found = 0
    f1 = open(fn1 , 'r')
    csv_reader = csv.reader(f1)
    print('-' * 82)
    print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
    print('-' * 82)
    for rec in csv_reader:
        if int(rec[3]) > search_qty:
            rec = f"{rec[0]:^5s} {rec[1]:^50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            found = 1
    if found == 0:
        print(search_qty, 'is not found in the list')
    f1.close()
    print()

#-----------------------------------------------------------------------------

def price_less_than():
    # -----------------------------------------
    # sorts the items less than the price user enters   --- you must enter the price in the format NNN.NNN
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_price = float(input('Enter the price of whose items you need: '))
    found = 0
    f1 = open(fn1 , 'r')
    csv_reader = csv.reader(f1)
    print('-' * 82)
    print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
    print('-' * 82)
    for rec in csv_reader:
        if float(rec[2]) <  search_price:
            rec = f"{rec[0]:^5s} {rec[1]:^50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            found = 1
    if found == 0:
        print(search_price, 'is not found in the list')
    f1.close()
    print()

#-----------------------------------------------------------------------------

def price_more_than():
    # -----------------------------------------
    # sorts the items more than the price user enters   --- you must enter the price in the format NNN.NNN
    #  CODE  ITEM  PRICE  QUANTITY
    #   0      1    2        3
    # -----------------------------------------
    search_price = float(input('Enter the price of whose items you need: '))
    found = 0
    f1 = open(fn1 , 'r')
    csv_reader = csv.reader(f1)
    print('-' * 82)
    print(f"{'CODE':^5s} {'ITEM':^50s} {'PRICE':^7s} {'QUANTITY IN STOCK':^8}")
    print('-' * 82)
    for rec in csv_reader:
        if float(rec[2]) > search_price:
            rec = f"{rec[0]:^5s} {rec[1]:^50s} {float(rec[2]):^7.3f} {float(rec[3]):^8.3f}"
            print(rec)
            print('-' * 82)
            found = 1
    if found == 0:
        print(search_price, 'is not found in the list')
    f1.close()
    print()
    
# -----------------------------------------------------------------------
fn2 = 'sales.csv'
fn3 = 'bill_costumer.csv'
# -----------------------------------------------------------------------

def Create_sales():
    f1 = open(fn2,'w')
    f1.close()
    f1 = open(fn3,'w')
    f1.close()

#-----------------------------------------------------------------------------
    
def sell_items():
    
    # -----------------------------------------
    # this is the file which is going to with costumer
    # sr_no ... code ... item ... price ... quantity sold  ... amount ... date of purchase ... cash memo
    #   0   ...  1   ...  2   ...   3   ...     4          ...   5    ...      6           ...    7
    # cash memo and date of purchase in list for later purpose
    # -----------------------------------------
    
    f1 = open(fn1,'r+', newline = '')
    csv_reader = csv.reader(f1)
    found = 0
    total_price = 0
    n = int(input('Enter the number of items you want to order: '))
    # -----------------------------------------
    print()
    print(f"{'WELCOME TO APPLE STORE':^95}")
    print()
    print()
    print('-' * 95)
    print(f" {'COSTUMER BILL':^94}")
    print('-' * 95)
    cash_memo = random.randint(1000,9999)
    date_of_purchase = datetime.date.today()
    print(f" {'CASHMEMO':^10s} {cash_memo} {' ':45} {'DATE OF PURCHASE':^20} {date_of_purchase}")
    print('-' * 95)
    print()
    srno = 0
    f2 = open(fn2, 'a', newline='')
    f3 = open(fn3, 'w', newline='')
    csv_writer_f2 = csv.writer(f2)
    csv_writer_f3= csv.writer(f3)

    for i in range(n):
        newlist_rec = []
        print()
        while True:
            code = (input('Enter the code of the item: '))
            if len(code) != 4:
                print('Enter a valid code')
            else:
                break
        print()
        qty = int(input('Enter the quantity in need: '))
        print()
        
        # -----------------------------------------
        for rec in csv_reader:
            if code == rec[0] and int(rec[3]) >= qty:
                srno += 1
                amt = float(rec[2])*qty
                total_price += amt
                newrec = [int(srno), rec[0],rec[1],float(rec[2]),qty, amt,date_of_purchase,cash_memo]
                rec[3] = str(int(rec[3]) - qty)
                newrec1 = f" {int(newrec[0]):^5d} {newrec[1]:^5s} {newrec[2]:^50s} {float(newrec[3]):^8.3f} {int(newrec[4]):^13d} {float(newrec[5]):^8.3f}"
                found = 1
            elif code==rec[0] and int(rec[3]) < qty:
                print('There is not enough stock')
                found = 0
                break
            
            newlist_rec += [rec]

        csv_reader=newlist_rec

        if found == 1:
            csv_writer_f2.writerow(newrec)
            csv_writer_f3.writerow(newrec)
            print()
            print(f"{'WELCOME TO APPLE STORE':^95}")
            print('-' * 95)
            print(f" {'COSTUMER BILL':^94}")
            print('-' * 95)
            print(f" {'SR NO':^6s}{'CODE':^5s} {'ITEM':^50s} {'PRICE':^8s} {'QUANTITY SOLD'} {'AMOUNT':^8s}")
            print('-' * 95)
            print(f" {int(newrec[0]):^5d} {newrec[1]:^5s} {newrec[2]:^50s} {float(newrec[3]):^8.3f} {int(newrec[4]):^13d} {float(newrec[5]):^8.3f}")
            print('-'*95)
            print('Total Price till now: ',total_price)
            print('-'*95)
        else:
            print("Enter valid code")
    
    f1.seek(0)
    t_rec=csv.writer(f1)
    t_rec.writerows(newlist_rec)
       
    f2.close()
    f3.close()
    f1.close()
    
#-----------------------------------------------------------------------------

def sales_daily():
    f2 = open(fn2,'r')
    csv_reader = csv.reader(f2)

    # ----------- Date : YYYY - MM - DD -------------
    
    # -----------------------------------------
    date_today = datetime.date.today()
    date_today = str(date_today)
    # -----------------------------------------
    print()
    print('-' * 95)
    print(f"{'WELCOME TO APPLE STORE':^95}")
    print('-' * 95)
    print(f" {'CODE':^5s} {'ITEM':^50s} {'PRICE':^8s} {'QUANTITY SOLD'} {'AMOUNT':^8s}")
    print('-' * 95)
    found = 0
    # -----------------------------------------
    for rec in csv_reader:
        if (rec[6]) == (date_today):
            print(f" {rec[1]:^5s} {rec[2]:^50s} {float(rec[3]):^8.3f} {int(rec[4]):^13d} {float(rec[5]):^8.3f}") 
            print('-' * 95)
            found = 1
    if found == 0:
        print(f"{'No Sales Made Today :(': ^95}")
        print('-'*95)
            

#-----------------------------------------------------------------------------

def sales_yearly():
    f2 = open(fn2,'r')
    csv_reader = csv.reader(f2)

    # ----------- Date : YYYY - MM - DD -------------
    
    # -----------------------------------------
    date_year = int(input('Enter the year of the sales to be sorted: '))
    year_starting = datetime.date(date_year,1,1)
    ys = str(year_starting)
    yt = datetime.datetime.strptime(ys, '%Y-%m-%d')
    yt = yt.year
    found = 0
    # -----------------------------------------
    print()
    print('-' * 95)
    print(f"{'WELCOME TO APPLE STORE':^95}")
    print('-' * 95)
    print(f" {'CODE':^5s} {'ITEM':^50s} {'PRICE':^8s} {'QUANTITY SOLD'} {'AMOUNT':^8s}")
    print('-' * 95)
    # -----------------------------------------
    for rec in csv_reader:
        ds = rec[6]
        dt = datetime.datetime.strptime(ds, '%Y-%m-%d')
        dt = dt.year
        if yt == dt:
            print(f" {rec[1]:^5s} {rec[2]:^50s} {float(rec[3]):^8.3f} {int(rec[4]):^13d} {float(rec[5]):^8.3f}") 
            print('-' * 95)
            found = 1
    if found == 0:
        print(f"{'No Sales Made This Year :(': ^95}")
        print('-'*95)

#-----------------------------------------------------------------------------

def sales_monthly():
    f2 = open(fn2,'r')
    csv_reader = csv.reader(f2)

    # ----------- Date : YYYY - MM - DD -------------
    
    # -----------------------------------------
    date_year = int(input('Enter the year of the sales to be sorted: '))
    date_month = int(input('Enter the month of the sales to be sorted (enter 0 before 1 digit month): '))
    year_starting = datetime.date(date_year,date_month,1)
    ys = str(year_starting)
    ms = str(year_starting)
    yt = datetime.datetime.strptime(ys, '%Y-%m-%d')
    yt = yt.year
    mt = datetime.datetime.strptime(ms, '%Y-%m-%d')
    mt = mt.month
    found = 0
    # -----------------------------------------
    print()
    print('-' * 95)
    print(f"{'WELCOME TO APPLE STORE':^95}")
    print('-' * 95)
    print(f" {'CODE':^5s} {'ITEM':^50s} {'PRICE':^8s} {'QUANTITY SOLD'} {'AMOUNT':^8s}")
    print('-' * 95)
    # -----------------------------------------
    for rec in csv_reader:
        ds = rec[6]
        dt = datetime.datetime.strptime(ds, '%Y-%m-%d')
        dt = dt.month
        if mt == dt:
            print(f" {rec[1]:^5s} {rec[2]:^50s} {float(rec[3]):^8.3f} {int(rec[4]):^13d} {float(rec[5]):^8.3f}") 
            print('-' * 95)
            found = 1
    if found == 0:
        print(f"{'No Sales Made This Month :(': ^95}")
        print('-'*95)


#-----------------------------------------------------------------------------
# menu :
# 1  --> display items
# 2  --> add items
# 3  --> delete items
# 4  --> update items price         --> increase or decrease
# 5  --> update items quantity      --> increase
# 6  --> search items               --> name or code
# 7  --> sort by quantity           --> more than or less than
# 8  --> sort by price              --> more than or less than
# 9  --> sell items                 --> bill and sales         --> bill for costumers and sales for statiscs purpose and record 
# 10  --> daily sales statistics 
# 11 --> monthly sales statistics 
# 12 --> yearly sales satistics
# 
#-----------------------------------------------------------------------------

menu = '''
-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------
'''
while True:
    print(menu)
    opt = int(input('Enter the option for the opertion of the program: '))
    if opt == 1:
        print()
        display_items()
        print()
    if opt == 2:
        print()
        add_items()
        print()
    if opt == 3:
        print()
        delete_items()
        print()
    if opt == 4:
        while True:
            update_price_menu ='''
                1. Increase the price of items
                2. Decrease the price of items
                0. Break
            '''
            print(update_price_menu)
            opt2 = int(input('Do you want to increase or decrease the price (1->inc, 2->dec): '))
            if opt2 == 1:
                print()
                update_items_price_inc()
                print()
            if opt2 == 2:
                print()
                update_items_price_dec()
                print()
            if opt2 == 0:
                print()
                break
    if opt == 5:
        print()
        print('By default the quantity will increase by 20')
        print()
        update_items_quantity_inc()
        print()
    if opt == 6:
         while True:
            search_items ='''
                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            '''
            print(search_items)
            opt2 = int(input('Do you want to search item or code (1->code, 2->item): '))
            if opt2 == 1:
                print()
                search_code()
                print()
            if opt2 == 2:
                print()
                search_name()
                print()
            if opt2 == 0:
                print()
                break
    if opt == 7:
         while True:
            sort_quantity ='''
                1. Sort quantity more than
                2. Sort quantity less than
                0. Break
            '''
            print(sort_quantity)
            opt2 = int(input('Do you want to sort quantity (1->more, 2->less): '))
            if opt2 == 1:
                print()
                quantity_more_than()
                print()
            if opt2 == 2:
                print()
                quantity_less_than()
                print()
            if opt2 == 0:
                print()
                break
    if opt == 8:
        while True:
            sort_price ='''
                1. Sort price more than
                2. Sort price less than
                0. Break
            '''
            print(sort_price)
            opt2 = int(input('Do you want to sort quantity (1->more, 2->less): '))
            if opt2 == 1:
                print()
                price_more_than()
                print()
            if opt2 == 2:
                print()
                price_less_than()
                print()
            if opt2 == 0:
                print()
                break
    if opt == 9:
        print()
        sell_items()
        print()
    if opt == 10:
        print()
        sales_daily()
        print()
    if opt == 11:
        print()
        sales_monthly()
        print()
    if opt == 12:
        print()
        sales_yearly()
        print()
    if opt == 0:
        print()
        break
    
#-----------------------------X----------------------------X--------------------
# Sample Output of the project
#-----------------------------X----------------------------X--------------------

'''
-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 1

----------------------------------------------------------------------------------
CODE                         ITEM                         PRICE  QUANTITY IN STOCK
----------------------------------------------------------------------------------
0001  Iphone 6s 64 GB                                    80.000        14       
0002  Iphone 6s Plus 128 GB                              99.999        20       
0003  Iphone 7 plus 128 GB                               135.500       25       
0004  Iphone 7 plus 256 GB                               145.500       28       
0005  Iphone 8 plus 256 GB                               160.000       26       
0006  Iphone X 512 GB                                    300.000       41       
0007  Iphone XS Max 256 GB                               270.450       50       
0008  Iphone SE                                          194.999       35       
0009  Iphone 11 256 GB                                   284.000       60       
0010  Iphone 11 Pro Max 256 GB                           360.550       70       
0011  Imac intel core i7 16GB RAM 2TB SSD                899.999       30       
0012  Imac intel core i5 16GB RAM 1TB SSD                500.900       40       
0013  Imac intel core i5 8GB RAM 1TB SSD                 350.900       50       
0014  Imac intel core i3 8GB RAM 1TB SSD                 300.900       50       
0015  Macbook Pro 2020 intel core i9 16GB RAM 1TB SSD    900.900       25       
0016  Macbook Pro 2020 intel core i7 8GB RAM 1TB SSD     800.900       30       
0017  Macbook Pro 2020 intel core i7 8GB RAM 512GB SSD   650.900       35       
0018  Macbook Pro 2019 intel core i7 8GB RAM 512GB SSD   550.900       35       
0019  Macbook Air 2020 intel core i5 8GB RAM 256GB SSD   450.900       39       
0020  Macbook Air 2019 intel core i5 8GB RAM 256GB SSD   350.900       40       
0019  Macbook Air 2015 intel core i5 4GB RAM 128GB SSD   300.900       39       
0021  Macbook Air 2015 intel core i3 4GB RAM 128GB SSD   250.900       40       
0022  Apple Watch Series 6 44mm                          150.750       50       
0023  Apple Watch Series 6 40mm                          145.500       50       
----------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 2

Enter code of the item: 0024
Enter name of item (max 50 characters long): Apple Airpods
Enter unit price: 40.00
Enter quantity (in stock): 50
More data (y/n)?n


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 1

----------------------------------------------------------------------------------
CODE                         ITEM                         PRICE  QUANTITY IN STOCK
----------------------------------------------------------------------------------
0001  Iphone 6s 64 GB                                    80.000        14       
0002  Iphone 6s Plus 128 GB                              99.999        20       
0003  Iphone 7 plus 128 GB                               135.500       25       
0004  Iphone 7 plus 256 GB                               145.500       28       
0005  Iphone 8 plus 256 GB                               160.000       26       
0006  Iphone X 512 GB                                    300.000       41       
0007  Iphone XS Max 256 GB                               270.450       50       
0008  Iphone SE                                          194.999       35       
0009  Iphone 11 256 GB                                   284.000       60       
0010  Iphone 11 Pro Max 256 GB                           360.550       70       
0011  Imac intel core i7 16GB RAM 2TB SSD                899.999       30       
0012  Imac intel core i5 16GB RAM 1TB SSD                500.900       40       
0013  Imac intel core i5 8GB RAM 1TB SSD                 350.900       50       
0014  Imac intel core i3 8GB RAM 1TB SSD                 300.900       50       
0015  Macbook Pro 2020 intel core i9 16GB RAM 1TB SSD    900.900       25       
0016  Macbook Pro 2020 intel core i7 8GB RAM 1TB SSD     800.900       30       
0017  Macbook Pro 2020 intel core i7 8GB RAM 512GB SSD   650.900       35       
0018  Macbook Pro 2019 intel core i7 8GB RAM 512GB SSD   550.900       35       
0019  Macbook Air 2020 intel core i5 8GB RAM 256GB SSD   450.900       39       
0020  Macbook Air 2019 intel core i5 8GB RAM 256GB SSD   350.900       40       
0019  Macbook Air 2015 intel core i5 4GB RAM 128GB SSD   300.900       39       
0021  Macbook Air 2015 intel core i3 4GB RAM 128GB SSD   250.900       40       
0022  Apple Watch Series 6 44mm                          150.750       50       
0023  Apple Watch Series 6 40mm                          145.500       50       
0024  Apple Airpods                                      40.000        50       
----------------------------------------------------------------------------------


#-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 3

Enter code of the item which has to be deleted: 0024
Record has been deleted


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 3

Enter code of the item which has to be deleted: 0025
0025 is not found in the record


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 4

                1. Increase the price of items
                2. Decrease the price of items
                0. Break
            
Do you want to increase or decrease the price (1->inc, 2->dec): 1

Enter the code of the item which has to be updated: 0016
Enter the amount of price you want to increase: 5.500
record have been edited


                1. Increase the price of items
                2. Decrease the price of items
                0. Break

Enter the code of the item which has to be updated: 0017
Enter the amount of price you want to decrease: 50.000
record have been edited


                1. Increase the price of items
                2. Decrease the price of items
                0. Break
            
Do you want to increase or decrease the price (1->inc, 2->dec): 0


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 5

By default the quantity will increase by 20

record have been edited


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
#-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 6

                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            
Do you want to search item or code (1->code, 2->item): 1

Enter the code to be searched: 0001
----------------------------------------------------------------------------------
CODE                         ITEM                         PRICE  QUANTITY IN STOCK
----------------------------------------------------------------------------------
0001                   Iphone 6s 64 GB                   80.000   34.000 
----------------------------------------------------------------------------------




                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            
Do you want to search item or code (1->code, 2->item): 1

Enter the code to be searched: 0099
0099 is not found in the list



                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            
Do you want to search item or code (1->code, 2->item): 2

Enter the item to be searched: Macbook Pro 2020 intel core i9 16GB RAM 1TB SSD
----------------------------------------------------------------------------------
CODE                         ITEM                         PRICE  QUANTITY IN STOCK
----------------------------------------------------------------------------------
0015  Macbook Pro 2020 intel core i9 16GB RAM 1TB SSD    900.900  45.000 
----------------------------------------------------------------------------------



                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            
Do you want to search item or code (1->code, 2->item): 2

Enter the item to be searched: Macbook Pro 2020 intel core i9 16GB RAM
Macbook Pro 2020 intel core i9 16GB RAM is not found in the list


                1. Item code
                2. Item name  --- ( You have to enter the exact name of the item)
                0. Break
            
Do you want to search item or code (1->code, 2->item): 0


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 9

Enter the number of items you want to order: 3

                                    WELCOME TO APPLE STORE                                     


-----------------------------------------------------------------------------------------------
                                         COSTUMER BILL                                         
-----------------------------------------------------------------------------------------------
  CASHMEMO  9950                                                 DATE OF PURCHASE   2020-12-11
-----------------------------------------------------------------------------------------------


Enter the code of the item: 0009

Enter the quantity in need: 2


                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
                                         COSTUMER BILL                                         
-----------------------------------------------------------------------------------------------
 SR NO CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
   1   0009                   Iphone 11 256 GB                  284.000        2       568.000 
-----------------------------------------------------------------------------------------------
Total Price till now:  568.0
-----------------------------------------------------------------------------------------------

Enter the code of the item: 0019

Enter the quantity in need: 1


                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
                                         COSTUMER BILL                                         
-----------------------------------------------------------------------------------------------
 SR NO CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
   3   0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        1       300.900 
-----------------------------------------------------------------------------------------------
Total Price till now:  1319.8
-----------------------------------------------------------------------------------------------

Enter the code of the item: 0024

Enter the quantity in need: 1


                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
                                         COSTUMER BILL                                         
-----------------------------------------------------------------------------------------------
 SR NO CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
   4   0024                    Apple Airpods                     40.000        1        40.000 
-----------------------------------------------------------------------------------------------
Total Price till now:  1359.8
-----------------------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 10


-----------------------------------------------------------------------------------------------
                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
 CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        2       568.000 
-----------------------------------------------------------------------------------------------
 0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        1       300.900 
-----------------------------------------------------------------------------------------------
 0024                    Apple Airpods                     40.000        1        40.000 
-----------------------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 11

Enter the year of the sales to be sorted: 2020
Enter the month of the sales to be sorted (enter 0 before 1 digit month): 09

-----------------------------------------------------------------------------------------------
                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
 CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
                                  No Sales Made This Month :(                                  
-----------------------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 11

Enter the year of the sales to be sorted: 2020
Enter the month of the sales to be sorted (enter 0 before 1 digit month): 12

-----------------------------------------------------------------------------------------------
                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
 CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        2       568.000 
-----------------------------------------------------------------------------------------------
 0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        1       300.900 
-----------------------------------------------------------------------------------------------
 0024                    Apple Airpods                     40.000        1        40.000 
-----------------------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 12

Enter the year of the sales to be sorted: 2020

-----------------------------------------------------------------------------------------------
                                    WELCOME TO APPLE STORE                                     
-----------------------------------------------------------------------------------------------
 CODE                         ITEM                         PRICE   QUANTITY SOLD  AMOUNT 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        5       400.000 
-----------------------------------------------------------------------------------------------
 0006                   Iphone X 512 GB                   300.000        2       600.000 
-----------------------------------------------------------------------------------------------
 0010               Iphone 11 Pro Max 256 GB              360.550        2       721.100 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        6       599.994 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0006                   Iphone X 512 GB                   300.000        4       1200.000
-----------------------------------------------------------------------------------------------
 0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        2       601.800 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        2       199.998 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        3       852.000 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        1        99.999 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        2       199.998 
-----------------------------------------------------------------------------------------------
 0010               Iphone 11 Pro Max 256 GB              360.550        2       721.100 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        3       852.000 
-----------------------------------------------------------------------------------------------
 0010               Iphone 11 Pro Max 256 GB              360.550        2       721.100 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0016    Macbook Pro 2020 intel core i7 8GB RAM 1TB SSD   800.900        2       1601.800
-----------------------------------------------------------------------------------------------
 0018   Macbook Pro 2019 intel core i7 8GB RAM 512GB SSD  550.900        3       1652.700
-----------------------------------------------------------------------------------------------
 0021   Macbook Air 2015 intel core i3 4GB RAM 128GB SSD  250.900        1       250.900 
-----------------------------------------------------------------------------------------------
 0006                   Iphone X 512 GB                   300.000        3       900.000 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        3       852.000 
-----------------------------------------------------------------------------------------------
 0008                      Iphone SE                      194.999        3       584.997 
-----------------------------------------------------------------------------------------------
 0010               Iphone 11 Pro Max 256 GB              360.550        2       721.100 
-----------------------------------------------------------------------------------------------
 0011         Imac intel core i7 16GB RAM 2TB SSD         899.999        2       1799.998
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        1        99.999 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        2       199.998 
-----------------------------------------------------------------------------------------------
 0002                Iphone 6s Plus 128 GB                 99.999        3       299.997 
-----------------------------------------------------------------------------------------------
 0016    Macbook Pro 2020 intel core i7 8GB RAM 1TB SSD   800.900        2       1601.800
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0004                 Iphone 7 plus 256 GB                145.500        3       436.500 
-----------------------------------------------------------------------------------------------
 0010               Iphone 11 Pro Max 256 GB              360.550        2       721.100 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0004                 Iphone 7 plus 256 GB                145.500        3       436.500 
-----------------------------------------------------------------------------------------------
 0020   Macbook Air 2019 intel core i5 8GB RAM 256GB SSD  350.900        1       350.900 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0005                 Iphone 8 plus 256 GB                160.000        4       640.000 
-----------------------------------------------------------------------------------------------
 0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        1       300.900 
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0006                   Iphone X 512 GB                   300.000        4       1200.000
-----------------------------------------------------------------------------------------------
 0001                   Iphone 6s 64 GB                    80.000        2       160.000 
-----------------------------------------------------------------------------------------------
 0009                   Iphone 11 256 GB                  284.000        2       568.000 
-----------------------------------------------------------------------------------------------
 0019   Macbook Air 2015 intel core i5 4GB RAM 128GB SSD  300.900        1       300.900 
-----------------------------------------------------------------------------------------------
 0024                    Apple Airpods                     40.000        1        40.000 
-----------------------------------------------------------------------------------------------


-----------------------------X----------------------------X--------------------
1. display items
2. add items
3. delete items
4. update items price
5. update items quantity
6. search items
7. sort by quantity
8. sort by price 
9. buy an item
10.daily sales
11.monthly sales
12.yearly sales
0. Break
-----------------------------X----------------------------X--------------------

Enter the option for the opertion of the program: 0

>>>
'''

# -----------------------------X----------------------------X--------------------
# End of the Project
# Thank you
# -----------------------------X----------------------------X--------------------
