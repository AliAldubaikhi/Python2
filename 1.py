

name=input("What is your Name? ")

print("Hello " + name + "Let's play a game!")

print("Think of random number from 1 to 100, and I'll try to guess it!")



play = True
guess = False
tries = 1

while(play == True):
    min_ = 0
    mid = 50
    max_ =  100
    
    while (guess == False): 
        equal = input("Is it %d? (yes/no)" %mid)
        if (equal == "yes"):
            print("Got it")
            print("I got it in"+str(tries)+"tries")
            break
        elif(equal == "no"):
            tries= tries+1
            greater=input("is it greter than %d?(yes/no)"%mid)
            if(greater == "yes"):
                min_ = mid+1
                
            elif (greater == "no"):
                max_ = mid - 1 
            
            mid = ((min_ + max_)/2)  
        
        
    more = input("Do you want to play more? ")
    if(more == "yes"):
        play = True
    elif (more == "no"):
        play = False
        
        print("Bye Bye")
