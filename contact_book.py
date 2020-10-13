def save_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    file = open("contacts.txt", 'a')
    file.write(name + ":" + phone + "\n")
    file.close()
    print('Contact Saved',end='\n\n')

def fetch_contact():
    opt = input("Search by name(n) or phone number?(p): ")    
    if opt.lower()=='n':
        name = input("Enter name: ")
        search_by_name(name)
    else:
        phone = input("Enter phone: ")
        search_by_phone(phone)    

def search_by_name(name):
    contact_list = open('contacts.txt').readlines()
    for i in contact_list:
        name_, num_ = i.split(":")
        if name_ == name:
            print(num_)
            return
    print("Contact not found.")    
    

def search_by_phone(num):
    contact_list = open('contacts.txt').readlines()
    for i in contact_list:
        name_, num_ = i.split(":")
        if num_.strip()== num:
            print(name_,end="\n\n")
            return
    print("Contact not found.")    


while True:
    save_or_read = input("Do you want to fetch(f) or save(s) a contact(f/s)?: ")
    if save_or_read.lower() == 's':
        save_contact()
    else:
        fetch_contact()


