import math
#Hipoteza: dla zdefiniowanej funkcji z= liczba zer na końcu liczby (2n nad n) można wyrazić wzorem tym
def z(value):
    z=0
    v=math.factorial(value)
    x=str(v)
    for i in range(1,len(x)):
        if x[-i]=='0':
            z+=1
        else:
            break
    return int(z)

#print(math.factorial(45))
n=1
t=1
while z(2*n)-2*z(n)<t:
    n+=1
print('n-',n)

print(((5**10)+1)/2)
