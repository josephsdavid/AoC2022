import os
import sys
import string


root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time


LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = "".join([x.upper() for x in LOWER_LETTERS])
LOWER_DICT = {letter:cnt+1 for cnt, letter in enumerate(LOWER_LETTERS)}
UPPER_DICT = {letter:cnt+27 for cnt, letter in enumerate(UPPER_LETTERS)}


def data_load()->list:
	# ./day3/
	with open('./day3/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [(line[:len(line)//2], line[len(line)//2:]) for line in data]
	return arr	

def calc_part_A(arr:list)->int:
	total_sum = 0
	for x in range(len(arr)):
		common_letter = "".join(set(arr[x][0]) & set(arr[x][1]))
		if common_letter.isupper():
			total_sum += UPPER_DICT[common_letter]
		elif common_letter.islower():
			total_sum += LOWER_DICT[common_letter]
		else:
			raise ValueError(f'Your inputs whack.  Aka not a string')
	return total_sum

def calc_part_B(arr:list)->int:
	total_sum = 0
	#probably shouldn't have split them up in the dataload but ¯\_(ツ)_/¯
	arr = ["".join([x[0], x[1]]) for x in arr]
	#Check the remainder of the length of the array divided by 3 is zero
	assert len(arr) % 3 == 0
	for x in range(0, len(arr), 3):
		common_letter = "".join(set(arr[x]) & set(arr[x + 1]) & set(arr[x + 2]))
		if common_letter.isupper():
			total_sum += UPPER_DICT[common_letter]
		elif common_letter.islower():
			total_sum += LOWER_DICT[common_letter]
		else:
			raise ValueError(f'Your inputs whack.  Aka not a string')
	return total_sum


@log_time
def run_part_A():
	data = data_load()
	sack_sum = calc_part_A(data)
	return sack_sum

@log_time
def run_part_B():
	data = data_load()
	sack_sum = calc_part_B(data)
	return sack_sum

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Part A
#Goal. 
#Count up all the letters in common between the two rucksacks in each line. 

#gameplan
#input data
#list of string tuples split by length. 

#Do a set comparison between the two halves for the common letters. 
#then add up their letter equivalents in the letter_dicts. 

#Part B
#Rejoin the tuples from data_load
#Iterate in steps of 3 and do set comparisons between the groups of 3.
