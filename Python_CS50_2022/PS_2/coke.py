def main():
    z=0
    while(z<50):
        coin=int(input(f"Gimme {50-z} cents more"))
        if coin==5 or coin==10 or coin==25:
            z+=coin
    if (z==50):
        print("Enjoy ur coke")
    else:
        print(f"Aight here's your coke and here you go, your {z-50} cents which I owe you")
        
if __name__=="__main__":
    main()
