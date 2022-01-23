#Answer1

y='python is a case sensitive language'
print()

#part- (a)
l=len(y)
print(l)
print()

#part- (b)
print(y[::-1])
print()

#part- (c)
newstring=slice(y[10:-9])
print(newstring)
print()

#part- (d)
old="a case sensitive"
new="object oriented"
x=y.replace(old,new)
print(x)
print()

#part- (e)
print(y.index("a"))
print()

#part- (f)
newstring = ''
for i in y:
    if i !=' ':
     newstring += i

print(newstring)
print()
print()


#Answer2
#input name
x="Hey,"
y=" Here!"
name =input('Enter Name:',) 

#input sid
temp="My SID is " 
SID= input('sid:',)

#input departement and cgpa
temp1="I am from "
XYZ= input('department name:',)
temp2=" department and my cgpa is "
CGPA= input('enter  CGPA:',)


print()
print()

#result
print(x+name +y)
print(temp+SID)
print(temp1+XYZ+temp2+CGPA)


print()
print()


#Answer 4
#enter the numbers for comparison
n1=int(input("enter the 1st number:"))
n2=int(input("enter the 2nd number:"))
n3=int(input("enter the 3rd number:"))
if(n1>n2):
    if(n1>n3):
        print("n1 is the greatest")
    else:
        print("n3 is the greatest")
elif(n2>n3):
    if(n2>n1):
        print("n2 is the greatest")
    else:
        print("n1 is the greatest")
elif(n3>n1):
    if(n3>n2):
        print("n3 is the greatest")
    else:
        print("n2 is the greatest")
        
print()
print()

#Answer6
#input length of sides of triangle
l1=int(input("length of 1st side :"))
l2=int(input("length of 2nd side :"))
l3=int(input("length of 3rd side :"))
if(l1<l2+l3):
    print("yes,triangle can be formed")
else:
    print("no,triangle can not be formed")    
if(l2<l1+l3):
    print("yes,triangle can be formed")
else:
    print("no,triangle can not be formed")
if(l3<l1+l2):
    print("yes,triangle can be formed")
else:
    print("no,triangle can not be formed")

print()
print()


#Answer 5

s = input('something:')

for name in s:
    print("yes")
else:
    print("no")
        
            
 



























