import pandas

data = pandas.read_csv(r"/workspaces/100_Days/Lesson_26_NATO/nato.csv")


alphabet = {row.Letter: row.Codeword for (index,row) in data.iterrows()}
word = ""
while word != "quit":
    word = input("Word: ").upper()
    answer = [alphabet[letter] for letter in word]
    print(answer)    
