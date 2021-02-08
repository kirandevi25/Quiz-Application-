import main
import quiz
import mysql.connector
from getpass import getpass
connection = mysql.connector.connect(user='root',password='kiraN@1995',host='localhost',database='project')
mycursor = connection.cursor()

n = input('Enter the choice(a/b):\n a->User\n b->student\n')
if n == 'a':
    while True:
        user = input(' Please Enter the username: ')
        password = input('Please Enter the password: ')

        mycursor.execute("select * from user where username = '%s' ;" % user)
        temp = mycursor.fetchall()

        if not temp:
            mycursor.execute("insert into user values ('%s','%s') ;" % (user,password ))
            connection.commit()
            mycursor.execute("select * from user where username = '%s' ;" % user)
            temp = mycursor.fetchall()
            temp = list(temp)

        if temp is None:
            print('username is not correct')

        elif temp[0][1] == password:
            main.main()
            break
        else:
            print('You have entered the Wrong password')
    connection.commit()
else:
    connection.commit()
    print('For Students'.center(32, '*'))
    quiz.main()