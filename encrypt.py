import sys
import re

string = sys.argv[1]

length = len(string)

if length > 5:
	print (string + " is more than 5 characters long.")

elif length < 5:
	print (string + " is less than 5 characters long.")

else:
	print (string + " is exactly 5 characters long.")

print "\n"

encrypted_string = str()
for char in range(0, length):
	letter = string[char].lower()
	
	if letter == 'a':
		newletter = letter.replace(letter, '01100001')
		print letter + " > "  + newletter
		encrypted_string += newletter + " "
	if letter == 'b':
		newletter = letter.replace(letter, '01100010')
		print letter + " > "  + newletter
		encrypted_string += newletter + " "

	if letter == 'c':
		newletter = letter.replace(letter, '01100011')
		print letter + " > "  + newletter
		encrypted_string += newletter + " "
	
	if letter == 'd':
                newletter = letter.replace(letter, '01100100')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "

	if letter == 'e':
                newletter = letter.replace(letter, '01100101')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "

	if letter == 'f':
                newletter = letter.replace(letter, '01100110')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'g':
                newletter = letter.replace(letter, '01100111')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	
	if letter == 'h':
                newletter = letter.replace(letter, '01101000')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	
	if letter == 'i':
                newletter = letter.replace(letter, '01101001')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "

	if letter == 'j':
                newletter = letter.replace(letter, '01101010')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'k':
                newletter = letter.replace(letter, '01101011')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'l':
                newletter = letter.replace(letter, '01101100')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'm':
                newletter = letter.replace(letter, '01101101')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'n':
                newletter = letter.replace(letter, '01101110')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'o':
                newletter = letter.replace(letter, '01101111')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'p':
                newletter = letter.replace(letter, '01110000')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'q':
                newletter = letter.replace(letter, '01110001')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'r':
                newletter = letter.replace(letter, '01110010')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 's':
                newletter = letter.replace(letter, '01110011')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 't':
                newletter = letter.replace(letter, '01110100')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'u':
                newletter = letter.replace(letter, '01110101')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'v':
                newletter = letter.replace(letter, '01110110')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'w':
                newletter = letter.replace(letter, '01110111')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'x':
                newletter = letter.replace(letter, '01111000')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'y':
                newletter = letter.replace(letter, '01111001')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "
	if letter == 'z':
                newletter = letter.replace(letter, '01111010')
                print letter + " > "  + newletter
                encrypted_string += newletter + " "


	elif letter == 'z':
		newletter = letter.replace(letter, 'AD')
		print letter + " > "  + newletter
		encrypted_string += newletter

	else:
		continue
print "\n" + string  + " > " + encrypted_string
