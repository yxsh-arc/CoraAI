def i(i):
    i = i.lower()

    if "namaste" in i:
        return "Namaste aap kaise hai 😄"

    if "hi" in i or "hello" in i or "hey" in i or "hoi" in i:
        return "Hey! kaise ho? 😄"

    if "acha" in i or "achi" in i or "accha" in i or "acchi" in i:
        return "Are wah, toh fir batao Aaj kya karna hai 😄"

    if i == "bye":
        return "exit"

    return "samjha nahi thora aur batao 🤔"

while True:
        user = input("You: ").lower()

        result = i(user)

        if result == "exit":
            print("AI: Bye bye 👋")
            break

        print("AI:", result)