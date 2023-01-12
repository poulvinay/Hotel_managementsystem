#Hotel Pahunchar
from tkinter import *
Font1=("Times",40)
Font2=("calibri",27)


print("Welcome to HOTEL PAHUNCHAR")
print('1.Vada Pav =10\n2.Misala Pav =30\n3.Pav Baji =30\n4.Poha =20\n5.Puri Baji =25\n6.Done')
e=True
list=[]
while e==True:
    x=input("Enter want your want:-")

    if x=='1' or x=='Vada Pav':
        x="Vada_Pav"
        q=int(10)
        list.append(x)
    elif x=='2' or x=='Misala Pav':
        x="Misala_Pav"
        q=int(30)
        list.append(x)
    elif x=='3' or x=='Pav Baji':
        x="Pav_Baji"
        q=int(30)
        list.append(x)
    elif x=='4' or x=='Poha':
        x="Poha"
        q=int(20)
        list.append(x)
    elif x=='5' or x=='Puri Baji':
        x="Puri_Baji"
        q=int(25)
        list.append(x)
    elif x=='6' or x=='Nothing':
        x= "Nothing"
        e=False
    else:
        print('invalid input')
        
        x="Nothing"
        q=int(0)

print(list)
mylist = []
list10 =[]
for i in list:
    if i not in mylist:
        mylist.append(i)
        list10.append(i)
print(mylist)
list1=[]
if list==[]:
    print()
    a=int(0)
else:
    list1=[]
    for i in mylist:
        
        a=int(input("Plate/s of "+i+" required:-")) 
        list1.append(a)
list2=[]
for n,i in enumerate(mylist):
    if i =="Vada_Pav":
        mylist[n]=int(10)
    elif i =="Misala_Pav":
        mylist[n]=int(30)
    elif i=="Pav_Baji":
        mylist[n]=int(30)
    elif i=="Poha":
        mylist[n]=int(20)
    elif i=="Puri_Baji":
        mylist[n]=int(25)
        


products = []

for num1, num2 in zip(mylist, list1):
	products.append(num1 * num2)
	

print(products)
u=sum(products)
print(u)
#DRINKS
print("1.Pepsi\n2.Slice\n3.Fruti\n4.Fizz\n5.Mountain Duo\n6.Done")
t=True
while t==True:
    y=input("Enter want you want:-")
    if y=='1' or y=='Pepsi':
        y="Pepsi"
        list2.append(y)
    elif y=='2' or y=='Slice':
        y="Slice"
        list2.append(y)
    elif y=='3' or y=='Fruti':
        y='Fruti'
        list2.append(y)
    elif y=='4' or y=='Fizz':
        y='Fizz'
        list2.append(y)
    elif y=='5' or y=='Mountain Duo':
        y='Mountain_Duo'
        list2.append(y)
    elif y=='6' or y=='Nothing':
        t=False
    else:
        print('invalid input')
        y='Nothing'
print(list2)
mylist2 = []
for i in list2:
    if i not in mylist2:
        mylist2.append(i)
print(mylist2)
list01=[]
list02=[]
list03=[]
if mylist2==[]:
    print()
    z=int(0)
    b=int(0)

else:
    list01=[]
    list02=[]
    list03=[]
    for i in mylist2:
        
        print("You want your "+i+" of")
        print("1. 10\n2. 20\n3. 40\n4.100")
        z=int(input("Enter:-"))
        if z==1:
            z=int(10)
        elif z==2:
            z=int(20)
        elif z==3:
            z=int(40)
        elif z==4:
            z=int(100)
        else:
            print("invalid entry")
            z=int(0)
        b=int(input("Quantity of "+i+" required:-"))
        list02.append(z)
        list03.append(b)
        list01.append(z*b)

#Chai

print("Food")
m, n = "", ""
for num1, num2 ,num3 ,num4 in zip(mylist, list10,list1,products):
	m= num2,num1,"X" , num3,"=",num4
	print(m)

print(products)
u=sum(products)
print(u)

print("Drink")

for num1, num2 ,num3 ,num4 in zip(mylist2,list01,list02,list03):
	n= num1,num4,"X" , num3,"=",num2
	print(n)
	
print(list01)
v=sum(list01)
print(v)
o='Your_Bill_is' ,u+v
print(o)
root = Tk()
root.title("Bill")
#bg=PhotoImage(file="")
#Label(root, image=bg).place(x=0,y=0)
Label(root,text="Hotel Pahunchar",font=Font1).pack()        
Label(root,text="Food").pack()
Label(root,text=m).pack()
Label(root,text="Drink").pack()
Label(root,text=n).pack()
Label(root,text=o,font=Font2).pack()
a = input()
