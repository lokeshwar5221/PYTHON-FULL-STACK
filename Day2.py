'''
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


'''
#BMI calculator
number_of_bmi_count=int(input("enter number of bmi calculation count:"))
details={}
for i in range(number_of_bmi_count):
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the height in meters:"))
    name=input("enter your name:")
    details.update({'weight':weight,'height':height,'name':name})
    if weight>0 and height>0:
        bmi=(weight)/((height)**2)
        details.update({'bmi':bmi})
        print(f'bmi is:{bmi}')
        if bmi<18.5:
            print("under weight")
        elif bmi>=18.5 and bmi<=24.9:
            print("normal weight")
        elif bmi>=25 and bmi<=29.9:
            print("over weight")
        else:
            print("obesity")
        print(f'the details of the person was:{details}')
    else:
        print("plese enter only positive values grater than 0")
#Task -->store the result of name,weight,height-->Bmi in to a calculator
'''

#repetation -->while
while True:
    try:
        weight=float(input("enter the weight in kgs:"))
        height=float(input("enter the height in meters:"))
        if weight>0 and height>0:
            bmi=(weight)/((height)**2)
            print(f'bmi is:{bmi}')
            if bmi<18.5:
                print("under weight")
            elif bmi>=18.5 and bmi<=24.9:
                print("normal weight")
            elif bmi>=25 and bmi<=29.9:
                print("over weight")
            else:
                print("obesity")
            break
    except Exception as e:
        print(e)
'''
