meme_dict = {
            "apple": "apfel",
            "water": "wasser",
            "ballons": "luftballons",
            "book": "buch"
            }
word = input("write unclear word:")
if word in meme_dict.keys():
    print(meme_dict[word])
