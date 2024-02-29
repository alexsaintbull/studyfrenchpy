
from random import choice

from verbs import conj_avoir, conj_etre
from verbs import reg_verbs_er as verbs, pronouns_er_conj as pronouns

n = int(input("How many verbs should I ask you? "))

corrects = 0

past_question = {}

for i in range(n):

	verb = choice(verbs)
	pronoun = choice(list(pronouns))

	if verb not in past_question:
		past_question[verb] = list(pronoun)
	else:
		while pronoun in past_question[verb]:
			pronoun = choice(list(pronouns))
	
	past_question[verb] = list(past_question[verb]) + list(pronoun)

	answer = input( pronoun + " ____ (" + verb + "): "  )

	if verb == "avoir":
		rigth_answer = conj_avoir[pronoun]		
	elif verb == "être":
		rigth_answer = conj_etre[pronoun]
	else:
		rigth_answer = verb.removesuffix("er")  + pronouns[pronoun]

	if answer == rigth_answer:
		print("\nCORRECT! :)\n")
		corrects += 1
	else:
		print("\nWRONG :(\n")
		print("\t" + rigth_answer+"\n")

print("Score: " + str(corrects) + "/" + str(n) + " (" + "{0:0.1f}".format(corrects*100/n) + "%)\n")