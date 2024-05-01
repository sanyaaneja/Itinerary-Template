#import mysql.connector as sqlite3
#conn=sqlite3.connect(host="localhost",  user="root", password="empll", database="company")
import sqlite3

from datetime import date

def input_date():
    while True:
      try:
          date_components = input('Date of Import (YYYY-MM-DD:) ').split('-')

          if date_components==['']:
            break

          year, month, day = [int(item) for item in date_components]

          d = date(year, month, day)
          print(d)
          return d
          #break
      except:
        print ("Invalid date")
        return 0
def main():
    #CREATE DATABASE
    conn = sqlite3.connect('Itinerary.db')
    c=conn.cursor()
    # CREATE TABLE
    CreateCommand =( '''CREATE TABLE IF NOT EXISTS INVOICE
                          (Product_Code int PRIMARY KEY, 
                          Product_Name varchar(50),
                          GST float,
                          Price float,
                          Stock float,
                          Import_Date date);''')

    conn.execute(CreateCommand) 
    conn.commit()
    conn.close()

def search(find,ch):
  conn = sqlite3.connect('Itinerary.db')
  c = conn.cursor()

  c.execute("SELECT * FROM Invoice where Product_Code = '"+str(find)+"';")
  items = c.fetchone()
  

  
  if items != None:    #  found
      if ch == 1:
         return items
      else:
        return items[0]
  else:  # not found
      return    #None
  conn.close()

def add_record():   # USER INPUT

  while True:
    code    = input("Product Code (9999)         : ")
    if code.isnumeric() == True:
      code = int(code)
      if search(code, 0) != None:
        print("The product code already exists")
      else:   
        break
  name    = input("Product Name                : ")


  GST     = float(input("GST value(%)                : "))
  price   = float(input("Price per Kg                : "))
  stock   = float(input("Stock (kg)                  : "))

  while True:
     in_date = input_date()
     if in_date != 0:
       break
  conn = sqlite3.connect('Itinerary.db')
  c = conn.cursor()
  command = "INSERT INTO Invoice VALUES('"+str(code)+"','"+name+"',"+str(GST)+","+str(price)+","+str(stock)+",'"+str(in_date)+"')"+";"
  c.execute(command)
  conn.commit()
  conn.close()
  print('Data added successfully!')

def delete_rec():    #DELETIN87G RECORD
  conn = sqlite3.connect('Itinerary.db')    
  c = conn.cursor()  
  c.execute("SELECT * FROM Invoice")
  items = c.fetchall()

  while True:
    while True:
      Delete = input("Product Code to be deleted: ")
      if Delete.isnumeric() == True:
        Delete = int(Delete)
        break
    count = 0
    for i in range(len(items)):
      if Delete == items[i][0]:
          count+=1
          break
    if count == 0:
        print("The product code entered cannot be found")
    else:
        c.execute("DELETE FROM Invoice WHERE Product_Code = '"+str(Delete)+"' ;")
        break
  conn.commit() 
  conn.close()
  print("Record deleted successfully!")

def displayall():      
  conn = sqlite3.connect('Itinerary.db')
  c = conn.cursor()
  c.execute("SELECT * FROM Invoice")
  items = c.fetchall()
  txt ="{:^13} {:^8} {:^8} {:^10} {:^10} {:^10} "
  #txt ="{:^13} {:^13} {:^10} {:^10} {:^10} {:^10} "
  print(txt.format("Product Code", "Price", "GST", "Stock", "Date", "Name"))
  print("-"*68)
  #print("-"*75)
  for row in items:
    txt ="{:^13} {:^8} {:^8} {:^10} {:^10} {} "
    print(txt.format(row[0],row[3], row[2], row[4], row[5], row[1]))
  print("-"*68)
  conn.close()

