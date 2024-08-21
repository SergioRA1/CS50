name = input("What's your name? ") #asks what's the user's name # name is an input
#print("hello", name, "nice to meet you", end= "")
# returns `hello (user input) nice to meet you´
#end = ""-- makes print not create a new line at the end, which it does by default which is interesting
name = name.strip()#deletes spaces on left and right
name = name.title()

#:you can join them together
name = name.strip().title()

#better way of doing that string
print(f"hello, {name}")
