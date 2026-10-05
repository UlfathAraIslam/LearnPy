class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def give_raise(self, amount):
        if amount <= 0:
            print("Invalid raise amount: must be positive.")
            return
        self.__salary += amount
        print(f"Raise applied. New salary: ¥{self.__salary}")

    def view_payslip(self):
        print(f"Payslip - {self.name}: ¥{self.__salary}")


def main():
    name = input("Employee name: ")
    salary = int(input("Starting salary: "))
    emp = Employee(name, salary)

    while True:
        amount = int(input("Raise amount (0 to finish): "))
        if amount == 0:
            break
        emp.give_raise(amount)

    emp.view_payslip()


if __name__ == "__main__":
    main()
