tasks = []
while True:
  print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
  choice = input("Enter choice: ")
  if choice == "1":
    tasks.append(input("Enter task: "))
  elif choice == "2":
    for i, t in enumerate(tasks, 1):
      print(i, t)
  elif choice == "3":
    n = int(input("Task number: "))
    if 0 < n <= len(tasks):
      tasks.pop(n-1)
    elif choice == "4":
      break
    else:
      print("Invalid choice")
