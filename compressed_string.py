""" Implement a method to perform basic string compression using the counts of repeated characters 
		For example, the string 'aabcccccaaa' would be a2b1c5a3. If the 'compressed' string would not 
		become smaller that the original string, your method should return the original string.
"""
original = True 
result = [""]
arr = [0] * 256

myInput = raw_input("> ") # has to enter input with spaces
myInput = myInput.split()

for i in range(0, len(myInput)):
	x = ord(myInput[i])
	arr[x] = arr[x] + 1

for i in range(0, 256):
	if arr[i] == 0:
		continue
	else:
		num = arr[i]
		element = chr(i)
		result.append(element)
		result.append(num)

		if num != 1:
			original = False 

if original == True:
	print "%s" % myInput
else:
	print "%s" % result 