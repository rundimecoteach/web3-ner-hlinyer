import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from pprint import pprint
import requests
import re
import justext

sourceFile = 'sourceFile.txt'
outputFile = 'result.txt'

def getFullName(items):
    names = {}
    j = 0
    for i in range(0,len(items)-1):
        if j <= i:
            name = items[i][0]
            if items[i][1] == 'B':
                j = i + 1
                while(j < len(items)):
                    if items[j][1] == 'I':
                        name += ' ' + items[j][0]
                        j += 1
                    else: 
                        break
            if (name not in names) :
                names[name] = 1
            else:
                names[name] += 1
    return names

def getGuessedName(items):
    most_names = Counter(items).most_common(5)
    names = []
    mainName = ''
    for item in most_names:
        if item[0][1] == 'B' and mainName == '':
            mainName = item[0][0]
        else:
            names.append(item[0][0])
    return [mainName] + names

def get_info_from_url(url):
    #get page to text
    page = requests.get(url).text
    #extract text
    text = ''
    paragraphs = justext.justext(page, justext.get_stoplist('English'))
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            text += '\n' + paragraph.text
    article = nlp(text)
    items = [(str(x),x.ent_iob_, x.ent_type_, x.pos_) for x in article 
        if (x.ent_type_ == 'PERSON' and x.pos_ != 'SPACE')]
    arts = [(str(x),x.ent_iob_, x.ent_type_, x.pos_) for x in article 
        if (x.ent_type_ == 'WORK_OF_ART' and x.pos_ != 'SPACE')]
    #get full names
    fullNames = getFullName(items)
    fullArts = getFullName(arts)
    most_names = getGuessedName(items)
    return most_names, fullArts


#load en core
nlp = en_core_web_sm.load()

sources = []
with open(sourceFile,'r',encoding='utf-8') as source_file:
    sources = source_file.read().split()

with open(outputFile,'w',encoding='utf-8') as output_file:
    for source in sources:
        names, arts = get_info_from_url(source)
        art_ind = [x for x in arts.keys()]
        output_file.write(str(names) + '\n')
        output_file.write(str(art_ind))
        output_file.write('\n\n')
print('done')





