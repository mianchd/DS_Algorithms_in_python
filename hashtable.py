
"""
hashtable implemtation using list of lists
Chaning aproach

"""

table_size = 10
table = [[] for _ in range(table_size)]

# Modulos Hash helper function
def hash_function(input):
	return input % table_size

def insert(key, value):
	table[hash_function(key)].append(value)

insert(32, 'toyota')
insert(24124, 'honda')
insert(32, 'bentley')

print(table)