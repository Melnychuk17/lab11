# Вапиант 6
# Дан текстовий файл f. Видалити з нього останній рядок, результат записати у
# файл g.
# Мельничук Олена 122В
f=open('f.txt', 'w')
f.write("Love\n is\n never\n wrong")
f.close()
with open('f.txt') as f:
    text = f.read()  # читаем файл
    items = text.split()  # переобразовуем в список
with open('g.txt', mode='w') as g:
    items = items[:-1]  # удаляем последний элемент
    text = '\n'.join(items)
    g.write(text)  # получаем новый файл



