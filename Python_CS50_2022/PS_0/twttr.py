def main():
    tweet=input("Aight shoot your tweet ")
    tweet_without_vowels(tweet)
def tweet_without_vowels(x):
    for s in x:
        if s.lower()=="a" or s.lower()=="e" or s.lower()=="i" or s.lower()=="o" or s.lower()=="u":
            continue
        else:
            print(s, end="")

if __name__=="__main__":
    main()


