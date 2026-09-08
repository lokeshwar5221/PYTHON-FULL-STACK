
#Task 1 Student Marks Manager 
marks=[]
for mark in range(3):
    mark=int(input("enter marks:"))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
marks.pop()
print(f'marks in the list are{marks}')
print(f'count of marks in the list:{len(marks)}')


#Task 2 Number List Analysis
numbers=[20,10,30,20,40,20]
numbers.sort()
numbers.reverse()
search=int(input("enter number to be searched:"))
if search in numbers:
           print(numbers.count(search))
           print(numbers.index(search))
print(f'min of numbers:{min(numbers)}')
print(f'max of numbers:{max(numbers)}')
print(f'sum of numbers:{sum(numbers)}')


