def main():
    aoe=input("So user, what is the answer of everything?")
    aoe=aoe.lower()
    answer_of_everything(aoe)

def answer_of_everything(n):
    match n:
        case "42"|"forty two"|"forty-two":
            print("yes")
        case _:
            print("No")

        
main()