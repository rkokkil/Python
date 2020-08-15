class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def raise_amount(self):
        # return self.pay * self.raise_amt
        return self.pay * Employee.raise_amt

    def __str__(self):
        return 'first - {}, last - {}, email - {}, pay - {}'.format(self.first, self.last, self.email, self.pay)

class Developer(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def raise_amount(self):
        return self.pay * Developer.raise_amt

    def __str__(self):
        return '{}, prog_lang - {}'.format(super().__str__(), self.prog_lang)


class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def print_employees(self):
        for emp in self.employees:
            print(emp)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def raise_amount(self):
        return self.pay * Manager.raise_amt


dev = Developer('Rambabu', 'Kokkiligadda', 10000, 'Python')
dev2 = Developer('Ram', 'K', 5000, 'Java')
dev3 = Developer('Haribabu', 'K', 12000, 'Go')
"""
print(dev)
print(dev.raise_amount())
"""
# print(help(dev))
# print(dev.__dict__)
# print(dev.__weakref__)
# print(dev.prog_lang)
# mgr = Manager('Mohan', 'Kokkiligadda', 20000, employees=[dev])
mgr = Manager('Mohan', 'Kokkiligadda', 20000, [dev, dev2])
print(mgr)
# print(mgr.raise_amount())
print()
mgr.print_employees()
print()
mgr.add_emp(dev3)
mgr.print_employees()
print()
mgr.remove_emp(dev2)
mgr.print_employees()

