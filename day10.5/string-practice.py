#!/usr/bin/env python3

given_string = "Practice is an important tool to being successful and it helps one’s goal come true. I hoped I could pass the practical test of manicure license. Manicure test had two parts, the practical and the written one, so I had to practice more than 10 times a day. Practice influences us all the time. The newborn baby has to practice in order to walk and speak because no baby is born with the capability of either talking or walking. The baby learns from human beings around them. The baby starts learning step by step. Parents always hold the baby’s hands as they help the baby make small steps. A baby does have to practice daily until he or she knows how to walk, the baby does fall always however, parents believe that continued practice can help it achieve its goal of walking hence day by day the baby can walk. Parents always worry about its physical problem like falling down and weak legs before it knows how to walk. Finally, they do feel happy and successful after the baby knows how to walk."

def wordCount(s):
    s.split()
    return len(Given_string)

word_count = wordCount(Given_string)
print(word_count)


#############################

def whiteSpaceRemover(s):
    s.replace(' ', '#')
    return s

cleaned_string = whiteSpaceRemover(given_string)
print(cleaned_string)


#############################

x_string = "23$23$23$23$45$56$555$6784$678"

total = 0
for i in x_string.split('$'):
    total += int(i)

print(total)


#############################

def cashCounter(s):
    result = s.count('$')
    return result

cash_sign_count = cashCounter(x_string)
print(cash_sign_count)


#############################

x_list = ['Parents ','always',' worry',' about',' its',' physical',' problem',' like',' falling down',' and',' weak ','legs',' before ','it',' knows',' how ','to',' walk.',' Finally,',' they ','do',' feel',' happy',' and',' successful',' after',' the ','baby',' knows',' how',' to',' walk.']
x_list_str = "".join(x_list)
print(x_list_str)

alphabet = input('Enter your alphabet seperated by commas (E.G: a, d, c, x, z, q): ')
alphabet_list = alphabet.split(', ')
print(alphabet_list)

total = []
for i in alphabet_list:
    for x in x_list:
        if i in x:
            total.append(x.replace(' ', ''))
print(total)
