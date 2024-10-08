class PhoneBook:

    def __init__(self):
        self.book = [0 for i in range(10 ** 7)]

    def add(self, data):
        phone = int(data[0])
        name = data[1]
        self.book[phone] = [phone, name]

    def find(self, phone):
        phone = int(phone)
        if self.book[phone] == 0:
            return print('not found')
        else:
            return print(self.book[phone][1])

    def delete(self, phone):
        phone = int(phone)
        self.book[phone] = 0


def main():
    n = int(input())
    com = []
    Book = PhoneBook()
    for i in range(n):
        com.append(input().split())

    for i in range(len(com)):
        if com[i][0] == 'add':
            Book.add(com[i][1:])
        elif com[i][0] == 'find':
            Book.find(com[i][1])
        elif com[i][0] == 'del':
            Book.delete(com[i][1])


main()
