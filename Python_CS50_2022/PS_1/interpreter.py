def main():
    equations=input("Hey user enter an equation please ")
    x=interpreter(equations)
    print(f"{x:0.1f}")

def interpreter(y):
    y=y.split(" ")
    if y[1]=="+":
        return int(y[0])+int(y[2])
    if y[1]=="/":
        return int(y[0])/int(y[2])
    if y[1]=="-":
        return int(y[0])-int(y[2])
    if y[1]=="*":
        return int(y[0])*int(y[2])
    
if __name__=="__main__":
    main()