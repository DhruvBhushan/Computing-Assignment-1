print("part a")
class Employee:
        count=0
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary
            Employee.count+=1
        def displayCount(self):
            print("There are %d employees" % Employee.count)
        def displayDetails(self):
            print("Name:", self.name,  ", Salary:", self.salary)
e1=Employee("mehak",  40000)
e2=Employee("ashok",  50000)
e3=Employee("viren",  60000)
e3.displayCount()
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()

print()
print()

print("part b")
class Employee:
        count=0
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary
            Employee.count+=1
        def displayCount(self):
            print("There are %d employees" % Employee.count)
        def displayDetails(self):
            print("Name:", self.name,  ", Salary:", self.salary)
e1=Employee("mehak",  40000)
e2=Employee("ashok",  50000)
e2.displayCount()
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()







num = int(input("Enter the number: "))  
list1 = [] #an empty list  
for i in range(num):  
  list1.append([])  
  list1[i].append(1)  
  for j in range(1, i):  
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
  if(num != 0):  
    list1[i].append(1)  
for i in range(num):  
  print(" " * (num - i), end = " ", sep = " ")  
  for j in range(0, i + 1):  
    print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")  
  print()  












# Creating a recursive function  
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter the number of disks: '))  
# We are referring source as A, auxiliary as B, and target as C  
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function  








#QUESTION 6
print("ANSWER 6")
#inputting the word from the first friend
word =input("Enter the word: ")
word=word.lower()

#inputting the meaningful word with the exact same letters
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()
#defining the dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#shopkeeper input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
