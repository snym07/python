'''
A python program for practicing list methods and functions:
	append()
	remove()
	split()
	count()
	join()
	index()
	copy()
	reverse()
	sort()
'''
def main():
	print('Enter something!')
	user_input = str(input()).split()

	text = '''
What do you want to do with your input :
1. show my input in string format
2. show my input in list format
3. append "to infinity and beyond" in the end
4. remove the given index item from the list
5. counts the given word in the list
0. exit the program

Press the corresponding number : 
	'''
	decoration(text)
	query = ask_query()
	while(query):
		if query == 1:
			print(list_to_string(user_input))
			query = ask_query()
		elif query == 2:
			print(user_input)
			query = ask_query()
		elif query == 3:
			append_text = 'to infinity and beyond'
			user_input.append(append_text)
			print(user_input)
			query = ask_query()
		elif query == 4:
			print('Enter the index :')
			user_index = int(input('> '))
			user_input.remove(user_input[user_index])
			print(user_input)
			query = ask_query()
		elif query == 5:
			print('Which word do you want to count : ')
			user_count = input('> ')
			print(user_input.count(user_count))
			query = ask_query()
		elif query == 6:
			print('6')
			query = ask_query()
		elif query == 7:
			print('7')
			query = ask_query()
		elif query == 8:
			print('8')
			query = ask_query()
		elif query == 9:
			print('9')
			query = ask_query()
		else:
			print('Invalid input!')


	#decoration(user_input)

def decoration(val):
	print('_' * 50)
	print('')
	print(val)
	print('_' * 50)

def ask_query():
	query = int(input('> '))
	return query

def list_to_string(myList):
	return ' '.join(myList)




if __name__ == "__main__":
	main()