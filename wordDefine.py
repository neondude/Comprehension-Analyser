from nltk.corpus import wordnet as wn

def getDefList(w):
    defList=[]
    syns = wn.synsets(w)
    for syn in syns:
        if (syn.lemmas()[0].name())==w:
            defList.append(syn.definition())
    if defList  == []:
        return ['No clear definitions for the given word']
    else:
        return defList

if __name__ == "__main__":
    word = raw_input("enter a word: ")
    for wdef in getDefList(word):
        print wdef