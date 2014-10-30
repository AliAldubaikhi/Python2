from random import randrange
t=0
Qn=input("How many problem you want to solve?")
print("INTEGER DIVISIONS")

while t != int(Qn):
        a = randrange(5) 
        b = randrange(12)
        if b%2 !=0 and b!=0:
                b=b+1
        
                try:
                        Q=int(input('%d / %s ='%(b,a)))
                        if int(Q) == (b//a):
                                print("CORRECT!")
                                t=t+1
                        else:
                                print("INCORRECT!")
                                t=t+1
                except ValueError:
                        print("Please enter Integers Only!")
                        t=t+1
                except ZeroDivisionError:
                        print("Can not do this operation because divided by Zero")
                        t=t+1
                        
if t == int(Qn):
        print("That was last problem :) see you")
                
                
                
                
        
        
                
        

