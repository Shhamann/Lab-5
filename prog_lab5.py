# вариант 4

import re

def task1(text):
    words_with_dash = set(re.findall(r"[а-яА-Я]+-[а-яА-Я]+", text))
    inf_in_brackets = set(re.findall(r"\(.+?\)", text))
    return words_with_dash, inf_in_brackets

def task2(data):
    links = set(re.findall(r"https://\S+.com/\S+(?=\")", data))
    return links

def task3(text):
    num = re.findall(r'(?<=\s)\d+(?=\s)', text)
    surname = re.findall(r'[A-Z][a-z]+', text)
    email = re.findall(r'\S+@\S+', text)
    date = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    link = re.findall(r'(?<=\s)\S+://\S+(?=\s)', text)
    with open('output.csv', 'a') as file_table:
        file_table.write('ID;фамилия;электронная почта;дата регистрации;сайт\n')
        for i in range(len(num)):
            s = f"{num[i]};{surname[i]};{email[i]};{date[i]};{link[i]}\n"
            file_table.write(s)

if __name__ == '__main__':
    text = ' '.join(open('task1-ru.txt', encoding='UTF-8').readlines())
    result1 = task1(text)
    print("Ответ на задание 1:")
    [print(i) for i in result1[0]]
    [print(i) for i in result1[1]]

    data = ''.join(open('task2.html', encoding='UTF-8').readlines())
    result2 = task2(data)
    print("\n\nОтвет на задание 3:")
    [print(i) for i in result2]

    table = ' '.join(open('task3.txt', encoding='UTF-8').readlines())
    task3(table)
    
    
    