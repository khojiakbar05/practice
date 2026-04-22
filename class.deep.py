''' CLASS DEEP DIVE
       (1) ENCAPSULATION <
       (2) INHERITANCE
       (3) POLYMORRPHISM
'''

print("========== ENCAPSULATION =============")
# Python => public, __private, _protected
'''
C++, JAVA => public & private & protected
PHP, TypeScript => public & private & protected
'''


class Account():
    # Stat
    description = "The Class makes bank accounts"

    # Constructor
    def __init__(self, owner, amount):
        self.__owner = owners
        self.__amount = amount

    # Method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit: ", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw: ", amount)
        self.__amount -= amount

    # Property decorator => Clasimizni ichidagi maxfiy malumotlarni call qilishiiz uchun ishlatamiz
    # getter =>  yani malumotlarni olish uchun ishlatiladi

    @property
    def holder(self):
        return self.__owner

    # setter => malumotlarni ozgartirish uchun ishlatiladi

    @holder.setter
    def holder(self, new_owner):
        print("change_ownership: ", new_owner)
        self.__owner = new_owner

    # bu function holderimizni ozgartirishimizni bir usuli
    def change_ownership(self, new_owner):
        print("change_ownership: ", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-----------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()


# my_account.amount = 1000000
# my_account.owner = "Martin"
# my_account.get_balance()

print("-----------")

# print(my_account.owner)

try:
    result = my_account.__amount
    print("result: ", result)
except Exception as err:
    print("No target state found: ", err)


# Property decorator orqali maxfiy malumotlarni call qilish. STATE sifatida
account_owner = my_account.holder
print("Account_owner Before: ", account_owner)


# . setter orqali maxfiy malumotlarni ozgartirish
my_account.holder = "Martin"


# Maxfiy usulda ozgartirish uchun yozilgan method() functionni call qilish
my_account.change_ownership("Martin")
print("Owner after: ", my_account.holder)
