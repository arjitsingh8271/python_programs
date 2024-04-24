'''
019
Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
'''

a = input("Enter a number 1,2 or 3: ")
if (a=="1"):
	print("Thank you")
elif (a=="2"):
	print("Well done")
elif (a=="3"):
	print("Correct")
else:
	print("Error message")