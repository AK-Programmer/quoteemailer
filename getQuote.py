import pandas as pd
import random

#importing data
def importData():
    data = pd.read_csv(r'quotes.csv', dtype=object)
    df = pd.DataFrame(data, columns=['Quote', 'Author', 'Tags'])
    df = df[df['Tags'].str.contains('philosophy', na=False)] #Filtering out quotes not related to philosophy
    return df

def chooseQuote(): #Chooses the quote and makes sure it hasn't been chosen before
    quoteChosen = False #Tells the program if a quote has been chosen
    f = open("previous.txt", mode='r', encoding='utf-8')

    while quoteChosen == False:
        index = random.randint(1, 19666) #Choose random number between 1 and 19,666
        input = "1" #Will store input from file
        newQuote = True #Tells the program if the quote hasn't already been sent before

        for line in f: #Check if index is equal to any old indexes in the file
            input = f.read(1)
            if index == input:
                newQuote = False
                break
        if newQuote == True:
            quoteChosen = True
            f.close()

            #Write the new index to the file
            with open ("previous.txt", 'a', encoding='utf-8') as f:
                f.write(str(index))
                f.write("\n")
                f.close()
    return index

def grabQuote(df, index):
    index = chooseQuote()
    final_quote = df.iloc[index, 0]
    final_author = df.iloc[index, 1]
    message = "\"" + final_quote + "\"" + "\n - " + final_author + "\nHave a great day! - Adar"
    return message
