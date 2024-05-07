def main():
    greetings=input("Hello user, great me please")
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




