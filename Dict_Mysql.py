import mysql.connector
# pip install mysql-connector-python
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122", #IP of the server that has database
database = "ardit700_pm1database"
)

cursor = con.cursor() #to navigate through db table

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word) #query to seach a specific word
results = cursor.fetchall() # to search it in a table

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")