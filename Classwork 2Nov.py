# генератор названий компаний

import random

names = ["пром","агро","торг","урал","север","юг","техно",
"экспо","метал","нефть","сельхоз","фарм","строй",
"кредит","алмаз","-девелопмент","развитие","мос",
"рос","кубань","сибирь","восток","нано","софт",
"микро","онлайн","инвест","текстиль","цемент"]

company_name = ""
for x in range(6):
    company_name = company_name + random.choice(names)


print(company_name)


#транслитератор

import string
def translit (d, text):
    temp = ""
    for s in text:
        temp = temp + d.get(s)
    return temp



d = {'а':'a','б':'b','в':'v', 'г':'g','д':'d','е':'e','ё':'eo','ж':'zh','з':'z','и':'i','й':'j','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'*','ы':'y','ь':'*','э':'e','ю':'u','я':'ya',' ':' ','—':'—'}

text = input ('введите текст')
text = text.lower().translate(str.maketrans('','',string.punctuation))
text = translit (d, text)
print(text)