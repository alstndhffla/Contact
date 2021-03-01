class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("----------------------")
        print("Name: ", self.name)
        print("Phone_number: ", self.phone_number)
        print("E_mail: ", self.e_mail)
        print("Address: ", self.addr)
        print("----------------------")


def set_contact():
    name = input("Name: ")
    phone_number = input("Phone_number: ")
    e_mail = input("E_mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    # 리턴 시키면 윗 줄 contact 변수를 사용하는 거라 회색(비활성화) 사라짐
    return contact 


def print_menu():
    print("##########################")
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    print("##########################")
    menu = input("메뉴 선택: ")
    print("##########################")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def store_contact(contact_list):
    f = open("contact_db.txt", "wt")    # 쓰기
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()


def load_contact(contact_list):
    f = open("contact_db.txt", "rt")    # 읽기
    lines = f.readlines()
    num = len(lines)/4
    num = int(num)  # 실수형이라 int 로 변환

    for i in range(num):
        name = lines[4*i].rstrip('\n')  # i 가 0부터 시작해 0 줄
        phone = lines[4*i+1].rstrip('\n')   # 한 줄
        email = lines[4*i+2].rstrip('\n')   # 두 줄
        addr = lines[4*i+3].rstrip('\n')    # 세 줄
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()


def run():
    contact_list = []   # 데이터를 집어넣을 리스트 선언
    load_contact(contact_list)  # 스크립트 실행시 기존 데이터파일을 읽어온다
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        if menu == 2:
            print_contact(contact_list)
        if menu == 3:
            name = input("Which name do want to delete?: ")
            delete_contact(contact_list, name)
        if menu == 4:
            store_contact(contact_list)
            break


if __name__ == "__main__":
    run()
