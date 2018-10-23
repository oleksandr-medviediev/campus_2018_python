replic_to_bob = input("Speak to Bob \n")
bob_answer = ""

if replic_to_bob == "":
    bob_answer = "Fine. Be that way!"
elif len(replic_to_bob) > 1 and replic_to_bob.endswith("!?"):
    bob_answer = "Calm down, I know what I'm doing!"
elif replic_to_bob.endswith("?"):
    bob_answer = "Sure"
elif len(replic_to_bob) > 1 and replic_to_bob.endswith("?!"):
    bob_answer = "Calm down, I know what I'm doing!"
elif replic_to_bob.endswith("!"):
    bob_answer = "Whoa, chill out!"
else:
    bob_answer = "Whatever."

print(bob_answer)
