
answer = int(input("""
    Введите одну из команд: 
               1. Создать(открыть файл)
               2. Внести изменения в файл
               3. Очистить файл
"""))

if answer == 1:
    fileName = input("Введите название файла")
    with open(fileName, 'r') as file:
        print(file.read())

elif answer == 2:
    fileName = input("Введите название файла")
    text = input("Введите текст файла: ")
    with open(fileName, "w") as file:
        file.write(text)  

elif answer == 3:
    fileName = input("Введите название файла")  
    with open(fileName, "w") as file:
        file.write("")

else:
    print("Команды не существует, повторите выьор.")                              




