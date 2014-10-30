class Animal:
  
	def __init__(self, name):
		self.name = name
		if name=="elephant":
                        self.info=['I am the largest land-living mammal in the world','I am haviest animal can walk','I am kind so I like people']
		if name=="tiger":
                        self.info=['I am the biggest cat','I am the prince of land ','I am eating meat only']
		
		if name=="bat":
                        self.info=['I use echo-location','I can fly','I see well in dark']

	def guess_who_am_i(self):
		hintn=0
		print("I will give you 3 hints, guess what animal I am")
		print("I have exceptional memory")
		Q=input("Who am I?")
		if Q == self.name:
                        print("You got it! I am",self.name)
		while ( Q != self.name and hintn!=3 ) :
			print(self.info[hintn])
			hintn=hintn + 1
			Q=input("Who am I?")
			if Q != self.name and hintn < 3 :
				
				print("Nope, try again!")
			elif Q != self.name and hintn==3 :
				print("I'm out of hints! The answer is",self.name)
				break
			elif Q == self.name:
				print("You got it! I am",self.name)
				break
			
            
                
        
                                
                                
                        
		

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
