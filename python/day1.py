# Day 1
import sys

#print(sys.argv)
a = int(sys.argv[1])
b = int(sys.argv[2])

print(f'value of a,b ={a},{b}')
print(a,'-',b,'=',a-b)
print(a,'+',b,'=',a+b)
print(a,'*',b,'=',a*b)
print(a,'**',b,'=',a**b)
if(b!=0):   
    print(a,'/',b,'=',round(float(a/b),2))
else:
    print(a,'/',b,'=','Inf')
