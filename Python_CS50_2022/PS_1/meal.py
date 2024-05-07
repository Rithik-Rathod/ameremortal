def main():
    time=input("Hey user what's the time? ")
    t=convert(time)
    food_time=is_it_eating_time(t)
    print(food_time)

def convert(x):
    x=x.split(":")
    y=x[1].split(" ")
    y[1]=y[1].lower()
    if y[1]=="pm" and float(x[0])!=12:
        x[0]=float(x[0])+12
    return float(x[0]) + float(float(y[0])/60) 

def is_it_eating_time(n):
    if 7<=n<=8:
        return "breakfast time!"
    elif 12<=n<=13:
        return "Lunch time!"
    elif 19<=n<=20:
        return "dinner time"

if __name__=="__main__":
    main()


