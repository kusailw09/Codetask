contacts = {}

while True:
  print("\n1. Add 2. Delete 3. Search 4. Exit")
  choice = input("Choose: ")

  if choice == "1":
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    print("Contact added")
  elif choice == "2":
    name = input("Enter name to delete: ")
    if name in contacts:
      del contacts[name]
      print("Contact deleted")
    else:
      print("Not found")
    elif choice == "3":
      name = input("Enter name to search: ")
      print("Phone:", contacts.get(name,"Not found"))
  elif choice == "4":
break
else:
print("Invalid choice")
