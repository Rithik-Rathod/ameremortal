#We are forced to reply, with ony hello. If we reply by any other keyword we'd need to pay upp.
def main():
    greetings=input("Hello user, greet me please")
    greetings=greetings.lower()
    _=greetings_charge(greetings)
    print(_)
def greetings_charge(n):
    if n.startswith("hello"):
        return "0$"
    elif n.startswith("h"):
        return "20$"
    else:
        return "100$"

if __name__=="__main__":
    main()




