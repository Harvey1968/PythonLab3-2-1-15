# 3.2.1.15 LAB: Collatz's hypothesis
#
# Prompts user for a number (integer)
# Tranlation "Good day, you wish to play a game, yes?"
print('"Guten Tag, Sie mochten ein Spiel spielen, ja?"')
# Tranlation "Please enter a number:"
c0 = int(input('Bitte geben Sie eine Zahl ein: '))

if c0 > 0:
	steps = 0
	# Will loop until c0 = 1
	while c0 != 1:
		if (c0 %2) != 0:
			# If integer is odd evaluate a new c0 as (3 × c0) + 1;
			c0 = (3 * c0) + 1
		else:
			# Even numbers are divided in half until they become an odd number;
			c0 = (c0 // 2)   
		print(c0)
		steps += 1
	# Outputs how many steps the calculation has taken to complete
	# Tranlation "This calculation has taken 'steps' steps to complete"
	print('"Diese Berechnung hat', steps, 'Schritte in Anspruch genommen"\n')
else:
	# If the user types an non-negative and non-zero integer number the following error message is displayed:
	# Tranlation "no, bad number"
	print('"Nein, schlechte Nummer"\n')
	 
