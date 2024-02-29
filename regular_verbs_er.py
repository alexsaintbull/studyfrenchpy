
from random import choice

from verbs import conj_avoir, conj_etre
from verbs import reg_verbs_er as verbs, pronouns_er_conj as pronouns

n = int(input("How many verbs should I ask you? "))

corrects = 0

for i in range(n):

	verb = choice(verbs)
	pronoun = choice(list(pronouns))

	answer = input( pronoun + " ____ (" + verb + "): "  )

	if verb == "avoir":
		rigth_answer = conj_avoir[pronoun]		
	elif verb == "être":
		rigth_answer = conj_etre[pronoun]
	else:
		rigth_answer = verb.removesuffix("er")
		rigth_answer = rigth_answer + pronouns[pronoun]

	if answer == rigth_answer:
		print("\nCORRECT! :)\n")
		corrects += 1
	else:
		print("\nWRONG :(\n")
		print("\t" + rigth_answer+"\n")

print("Score: " + str(corrects) + "/" + str(n) + " (" + str(corrects*100/n) + "%)\n")