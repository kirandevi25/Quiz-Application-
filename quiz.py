from datetime import datetime
import mysql.connector
connection = mysql.connector.connect(user='root',password='kiraN@1995',host='localhost',database='project')
mycursor = connection.cursor()

def run_quiz(name):
    marks = 0
    mycursor.execute("select distinct(topic) from quiz;")
    print('These are the Available topics, choose any one : ')
    for i in mycursor.fetchall():
        print(i[0], end='\t')
    print()
    topic = input("Enter the name of the topic: ")
    mycursor.execute("select * from quiz where topic='%s' ;" % (topic))
    temp = mycursor.fetchall()
    connection.commit()

    if len(temp)==0:
        print('Selected topic is not available')
    else:

        for i in temp:
            print(i[0])
            print('a:', i[1], '\tb:', i[2], '\tc:', i[3], '\td:', i[4])
            ans = input("answer: ")
            if ans == i[5]:
                marks += 1

        mycursor.execute("insert into topics values ('%s','%s','%d','%s');" %
                  (name, topic, marks, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        connection.commit()
        print("You obtained %d marks" % marks)

def main():
    name = input('Enter your name: ')
    run_quiz(name)