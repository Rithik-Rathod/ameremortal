def main():
    plate_no=input("So, what no. do you want?")
    if isvalid(plate_no) ==True :
        print("Ok this is cool")
    else:
        print("invalid")
def isvalid(x):
    if len(x)>6 or len(x)<2:
        return False
    else:
        for s in x:
             if s.isalnum()==False:
                  return False

        for s in x[0:1]:
       
                    if s.isalpha()==False:
                        return False
                    else:  
                        continue

        for s in x[2:]:    
                if s.isnumeric()==True:
                    if s=="0":
                        return False
                    else :
                        if x[-1].isalpha()==True:
                            return False
                        else:
                            return True
                else:
                    continue
    return True
            
if __name__=="__main__":
    main()


        

