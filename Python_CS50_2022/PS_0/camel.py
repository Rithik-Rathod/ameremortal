def main():
   var=input("Ok, input your camel variable and I'll give back a snake variable ")
   snake_var(var)
def snake_var(x):
    for s in x:
        if s.isupper()==True:
            s=s.lower()
            s="_"+s
            print(s, end="")
        else:
            print(s, end="")
    return
            
if __name__=="__main__":
    main()

