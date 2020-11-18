import mysql.connector

db = mysql.connector.connect(host="localhost", user="tim", password="@sim0v73", database="lotto")
cursor = db.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#open csv file
history_file = open("winnums3.csv")
new_history_file = open("new_winnums3.csv", "w")
line_count = 0
new_history_file.writelines("DrawDate, W1, W2, W3, W4, W5, PB, Multiplier")
for x in history_file.readlines():
    line_count += 1
    if line_count == 1:
        continue
    data = x.split(",")
    print (data)
    drawdate = data[0]
    print (drawdate)
    date_split = drawdate.split("/")
    print (date_split)
    drawdate = date_split[2] + "-" + date_split[0] + "-" + date_split[1]
    print (drawdate)
    wb1 = data[1]
    wb2 = data[2]
    wb3 = data[3]
    wb4 = data[4]
    wb5 = data[5]
    pb = data[6]
    sqlstring = drawdate+", "+wb1+", "+wb2+", "+wb3+", "+wb4+", "+wb5+", "+pb+"\n"
    new_history_file.writelines(sqlstring)