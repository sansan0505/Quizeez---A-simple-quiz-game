import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='admin',data
base='quiz')
c=db.cursor()
#home page
def home():
f=1
while f!=2:
print("*****************")
print("WELCOME TO QUIZEEZ")
print("*****************")
print("1.TAKE QUIZ")
print("2.ADMIN")
print("3.EXIT")
f=int(input('Enter your choice:'))
if f==1:
new_player()
print('\nTIME FOR SOME QUIZZZ!!!!\n')
level1()
elif f==2:
admin_code=int(input('Enter code'))
if admin_code==2023:

add()
else:
print('You are not supposed to be here! RETURN!\n')
home()
elif f==3:
print("EXITING THE QUIZ")
break
else:
print("INVALID ENTRY")

#new player
def new_player():
sql="insert into points(name) values(%s);"
name=input("Enter your name: ")
data=(name,)
c.execute(sql,data);
print("\nNEW PLAYER ADDED")
print('Welcome',name.upper())

#add questions
def add():
print('\n')

question1=input("Enter the question")
optionA=input("Enter the optiona")
optionb=input("Enter option b")
optionc=input("Enter optionc")
optiond=input("Enter optiond")
correctoption=input("Enter correct option")
levels=int(input("enter levels"))
if levels==1:
q="select max(sr_no) from questions"
c.execute(q)
sl=c.fetchone()
sl=sl[0]+1
qry="insert into questions
values({},'{}','{}','{}','{}','{}','{}',{});".format(sl,question1,optiona,optionb,optionc,opt
iond,correctoption,levels)
elif levels==2:
q="select max(sr_no) from questions2"
c.execute(q)
sl=c.fetchone()
sl=sl[0]+1
qry="insert into questions2
values({},'{}','{}','{}','{}','{}','{}',{});".format(sl,question1,optiona,optionb,optionc,opt
iond,correctoption,levels)

elif levels==3:
q="select max(sr_no) from questions3"
c.execute(q)
sl=c.fetchone()
sl=sl[0]+1
qry="insert into questions3
values({},'{}','{}','{}','{}','{}','{}',{});".format(sl,question1,optiona,optionb,optionc,opt
iond,correctoption,levels)

c.execute(qry)
c.connect()
print("Success")
#calling question
def level1():
print(' LEVEL 1 \n')
point=0
qry="select * from questions where levels=1"
c.execute(qry)
qs=c.fetchall()
for i in qs:
print(i[1],"\n")

print(i[2],"\t\t\t",i[3],'\n')
print(i[4],"\t\t",i[5],'\n')
ans=input('Type your answer: ')
x=i[6]
if ans==x.lower():
point=point+1
print('YOUR ANSWER IS CORRECT!! KEEP GOIN :)')
print("Points scored:",point,'\nRequired points: 4')
else:
print(" sike!! THats the wrong answer <3\n \n THE CORRECT
ANSWER IS :",x )
print("\t\t\t\t\t\t\t\t",point)
input('Enter any key to continue')
for j in range(2):
print()

if point==4:
level2(point)
else:
print("You haven't attained the required points to reach the next level.
Try this level Again")
level1()

def level2(point):
print(' LEVEL 2 \n')
print('You have reached level 2!')
qry="select * from questions2 where levels=2"
c.execute(qry)
qs1=c.fetchall()
for i in qs1:
print(i[1],"\n")
print(i[2],"\t\t\t",i[3],'\n')
print(i[4],"\t\t",i[5],'\n')
ans=input('Type your answer: ')
x=i[6]
if ans==x.lower():
point=point+1
print('YOUR ANSWER IS CORRECT!! KEEP GOIN :)')
print("Points scored:",point,'\nRequired points: 9')
else:
x=i[6]
print(" sike!! THats the wrong answer <3\n \n THE CORRECT
ANSWER IS :",x )
print("\t\t\t\t\t\t\t\t",point)

input('Enter any key to continue')
for j in range(2):
print()
if point>=9:
level3(point)
else:
print("You haven't attained the required points to reach the next level.
Try this level Again")
level2(point)

def level3(point):
print(' LEVEL 3 \n')
print('You have reached level 3!')
qry="select * from questions3 where levels=3"
c.execute(qry)
qs=c.fetchall()
for i in qs:
print(i[1],"\n")
print(i[2],"\t\t\t",i[3],'\n')
print(i[4],"\t\t",i[5],'\n')
ans=input('Type your answer: ')
x=i[6]

if ans==x.lower():
point=point+1
print('YOUR ANSWER IS CORRECT!! KEEP GOIN :)')
print("Points scored:",point,'\nRequired points: 12')
else:

print(" sike!! THats the wrong answer <3\n \n THE CORRECT
ANSWER IS :",x )
print("\t\t\t\t\t\t\t\t",point)
input('Enter any key to continue')
for j in range(2):
print()
if point==12:
print('CONGRATS! You have completed the quiz <3')
else:
print("You haven't attained the required points to complete the quiz.
Try this level Again")
level3(point)
home()
