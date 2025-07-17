import json
def load_contacts():
	try:
		with open("contacts.json","r")as file:
			data = json.load(file)
			return data
	except:
		return {}
def save_contacts(contacts) :
	with open("contacts.json","w")as file:
		json.dump(contacts,file)
def add():
	contacts = load_contacts()	
	name = input("Enter name: ").lower()
	if not name.isalpha():
		print("Enter valid name!Letters only")
		return
	contact = input("Enter phone number: ")
	if not contact.isdigit() or len(contact) != 10 :
		print("Enter valid contact!")
		return
	confirmation = input(f"Confirm save {name}:{contact} (yes/no)").lower().strip()
	if confirmation=="yes":
		contacts[name] = contact
		save_contacts(contacts)
		print("saved successfully!")
	else:
		print("Contact not saved!")
def search():
	search_name = input("Enter name: ")
	contacts = load_contacts()
	if search_name in contacts:
		try:
			with open("contacts.json","r")as file:
				data = json.load(file)
				print(data[(search_name)])
		except:
			print("Error")
		return
	else:
		print("contact not found")
		return
def view():
	try:
		with open("contacts.json","r")as file:
			data = json.load(file)
		print(data)
	except (json.JSONDecodeerror,FileNotFoundError):
		print("No contacts found")
def delete():
	contacts = load_contacts()
	del_name = input("Enter name to delete: ")
	if del_name in contacts:
		confirm = input(f"Delete {del_name}? (yes/no)")
		if confirm == "yes":
			del contacts[del_name]
			save_contacts(contacts)
			print("Contact deleted successfully")
		else:
			print('Contact not deleted')
	else:
		print('contact not found')
while True:
	print("\n1.Add contacts\n2.Search contacts\n3.Delete contact\n4.View all contacts\nUse numbers!")
	option = input("Choose from the above options: ")
	if option == "1":
		add()
	elif option == "2":
		search()
	elif option == "3":
		delete()
	elif option == "4":
		view()
	else:
		print("Enter a valid option!")															