def fizz(s):
    if (s%3 and s%5==0):
        print("Buzz")
    elif (s%5 and s%3==0):
        print("Fizz")
    elif(s%15==0):
        print("FizzBuzz")
    else : print(s)
        
 
a=input() 
b=input()
c=input()

if(c.isdigit()):
    fizz((int(c))+1)
elif (b.isdigit()):
    fizz((int(b))+2) 
else:fizz((int(a))+3) 
    
    