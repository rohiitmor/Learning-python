#write a python program to display a user entered name followed by good afetr noon usnig input () function 
name = input("enter you name ")

print(f"good afternoon {name}")


#write a python program to fill in a letter template given below with name and date 
name = input("Enter your name: ")
date = input("Enter date: ")

letter = f'''Dear {name},
You are cordially invited to attend the event on {date}.

Thank you,
[Your Name]
'''

print(letter)
