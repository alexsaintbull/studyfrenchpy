
from random import choice

from verbs import conj_avoir, conj_etre
from verbs import reg_verbs_er as verbs, pronouns_er_conj as pronouns

n = int(input("How many verbs should I ask you? "))

corrects = 0
errors = {}

past_question = {}

for i in range(n):

	# generating verb and pronoun for the question
	verb = choice(verbs)
	pronoun = choice(list(pronouns))

	# checking that the generated question isn't been asked already
	if verb not in past_question:
		past_question[verb] = list(pronoun)
	else:
		while pronoun in past_question[verb]:
			# generating new pronoun if if the current one was already asked
			pronoun = choice(list(pronouns))
	
	# added current question to the dictionary 
	past_question[verb] = list(past_question[verb]) + list(pronoun)

	# ask the question
	answer = input( pronoun + " ____ (" + verb + "): "  )

	# finding correct answer
	if verb == "avoir":
		rigth_answer = conj_avoir[pronoun]		
	elif verb == "être":
		rigth_answer = conj_etre[pronoun]
	else:
		rigth_answer = verb.removesuffix("er")  + pronouns[pronoun]

	# printing results
	if answer == rigth_answer:
		print("\n\tCORRECT! :)\n")
		corrects += 1
	else:
		print("\n\tWRONG :(\n\n\t" + rigth_answer+"\n")
		errors[answer] = rigth_answer

# printing score and errors
print("\n\nScore: " + str(corrects) + "/" + str(n) + " (" + "{0:0.1f}".format(corrects*100/n) + "%)\n")
if not corrects == n:
	print("See your errors:\n\tAnswer\t\tCorrect\n")
	for a in errors:
		print("\t"+a+":\t"+errors[a])