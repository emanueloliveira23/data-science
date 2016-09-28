
# Utilities functions

def retrieve_columns(file, columns, separator = " "):
	
	file.seek(0)
	file.readline()
	
	res = []
	
	for line in file:
		parts = line.split(separator)
		item = []
		for column in columns:
			item.append(parts[column])
		res.append(item)
		
	return res

def retrieve_columns_as_float(file, columns, separator):
	columns = retrieve_columns(file, columns, separator)
	values_as_str = map(map_to_first, columns)
	values_as_float = map(map_to_float, values_as_str)
	return values_as_float
	
def map_to_first(item_as_array):
	return item_as_array[0]

def map_to_float(item_as_string):
	return float(item_as_string)


# Menu functions

def count_entries(entries):
	return len( entries )

def min_entry(entries):
	return min( entries )

def max_entry(entries):
	return max( entries )

def mean_entry(entries):
	sum = 0
	for v in entries:
		sum += v
	return sum / len(entries)
	
def median_entry(entries):
	values_sorted = sorted(entries)
 	mean = int( len(values_sorted) / 2 )
 	if (mean % 2 == 0):
 		return (values_sorted[mean] + values_sorted[mean+1]) / 2
	else:
		return values_sorted[mean]
	
	
# Main execution

print "------------------"
print "Univariate analiys"
print "------------------"

dataset = "data.txt" # raw_input('dataset: ')
column = 0 # int(raw_input('column index: '))
separator = '\t'

print 'Begining analisys...\n'

with open(dataset) as file:
	entries = retrieve_columns_as_float(file, [column], separator)
	print 'Number of entries: ', count_entries(entries)
	print 'Min of entries: ', min_entry(entries)
	print 'Max of entries: ', max_entry(entries)
	print 'Mean of entries: ', mean_entry(entries)
	print 'Median of entries: ', median_entry(entries)
	
	
