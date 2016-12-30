# An algorithm to determine if the given string contains any unique characters or not

def unique():
	print "The String you entered have all unique characters!"

def not_unique():
	print "The String you entered does not have all unique characters!"

print "Enter a String :\n"

input = raw_input("> ")

arr = [False] * 256
temp = True 

if len(input) > 256:
	not_unique()
else:
	for i in range(0, len(input)):
		x = ord(input[i]) # ord() converts char value in int
		if arr[x] == False:
			arr[x] = True

		elif arr[x] == True:
			not_unique()
			temp = False 
			break

if temp == True:
	unique()