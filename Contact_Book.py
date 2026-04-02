def contact_book():
    contact_list = {}
    add_contact = int(input("Enter how many contact you want to add: "))
    for i in range(add_contact):
        name = input("Enter Name: ")
        phone_num = input("Enter PH No.: ")
        contact_list[name]= phone_num
    print("-----Contact Book-----")
    for name, phone in contact_list.items():
        print(f"{name}: {phone}")
        
    # Searching a name in contact book
    search_name = input("Enter a name to search: ")
    if search_name in contact_list:
        print(f"{search_name}'s number is {contact_list[search_name]}")
    else:
        print("Contact not found.")     
contact_book()
