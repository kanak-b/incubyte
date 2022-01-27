import mysql.connector 
import pandas as pd;

# Make the connection with MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hospital"
)

# Create a cursor object
cur = mydb.cursor()

# Create a dataframe from the text file i.e. info from the Patient data
df = pd.read_csv("data/data.txt",delimiter="|")

#Segmenting the Patient table into multiple tables country wise
for i, row in df.iterrows():
  
    country = row.Country
    details = (row.Customer_Name,str(row.Customer_Id),row.Open_Date,row.Last_Consulted_Date,row.Vaccination_Id,row.Dr_Name,row.State,row.Country,row.DOB,row.Is_Active)
    
    try :
        if country in df['Country'] :
            
            cur.execute("INSERT INTO "+ country +"(Customer_Name,Customer_ID,Open_Date,Last_Consulted_Date,Vaccination_Id,Dr_Name,State,Country,DOB,Is_Active) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , details)
            
        else :
        
            cur.execute("CREATE TABLE "+ country +" (Customer_Name varchar(255) NOT NULL Primary key,Customer_ID varchar(18) NOT NULL,Open_Date DATE NOT NULL,Last_Consulted_Date DATE,Vaccination_Id char(5),Dr_Name char(255),State char(5),Country char(5),DOB DATE,Is_Active char(1));")
            cur.execute("INSERT INTO "+country +"(Customer_Name,Customer_ID,Open_Date,Last_Consulted_Date,Vaccination_Id,Dr_Name,State,Country,DOB,Is_Active) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , details)
            
    except:
        
        print("Already exists.")

mydb.commit()
mydb.close()
