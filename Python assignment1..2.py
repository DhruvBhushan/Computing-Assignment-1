#Answer  1 (pyhton program to find average of three numbers)
print('Answer 1')
# take inputs
a=int(input('enter first number: '))
b=int(input('enter secont number: '))
c=int(input('enter third number: '))
print()
# calculate average
result = (a + b + c)/3

# display result
print('The average of numbers : ',result)

print()
print()


#Answer 2
print('Answer 2')
#eneter your details
income=int(input('Enter your gross income: '))
dep=int(input('Enter number of dependents: '))
#output
Y= income-10000-(dep*3000)
#result
print('your annual tax : ',Y*0.2)

print()
print()


#Answer  3
print('Answer 3')
#input details
SID=int(input('Enter your sid: '))
Name=input('eneter your full name: ')
Gender=input('Enter your gender: ')
Course=input('Enter your course name: ')
CGPA=input('Enter your CGPA: ')

print()

#Student details
Student=[SID,Name,Gender,Course,CGPA]
print(Student)


print()
print()


#Answer 4
print('Answer 4')
#input marks
M1=int(input('Enter marks of first student:'))
M2=int(input('Enter marks of second student: '))
M3=int(input('Enter marks of third student: '))
M4=int(input('Enter marks of fourth student: '))
M5=int(input('Enter marks of fifth student: '))

#marks obtained by different student
Marks=[M1,M2,M3,M4,M5]
Marks.sort()
print(Marks)

print()
print()

#Answer 5
print('answer 5')
#input
color=['Red','Green','White','Pink','Black','yellow']
print(color)

print()

#part 1
del color[3]
print('After deletiong 4th term, new list is:',color)

print()

#part 2
color=['Red','Green','White','Pink','Black','Yellow']
color[3]=color[4]='purple'
print('Answer for part B: ', color[0:4]+color[5:1])

