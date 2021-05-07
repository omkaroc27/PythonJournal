import os
import json #json exposes an API familiar to users of the standard library 
import difflib


from difflib import get_close_matches

data =json.load(open("D:\python sem1\data.json"))
c='y'
def extract(word):
                    word=word.lower()
                    if word in data:
                                        return data[word]

                    elif len (get_close_matches(word,data.keys())) > 0 :
                                       new=input("\nDid you mean %s ?\n\nEnter 'y' if yes.\n'n' if No\n"% get_close_matches)
                                       new=new.lower()
                                       if new =="y":
                                             return data[get_close_matches(word,data.keys())[0]]
                                       elif new=='n' :
                                                            print("\nsorry unfortunatly we don't have the meaning ")
                                       else:
                                        print("Type y/n not anything else .can you Be more Wrong")
                    else :
                                        return"the word entering is worng please try again."
                                       
Enter=input("Enter your Word :")
means=extract(Enter)
print(means)