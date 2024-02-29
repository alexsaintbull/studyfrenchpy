from random import choice
from itertools import product

from verbs import conj_avoir, conj_etre
from verbs import reg_verbs_er as verbs, pronouns_er_conj as pronouns 

n = int(input("\nHow many verbs should I ask you? "))

corrects = 0
errors = {}

questions = list(product(verbs, list(pronouns)))

for i in range(n):

	try:
		question = choice(questions)
	except IndexError as e:
		print("\nSorry, I don't have any more questions for you :(")
		quit()
		
	verb = question[0]
	pronoun = question[1]

	questions.remove(question)	

	# ask the question
	answer = input("\n"+str(i+1)+"/"+str(n)+"\n"+pronoun+" ____ ("+verb+"): ")

	while answer[-1] == " ":
		answer = answer.removesuffix(" ")

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
print("\n\n")