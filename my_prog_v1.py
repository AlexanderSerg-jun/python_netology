HELP = """
help - начнает печатать справку по программу
add - добавить задачу в список ( название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""
#Cоздаем список
tasks = []

command = input("Введите команду: ")
if command == "help":
    print(HELP)
elif command == "add":
    task = input("Введите название задачи : " )
    tasks.append(task)
    print("Задача добавлена")

elif command == "show":
    print(tasks)
else:
    print("Неизвестная команда")