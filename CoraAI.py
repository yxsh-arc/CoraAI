#_______IMPORTS_______

import random

#_______FUNCTION_______

def chat(text):
    text = text.lower()
    words = text.split()

#_______WORDS_______

    greet_words = [ "hi", "hello", "hii", "hey", "hoi" ]
    
    happy_words = [ "acha", "accha", "achi", "acchi", "happy", "khush" ]

    sad_words = [ "sad", "udaas", "dukhi", "mood off" ] 

#_______REPLIES_______

    greet_replies = [ "Hey! Kaise ho? 😄", "Hey! Kya haal hai? 😄", "Bolo boss.. Kya scene hai?" ]


    happy_replies = [ "Are wah, toh fir batao Aaj kya karna hai 😄", "Badiya! Aur batao kya chal raha hai" ]


    sad_replies = [ "Chinta mat karo me huna 🫂🌷", "Chinta mat kar bro sab thik ho jayega bas khudko thora time do  🫂😄"]


#_______RANDOM_CHOICE_______

    if any(word in words for word in greet_words):
        return random.choice(greet_replies)

    if "namaste" in words:
        return "Namaste aap kaise hai 😄"

    if any(word in words for word in happy_words):
        return random.choice(happy_replies)

    if any(word in words for word in sad_words):
        return random.choice(sad_replies)

    if "bye" in words:
        return "exit"

    return "samjha nahi thora aur batao 🤔"

#_______TITLE_______

print("CORA AI™ • DEMO VERSION --v0.8")
print(" ")

#_______LOOP_______

while True:
    user = input("You: ")

    result = chat(user)

    if result == "exit":
        print("AI : Bye bye 👋")
        print("support us by donating 1$ for CORA AI project, UPI: tayash@fam")
        break

#_______OUTPUT_______

    print("AI: ", result)