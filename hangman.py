from builtins import input 
import time

#welcoming the user
name = input("What is your name? ")

print("Hello, " + name + "  time to play hangman!")

print ("")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set the secret
word = "dinner"
second_word = "code"

#creates a variable with an empty value
guesses = ' '

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:
	# make a counter that starts with zero
	failed = 0
	
	# for every character in secret_word
	for char in (word, second_word):
		#see if the caracter is in the players guesses
		if char in guesses:
			#print then out the characte
			print(char)
		else:
			# if not found, print a dash
			print("_")
			# and increase the failed counter with one
			failed += 1
	#if failed is qual to zero
	# print You Won
	if failed == 0:
		print ("You win!")
		#exit the loop, effectively ending the script
		break
		
	print("")
	
	#ask the user go guess a character
	guess = input ("guess a character:")
	
	# set the playerz guess to guesses
	guesses += guess
	
	#if guess is not found in the secret word
	if guess not in (word):
		#turns counter descreases with 1 (now 9)
		turns -= 1
		print("Wrong")
		
		#how many turns are left
		print("You have", +turns, "more guesses")
		
		if turns == 0:
			#print "You Lose"
			print("You Lose")
			
while turns > 0:
	# make a counter that starts with zero
	failed = 0
	
	# for every character in secret_word
	for char in (second_word):
		#see if the caracter is in the players guesses
		if char in guesses:
			#print then out the characte
			print(char)
		else:
			# if not found, print a dash
			print("_")
			# and increase the failed counter with one
			failed += 1
	#if failed is qual to zero
	# print You Won
	if failed == 0:
		print ("You Win")
		#exit the loop, effectively ending the script
		break
		
	print("")
	
	#ask the user go guess a character
	guess = input ("guess a character:")
	
	# set the playerz guess to guesses
	guesses += guess
	
	#if guess is not found in the secret word
	if guess not in (second_word):
		#turns counter descreases with 1 (now 9)
		turns -= 1
		print("Wrong")
		
		#how many turns are left
		print("You have", +turns, "more guesses")
		
		if turns == 0:
			#print "You Lose"
			print("You Lose")
		
		
	
	