def Mmodify(m) :
  conn = sqlite3.connect('Itinerary.db') 
  c = conn.cursor()  
  c.execute("SELECT * FROM Invoice")
  items = c.fetchall()
  while True:
    while True:
      modify = input("Product Code to be modified: ")
      if modify.isnumeric() == True:
         modify = int(modify)
         break
    count = 0
    for i in range(len(items)):
      if modify == items[i][0]:
        count+=1
        break
    if count == 0:
      print("The product code entered cannot be found")
    else:
      if m == "Import_Date":
        while True:
            new_change = input_date()
            if new_change != 0:
              break
      elif m in ("GST","Price","Stock"):
            new_change = float(input("New "+m +": "))
      else:
          new_change = input("New "+m +": ")
      Str1 = "UPDATE Invoice SET "+ m + " = '" + str(new_change) +"' WHERE Product_Code = '"+ str(modify) + "' ;"
      c.execute(Str1)
      break
  conn.commit()
  conn.close()

def invoice():
  displayall()
  print("Press enter to exit")
  conn = sqlite3.connect('Itinerary.db')
  c = conn.cursor()
  c.execute("SELECT * FROM Invoice")
  items = c.fetchall()
  Total = 0     

  while True:
      PCode = input("Product Code : ")
      count = 0
      if PCode == "":
        break
      else:
        for i in range(len(items)):
          if int(PCode) == items[i][0]:
            count+=1
            break
        if count == 0:
          print("The product code entered cannot be found")
        else:
          Qty = input("\tQuantity : ")
          Str = "SELECT * FROM Invoice where Product_Code = '" + PCode +"';"
          c.execute(Str)
          items1 = c.fetchone()
          t = items1[3] * float(Qty)
          print("\tPrice: ",t)
          total = t +  items1[2]/100 * t
          print("\t\tTotal Price:",total)
          Total += total

  print("\t\t\tGrand Total:",Total)   
      
def Search():
      ky = input ("Product Code : ")
      row = search(ky,1)
      if row != None:
        txt ="{:^13} {:^8} {:^8} {:^10} {:^10} {:^10} "
        #txt ="{:^13} {:^13} {:^10} {:^10} {:^10} {:^10} "
        print(txt.format("Product Code", "Price", "GST", "Stock", "Date", "Name"))
        print("-"*68)
        #txt ="{:^13} {:^13} {:^10} {:^10} {:^10} {:} "
        txt ="{:^13} {:^8} {:^8} {:^10} {:^10} {} "
        print(txt.format(row[0],row[3], row[2], row[4], row[5], row[1]))
        print("-"*68)
      else :
        print("The product code doesnot exists")
        print("-" * 68)

topic = str.format("{0:^68}", "ITINERARY DATABASE")
print(topic)
print("-" * 68)
print() 

while True:  
    while True:
      choice = input("""
\t\t\t0. Create New Table
\t\t\t1. Add New Record
\t\t\t2. Modify Value
\t\t\t3. Delete Record
\t\t\t4. Display Table
\t\t\t5. Print Invoice
\t\t\t6. Search Record
\t\t\t7. Exit

\t\t\tEnter a choice(0-7): """) 
      if choice not in "01234567" :          #Validity 
          print("Invalid choice!")
      else:
        break
    print()
    if choice =="" or choice == "7":
      break 
    elif choice =="0":
      main()
      print("Table created!")
    elif choice =="1":
      add_record()
    elif choice =="2":
      while True:
        CH = input("""What do you want to modify?
\t\ta. Product Name
\t\tb. GST
\t\tc. Price
\t\td. Stock
\t\te. Import Date
\t\tf. Exit   

\t\tEnter a choice(a-f): """)
        CH = CH.lower()
        if CH == "a":
          Mmodify("Product Name")
        elif CH == "b":
          Mmodify("GST")
        elif CH == "c":
          Mmodify("Price")
        elif CH == "d":
          Mmodify("Stock")  
        elif CH == "e":
          Mmodify("Import Date") 
        elif CH == "f":
          break 
        else:
          print("Invalid Choice!") 
          continue
        break

    elif choice =="3":
      delete_rec()
    elif choice =="4":
      displayall()    
    elif choice == "5":
      invoice()
    elif choice =="6":
      Search()
