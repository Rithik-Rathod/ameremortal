#We'll convert emojis into emoticons.
x=input(" I'll convert magically your emoticons to emojis")
#The emoticons were obtained from the PS using inspector element.
x=x.replace(":(","🙁")
x=x.replace(":)","🙂")
print(x)
