print('Checking FizzBuzz for if else conditional use case')

for i in range(1, 100):
	if(i % 5 == 0 and i % 3 == 0):
		print ("FizzBuzz")
	if(i % 5 == 0):
		print ("Fizz")
	elif(i % 3 == 0):
		print ("Buzz")
	else:
		print ("Exceptional Number => " + str(i))
	
	