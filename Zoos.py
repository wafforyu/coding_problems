#You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .
#
#Determine if the entered word is similar to word zoo.
#
#For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

string = input("enter zoo: ")
def zoos(_string):
    for(i in _string):
        if(i == "z"):
            ctr+= 1

#UNDONE!!