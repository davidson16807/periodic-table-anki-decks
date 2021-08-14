from tools import *

for established, introduced in pairwise(sequences):
	for shown in introduced:
		# inforce retrieval of element from atomic number
		print(property_card_html(
			element_html('{{c1::'+shown+'}}', '{{c1::'+abbreviation[shown]+'}}', str(element_to_index[shown])),
			tags=['number_to_element']
		))
	for shown in introduced:
		# inforce retrieval of atomic number from element name
		print(property_card_html(
			element_html(shown, abbreviation[shown], '{{c1::'+str(element_to_index[shown])+'}}'),
			tags=['element_to_number']
		))
