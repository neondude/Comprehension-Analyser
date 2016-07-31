from nltk.corpus import wordnet as wn
import string as st

#prepositions and pronouns and common words
preAndPro = ['the','a','an','as','aboard','about','above','abreast','abroad','absent','across','adjacent','after','against','along','alongside','amid','amidst','among','apropos','apud','around','as','atop,','ontop','bar','before','behind','below','beneath','beside','besides','between','beyond','but','by','come','down','during','except','for','from','in','inside','into','less','like','minus','of','off','on','onto','opposite','out','outside','over','past','per','post','pre','pro','qua','re','sans','save','sauf','short','since','sithence','than','through','thru','throughout','thruout','to','toward','towards','under','underneath','unlike','until','up','upon','pon','upside','versus','vs','with','within','without','he','she','it','we','they','me','him','her','us','them','i','what','who','mine','yours','ours','theirs','hers','his','this','that','these','those','whom','whose','which', 'whoever', 'whatever', 'whichever', 'whomever','myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'themselves','anything', 'everybody', 'another', 'each', 'few', 'many', 'some', 'all', 'any', 'anybody', 'anyone', 'everyone', 'everything', 'noone', 'nobody', 'nothing', 'none', 'other', 'others', 'somebody', 'someone', 'something', 'most', 'enough', 'little', 'more', 'both', 'either', 'neither', 'one', 'much', 'such','had','only','so','and','was','been','did','became','become','not']


def getDefList(w):
    defList=[]
    w = w.lower()
    if w not in preAndPro:
        syns = wn.synsets(w)
        count = 0 #get limited number of definitions
        for syn in syns:
            if count == 4:
                break
            defList.append(syn.definition())
            count+=1
    if defList  == []:
        return []
    else:
        return defList

def ParaCompile(para):
    words = para.split()
    rPara = '<p> '
    for word in words:
        cWord = '' #correct word
        for ch in word:
            #remove numbers and special characters from the word
            if ch not in st.digits and ch not in st.punctuation: 
                cWord += ch
        if cWord == '' or cWord in preAndPro:
            rPara += word + ' '
        else:
            defList = getDefList(cWord)
            if defList ==[]:
                rPara += word + ' '
            else:
                rPara += '<a href="#" data-toggle="popover" data-placement="bottom" data-html="true" data-trigger="focus" data-content="<ul>'
                for defs in defList:
                    rPara += '<li>' + defs.replace('"' , '') + '</li><br/>'
                rPara += '">'+word+'</a> '
    rPara += ' </p>'
    return rPara

if __name__ == "__main__":
    fob = open('ParaCompile.html','w')
    result =''
    para = []
    para.append("""Maharana Pratap ruled over Mewar only for 25 years. However, he accomplished so much grandeur
during his reign that his glory surpassed the boundaries of countries and time turning him into an
immortal personality. He along with his kingdom became a synonym for valour, sacrifice and patriotism.
Mewar had been a leading Rajput kingdom even before Maharana Pratap occupied the throne. Kings of
Mewar, with the cooperation of their nobles and subjects. had established such traditions in the
kingdom. as augmented their magnificence despite the hurdles of having a smaller area under their
command and less, population. There did come a few thorny occasions when the flag of the kingdom
seemed sliding down. Their flag once again heaved high in the sky thanks to the gallantry and brilliance
of the people of Mewar. """)
    para.append("""The destiny of Mewar was good in the sense that barring a few kings, most of the rulers were
competent and patriotic. This glorious tradition of the kingdom almost continued for 1500 years since
its establishment. right from the reign of Bappa Rawal. In fact only 60 years before Maharana Pratap,
Rana Sanga drove the kingdom to the pinnacle of fame. His reputation went beyond Rajasthan and
reached Delhi. Two generations before him, Rana Kumbha had given a new stature to the kingdom
through victories and developmental work. During his reign, literature and art also progressed
extraordinarily. Rana himself was inclined towards writing and his works are read with reverence even
today.The ambience of his kingdom was conducive to the creation of high quality work of art and
literature. These accomplishments were the outcome of a longstanding tradition by several generations. """)
    para.append("""The life of the people of Mewar must have been peaceful and prosperous during the long span of time:
otherwise such extraordinary accomplishment in these fields would not have been possible. This is
reflected toed in their art and literature as well as their loving nature. They compensate for lack of
admirable physique by their firm but pleasant nature. The ambience of Mewar remains lovely thanks to
the cheerful and liberal character of its people.
 """)
    para.append(""" One may observe astonishing pieces of workmanship not only in the forts and palaces of Mewar but
also in public utility buildings. Ruins of many structures which are still standing tall in their grandeur are
testimony to the fact that Mewar was not only the land of the brave but also a seat of art and culture
Amidst aggression and bloodshed, literature and art flourished and creative pursuits of literature and
artists did not suffer. Imagine how glorious the period must have been when the Vijaya Stambha which
is the sample of our great ancient architecture even today. wasconstructed. In the same fort, Kirti
Stambha is standing high reflecting how liberal the then administration was which allowed people from
other communities and kingdoms to come and carry out construction work. It is useless to indulge in the
debate whether the Vijay Stambha was constructed first or the Kirti Stambha. The factis that both the
capitals are standing side by side and reveal the proximity between the king and the subjects of Mewar. """)
    para.append("""The cycle of time does not remain the same. Whereas the reign of Rana Sanga was crucial in raising
the kingdom to the acme of glory, it also proved to be his nemesis. History took a turn. The fortune of
Mewar- the land of the brave, started waning. Rana tried to save the day with his acumen which was
running against the stream and the glorious traditions for sometime.
 """)
    for par in para:
        result += ParaCompile(par)
    fob.write(result)
    fob.close()