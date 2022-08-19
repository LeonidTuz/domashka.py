name = open(r'C:\Users\tuzle\Desktop\info.txt', 'r', encoding='utf-8')

logins = list()

for row in name:
    stroki = row.split(', ')
    for words in stroki[1]:
        word = words.split(' ')
        logins.append(word[0])
        break
    for words_2 in stroki[2]:
        word_2 = words_2.split(', ')
        logins.append(word_2[0])
        break
    logins.append(stroki[0])
    logins.append(stroki[3])

login = '.'.join(logins).split('\n.')


dic = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
       'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
       'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
       'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
       'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
       'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'yi',
       'э': 'e', 'ю': 'yu', 'я': 'ya'}


def tr(x):
    t = ''
    for i in x:
        t += dic.get(i.lower(), i.lower()).upper() if i.isupper() else dic.get(i, i)
    return t


login_1 = ('\n'.join(login).lower())


my_file = open('logins.txt', 'w',)
my_file.write(tr(login_1))
my_file.close()










