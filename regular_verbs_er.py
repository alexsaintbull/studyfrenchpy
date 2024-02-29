
import random

verbs = ["adorer", "aimer", "arriver","avoir","détester","donner","être","habiter","monter","parler","réserver","rester"]
pronouns = {"je":"e", "tu":"es", "il/elle":"e", "nous":"ons", "vous":"ez", "ils/elles":"ent"}

conj_avoir = {"je":"ai", "tu":"as", "il/elle":"a", "nous":"avons", "vous":"avez", "ils/elles":"ont"}
conj_etre = {"je":"suis", "tu":"es", "il/elle":"est", "nous":"sommes", "vous":"êtes", "ils/elles":"sont"}

n = int(input("How many verbs should I ask you? "))

corrects = 0

for i in range(n):

	verb = random.choice(verbs)
	pronoun = random.choice(list(pronouns))

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