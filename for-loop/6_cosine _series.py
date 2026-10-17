# cosine serise

x=float(input("Enter a value of x in a radians: "))
n=int(input("Enter a number of terms: "))

cos_x=0

for i in range(n):
    fact=1
    for j in range(1,2*i+1):
        fact=fact*j
    term = ((-1)**i)*(x**(2*i))/fact
    cos_x=cos_x+term

print("Cosine value=",cos_x)



    
