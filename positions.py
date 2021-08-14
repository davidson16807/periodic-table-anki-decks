from tools import *

def cloze(hidden):
	return '{{c1::'+hidden+'}}'

for established, introduced in pairwise(sequences):
	for shown in established:
		# introduce element by asking which element is below an established one
		if shown in below:
			hidden = below[shown]
			print(adjacency_card_html(
				element_html(shown, abbreviation[shown]), 
				element_html(cloze(hidden), cloze(abbreviation[hidden])), 
				direction='column',
				tags=['element_to_element_below']
			))
	for shown in introduced:
		# reinforce the mapping above in the opposite direction
		if shown in above:
			hidden = above[shown]
			print(adjacency_card_html(
				element_html(shown, abbreviation[shown]), 
				element_html(cloze(hidden), cloze(abbreviation[hidden])), 
				direction='column-reverse',
				tags=['element_to_element_above']
			))
	for shown in introduced:
		# reinforce the mapping above in the opposite direction
		if shown in before:
			hidden = before[shown]
			print(adjacency_card_html(
				element_html(shown, abbreviation[shown]), 
				element_html(cloze(hidden), cloze(abbreviation[hidden])), 
				direction='row-reverse',
				tags=['element_to_element_before']
			))
	for shown in introduced:
		# establish the shown comes after another that has already been introduced
		if shown in after:
			hidden = after[shown]
			print(adjacency_card_html(
				element_html(shown, abbreviation[shown]), 
				element_html(cloze(hidden), cloze(abbreviation[hidden])), 
				direction='row',
				tags=['element_to_element_after']
			))
