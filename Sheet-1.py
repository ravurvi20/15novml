#Q2
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a= 20; a+=30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
#print(False in 'False')
print(((True==False) or (False > True)) and (False<=True))

#Q3
s1= 'Nice to have it'
s2= 'here'
print(s1+ ' ' + s2)

#Q4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#Q5
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
s1= 'Nice to have it'
s2= 'here'
a[0]=s1
a[5]=s2
print(a)

#Q6
numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
for i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)
#Q7
colour_list_1=set(["White", "Black" , "Red"])
colour_list_2=set(["Red", "Green"])
print(set((colour_list_1)- (colour_list_2)))


#Q8
a=input('Enter string')
string=set(string)
alpha=list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string:
    if(word in alpha):
        i+=1
    if(i==26):
        print('string is panagram')
    else:
        print('string is not panagram')


#Q9
n=int(input("Enter value"))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
print(n+int(t1)+ int(t2))


#Q11
a= input('enter the string')
print(a, sep=',')
a.sort()
print(a)


#Q12
d={'Student': ['Rahul', 'Kishor', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
marks_list=d.get('Marks')
student_list=d.get('Student')
num= marks_list.index(max(marks_list))
print(student_list[num])


#Q13
s=input('enter string')
d=l=0
for c in s:
    if c.isdigit():
        d+=1
    elif c.isalpha():
        l+=1
else:
    pass
print('digit',d)
print('letters',l)



