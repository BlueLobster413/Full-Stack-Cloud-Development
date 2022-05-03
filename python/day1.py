# Day 1
import sys

#print(sys.argv)
a = int(input())
b = int(input())
c = int(input())

print(f'value of a,b,c ={a},{b},{c}')
print(a,'-',b,'=',a-b-c)
print(a,'+',b,'=',a+b+c)
print(a,'*',b,'=',a*b*c)
print(a,'**',b,'=',(a**b)**c)
if(b!=0):   
    print(a,'/',b,'=',round(float(a/b),2))
else:
    print(a,'/',b,'=','Inf')

