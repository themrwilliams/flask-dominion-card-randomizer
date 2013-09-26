import csv
import random

class Dominion:
	cards = []

	def __init__(self):
		reader = csv.reader(open('data/cards.txt'), delimiter="|", quotechar="", quoting=csv.QUOTE_NONE)
		for row in reader:
			self.cards.append(row)

	def get_random_cards(self, sets=[]):
		if (sets is []):
			return []

		filtered = []
		for card in self.cards:
			if card[1] not in sets:
				continue

			filtered.append(card)

		random.shuffle(filtered)

		filtered = filtered[:10]

		return filtered
