import os
from termcolor import colored, cprint
print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')

checklist = list()

def create(item):
	checklist.append(item)

def read(index):
	item = checklist[int(index)]
	return item

def update(index, item):
	checklist[index] = item

def destroy(index): 
	checklist.pop(index)

def list_all_items():
	index = 0
	for list_item in checklist:
		print_red_on_cyan("{} {}".format(index, list_item))
		index += 1

def mark_completed(index):
	checklist[index] = "√" + checklist[index]
	
def select(function_code):
	#Create item
	if function_code == "C" or function_code == "c":
		input_item = user_input("Add to list: ")
		create(input_item)

	elif function_code == "R" or function_code == "r":
		item_index = user_input("Index Number?")

		# Remember that item_index must actually exist or our program will crash.
		print_red_on_cyan(read(int(item_index)))

	elif function_code == "U" or function_code == "u":
		item_up = user_input("Index Number?")
		input_up = user_input("Input item:")
		update(int(item_up), input_up)

	elif function_code == "D" or function_code == "d":
		item_del = user_input("Enter Index Number: ")
		destroy(int(item_del))

	elif function_code == "M" or function_code == "m":
		input_mark = user_input("Index Number:")
		mark_completed(int(input_mark))

	elif function_code == "P" or function_code == "p":
		list_all_items()

	elif function_code == "Q" or function_code == "q":
		return False
	else:
		print("Unknown Option")
	return True

def user_input(prompt):
	# the input function will display a message in the terminal 
	# and wait for user input.
	user_input = input(prompt)
	os.system("clear")
	return user_input


running = True

while running:
	selection = user_input( 
		"Press C to add to list, R to Read from list, U to update list, D to destroy item in list, M to mark list item done, P to display list, and Q to quit:  ")
	running = select(selection)

	

# def test():
	
# 	# create("purple sox")
# 	# create("red cloak")

# # 	#print(read(0))
# # 	#print(read(1))

# # 	update(0, "purple socks")
# # 	destroy(1)

# # 	#print(read(0))

# # 	#list_all_items()

# # 	select("C")
# # 	#list_all_items()

# # 	select("R")
# # 	#list_all_items()

# test()
