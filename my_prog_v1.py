HELP = """
help - начнает печатать справку по программу
add - добавить задачу в список ( название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""
#Cоздаем словарь
tasks = {
  
}

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "add":
    date = input("Введите дату для добавления задачи: ")
    
    task = input("Введите название задачи : " )
    if date in tasks:
      #Дата есть в словаре
      #Добавляем в список задачу
      task[date].append(task)
    else:
     # Если даты нет в словаре, то мы создаем пустой список, а затем добавляем запись
      tasks[date] = []
      tasks[date].append(task)
    print("Задача ", task, "добавлена на дату ", date)

  elif command == "show":
    print(tasks)
  else:
    print("Неизвестная команда")
    break
print("Have a nice day")