from Ass12.handler import read_file, write_file

def add_member():
    member_id = input("Enter User ID: ")
    name = input("Enter Name: ")

    member_data = f"{member_id},{name}\n"
    write_file("members.txt", member_data)
    print("Member added")

def search_member():
    member_id = input("Enter User ID: ")
    members = read_file("members.txt")
    for member in members:
        if member.startswith(member_id):
            member_id, name = member.strip().split(",")
            print("Member found")
            print("Member User ID:", member_id)
            print("Name:", name)
            return
    print("Member not found")

def display_all_members():
    members = read_file("members.txt")
    if members:
        print(" All Members ")
        for member in members:
            member_id, name = member.strip().split(",")
            print("Member User ID:", member_id)
            print("Name:", name)
            print("********************")
    else:
        print("No members are available")