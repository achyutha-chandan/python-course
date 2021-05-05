#SayOurName.py-lets everybody print thier name on the screen many times
name = input ("What is your name?\n")
while name !="":
    for x in range(100):
        print(name,end = "")
    print()
    name = input("Type another name,or just hit [Enter] to quit:")
print("Thanks for playing!")
