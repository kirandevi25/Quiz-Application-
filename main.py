import login
import quiz
import mysql.connector
connection = mysql.connector.connect(user='root',password='kiraN@1995',host='localhost',database='project')
mycursor = connection.cursor()

def add_question():

    topic = input("Enter the topic name: ")
    question = input("Enter the question: ")
    option_a = input("Enter option a: ")
    option_b = input("Enter option b: ")
    option_c = input("Enter option c: ")
    option_d = input("Enter option d: ")
    correct_ans = input("Correct option: ")
    mycursor.execute("insert into quiz values('%s','%s','%s','%s','%s','%s','%s') ;" % (
        question, option_a, option_b, option_c, option_d, correct_ans, topic))
    connection.commit()

def print_student_marks():
    mycursor.execute("select * from topics ;")
    print('MARKS:\nName\t\tTopic\t\tMarks\t\tDate')
    for i in mycursor.fetchall():
        print(i[0], i[1], i[2], i[3], sep='\t\t')
    connection.commit()

def main():
    n = ''
    while n != 'q':
        print('Enter the choice')
        print('1:Add new user\n2:Add new Question\n3:View student Marks\nq:quit')
        n = input()
        if n == '1':
            mycursor.execute("insert into user values('%s','%s')" %
                      (input('Enter new username: '), input('Enter password: ')))
            connection.commit()

        elif n == '2':
            add_question()
            connection.commit()

        elif n == '3':
            print_student_marks()
            connection.commit()
