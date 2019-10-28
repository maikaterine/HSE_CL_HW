#ЗАДАЧА 1
a = 23
b = 34.02
c = "python is cool "
d = "you are cool, too"
print(a+b)#можно складывать, вычитать, умножать, делить
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
#print(a+c) а вот строки и числа сложить нельзя, т.к. это разный тип данных
print(c+d)# две строки сложить можно
#e = (c+d)
#print (e-d) #а вычитать нельзя
print (c*2) #строки можно умножать на числа
#print(c*d) а перемножать строки уже нельзя

#Задача2
a = "добрый"
b = ' '
c = 'вечер'
d = (a + b + c)
print (d)
print (c+b+a)

#Задача3
word = "апельсин"
print(word)
one = (word [2:5])
my_word =(word [5]+ word[1]+word[0]+word[7]+word[6]+one)
print (my_word)

#Задача4
text = "WOW,NOEL SEES LEON"
print(text.lower())
text_new = text.lower()
print (text_new[::-1])
