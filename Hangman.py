import random
import wordsList
w=random.choice(wordsList.words)
word=list(w)
Guessed=[]
for _ in word:
    Guessed.append("_")
attempts=0
maxAttempts=len(word)-2
isGameover=False
while not isGameover:
    print("You have {0} attempts remaining".format(maxAttempts-attempts))
    let=input("Enter a single letter player :):")
    if let in word:
        print("Great! {0} is in the word".format(let))
        for i in range(len(word)):
            if word[i]==let:
                word[i]='_'
                Guessed[i]=let
        print("So far you guessed: {0}".format(" ".join(Guessed)))
    else:
        print("Oops! thats not in the word sorry")
        attempts+=1
    print("________________")
    print("|"+"      |")
    print("|" + ("      O" if attempts>0 else " "))
    print("|" +("     / \\ " if attempts>1 else " "))
    print("|" +("      | " if attempts>2 else " "))
    print("|"+("     / \\" if attempts>3 else " "))
    print("|")
    if all(x=="_" for x in word):
        print("You are corrrect! Congratulations you won")
        print("Great!")
        f=input("Enter anything to exit")
        isGameover=True
    elif maxAttempts==attempts:
        print("OOps you lost :(")
        f=input("Enter anything to exit")
        isGameover=True
       
    