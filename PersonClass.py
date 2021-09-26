class Person:

    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def print_person(self):
        return self.__name, self.__address, self.__phone_number


class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, on_date):
        Person.__init__(self, name, address, phone_number)

        self.__cust_number = cust_number
        self.__on_list = on_list

    def print_person(self):
        person.print_person(self)
        print('Customer Number:', self.__customer_number)
        if self.
