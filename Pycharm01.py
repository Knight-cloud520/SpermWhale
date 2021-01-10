# Author: Knight

name = input("name:")
age = int(input("age:"))
print(type(age), type(str(age)))
job = input("job:")
salary = input("salary:")

#info = '''
#--------------- info of '''+ name +''' ----------------
#name: '''+ name +'''
#age:  '''+ age +'''
#job:  '''+ job +'''
#salary: '''+ salary
#print(info)  #不用字符串拼接

info1 = '''
--------------- info1 of %s ----------------
name: %s
age:  %d
job:  %s
salary: %s
''' % (name, name, age, job, salary)
print(info1)

info2 = '''
--------------- info2 of {_name} ----------------
name: {_name}
age:  {_age}
job:  {_job}
salary: {_salary}
''' .format(_name = name, _age = age, _job = job, _salary = salary)
print(info2)

info3 = '''
--------------- info3 of {0} ----------------
name: {0}
age:  {1}
job:  {2}
salary: {3}
''' .format(name, age, job, salary)
print(info3)


'''
#import getpass  #Pycharm不能用

_username = 'knight'
_password = '123'

username = input("username:")
password = input("password:")

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name = username))
else:
    print("Invalid username or password!")

print(username, password)
'''

'''
for i in range(0, 10):
    if i < 3:
        print("loop", i)
    else:
        continue
    print("hehe...")
'''

'''
age_of_oldboy = 56

count = 0

#for i in range(3):
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess_age < age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
    if count == 3:
        countinue_confirm = input("do you want to keep guessing..?")
        if countinue_confirm != 'n':
            count = 0

else:
    print("you have tried too many times..fuck off")
'''