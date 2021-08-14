from tools import *

for established, introduced in pairwise(sequences):
	for shown in introduced:
		# inforce retrieval of element name from symbol
		print(property_card_html(
			element_html('{{c1::'+shown+'}}', abbreviation[shown], str(element_to_index[shown])),
			tags=['element_to_symbol']
		))
	for shown in introduced:
		# inforce retrieval of symbol from element name
		print(property_card_html(
			element_html(shown, '{{c1::'+abbreviation[shown]+'}}', str(element_to_index[shown])),
			tags=['element_to_symbol']
		))
