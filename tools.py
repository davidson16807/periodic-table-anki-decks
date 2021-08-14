import itertools

def split(elements, trigger):
	result = [[]]
	for element in elements:
		if trigger(element) and len(result[-1]) > 1:
			result.append([])
		else:
			result[-1].append(element)
	return result

def whitespace(text):
	return len(text.strip()) < 1

def pairwise(elements):
	last = elements[0]
	for current in elements[1:]:
		yield last, current
		last = current

with open('groups.txt') as file:
	groups = split([line.strip() for line in file.readlines()], whitespace)

with open('flashcard-sequence.txt') as file:
	sequence = [line.strip() for line in file.readlines()]
	sequences = split(sequence, whitespace)

with open('indices.txt') as file:
	index_lines = file.readlines()
	index_to_element = {int(line.split('\t')[0]) : line.split('\t')[1].strip() for line in index_lines if not whitespace(line)}
	element_to_index = {line.split('\t')[1].strip() : int(line.split('\t')[0]) for line in index_lines if not whitespace(line)}

with open('abbreviations.txt') as file:
	abbreviation = {line.split('\t')[1].strip() : line.split('\t')[0] for line in file.readlines() if not whitespace(line)}

with open('adjacency-template.html') as file:
	adjacency_template = file.read()

with open('property-template.html') as file:
	property_template = file.read()

with open('element-template.html') as file:
	element_template = file.read()

above = {}
below = {}
for group in groups:
	for top,bottom in pairwise(group):
		above[bottom] = top
		below[top] = bottom

before = {}
after = {}
for element in element_to_index:
	i = element_to_index[element]
	if (i-1) in index_to_element:
		before[element] = index_to_element[i-1]
	if (i+1) in index_to_element:
		after[element] = index_to_element[i+1]

ordering = {sequence[i]:i for i in range(0,len(sequence))}

def element_html(name, abbreviation='', number='', mass=''):
	result = element_template
	result = result.replace('{{name}}', name)
	result = result.replace('{{abbreviation}}', abbreviation)
	result = result.replace('{{number}}', number)
	result = result.replace('{{mass}}', mass)
	return result

def adjacency_card_html(shown, hidden, direction='column', tags=[]):
	result = adjacency_template
	result = result.replace('{{shown}}', shown)
	result = result.replace('{{hidden}}', hidden)
	result = result.replace('{{direction}}', direction)
	result = result.replace('{{tags}}', ('\t'+' '.join(tags)) if tags else '')
	return result

def property_card_html(shown, tags=[]):
	result = property_template
	result = result.replace('{{shown}}', shown)
	result = result.replace('{{tags}}', ('\t'+' '.join(tags)) if tags else '')
	return result
