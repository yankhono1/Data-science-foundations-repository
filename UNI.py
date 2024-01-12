# welcome message
print("Hi! My name is UNI, the university chatbot, and I a here to help you through your reception :")
print("I am going to ask you a few questions to get to know you a little better.")

# name
name = input("What is your name? ")
print(f"Hi {name}")

# age
age = int(input("How old are you? "))
if age >= 55:
    response = "You must be one of out PhD students, it's great to have you here"
elif age >= 40:
    response = "You must be one of our postgraduate students, nice to meet you"
elif age >= 35:
    response = "It is never too late to pursue your dreams"
elif age >= 17:
    response = "Wow! You are starting university at a young age!"
elif age > 13:
    response = "You must be one of the child prodigies I have heard of you"
else:
    response = "Age is just a number :)"

# the order of the elif statements are important
print(response)

# faculty
faculty = input("What faculty are you in? ")
print(f"The {faculty} faculty is really geat. How exciting!")

# majors
majors = input("Are you majoring in anything? ")
if majors.lower() == "yes":
    majors2 = input("What are you majoring in? ")
    print(f"Ah, {majors2}. A friend of mine studied that.")
elif majors.lower() == "no":
    print("Okay, no problem")
else:
    print("Please answer with 'yes' or 'no'.")

print("I think that is all...")
print("Oh wait! I have a few more questions")

# favourite coulor
fav_colour = input("What is your favorite colour? ")
fav_colour_lower = fav_colour.lower()

team_colors = ["green", "red", "black"]

if fav_colour_lower in team_colors:
    print(f"You are at the right place! {fav_colour} is one of our team colors.")
else:
    print("Those are nice colors, but I like green, red, and black because they're our team colors.")

# end_program = "bye"
end_words = ["bye", "goodbye", "exit", "quit"]
print(f"Thank you for telling me moe about yourself! It was great talking to you {name}.")
print(f"\nI hope you enjoy working with the {faculty} faculty") 
print("\nI will do my best to answer some questions that you may have.") 
print(f"\nWhen you are done asking questions, you can just say {end_words}")

# dictionary holding questions and answers
qa = {
  "where is the fees office": "The fees office is located in the Blue building on Moores lane.",
  "who can help me with my curriculum form": "You can speak to your adviser or Orientation leader.",
  "where can i find out more about student accommodation": "The SRC can help you with that.",  
  "what clubs does the university offer": "The university offers a wide range of clubs.",
  "which courses should i take": "You can talk to an Orientation Leader or your course advisor.",
  "who is my student mentor": "You can find out who your student mentor is by reporting to Room 42"
}


# Defines a new function called ask_question that takes a parameter called question.
def ask_question(question):
  question = question.lower().strip()
  # cek if question is in qa dictionarry
  answer = qa.get(question)
  # if question is found print the answer
  if answer:
    print(answer)
    # if answer is one of the end words, print goodbye  
  elif question in end_words:
    print("Goodbye!")
    return True # exit loop
  
  else:
    print("I don't understand. Please try again.")
    
  return False

# print("\nHi again, welcome to the university help chatbot!")
# name = input("What is your name? ")
print(f"\n{name} Please ask me anything about the university.")

done = False
while not done:
  question = input("\nWhat is your question? ")
  done = ask_question(question)

print("\nThanks for using the university help chatbot!")

