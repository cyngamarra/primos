import sys	
i=2
j=1
a=int(sys.argv[1])
while i<a and j==1:
 if a%i==0:j=0
 i+=1
print j