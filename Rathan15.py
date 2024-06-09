with open("Quotes.Txt","r") as file:
    count=0
    for line in file:
        word=line.spilt()
        count+= len(words)
        print(count)

