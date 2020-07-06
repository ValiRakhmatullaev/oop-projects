# Клиент выбирает необходимый препарат из списка доступных.
# Заполнять форму заказа, указывая количество и дозировку.
# Клиент оплачивает заказ. Фармацевт управляет списком препаратов.
# Часть  препаратов требуют электронного рецепта, которые можно значит клиенту только врач.
# Клиент может сделать запрос врачу на продление рецепта

medecines = {'1': '  trimol',
             '2': ' paracetamol',
             '3': 'spirulin',
             '4': 'insulin',
             '5': ' danabol'}


class Client:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def order(self, medecine):
        return f'your order is{medecine}'

    def Order_form(self):
        return f'your quantity is {kol}'

    def __str__(self):
        return f'Client  {self.name}, age - {self.age}, phone number - {self.phone_number}'


pac = Client('Jone', 78, 333204957)
print(pac)
zak = input('choose the medecine !: '
            '1 - trimol '
            '2 - paracetamol '
            '3 - spirulin '
            '4 - insulin '
            '5 - danabol ')

print(pac.order(medecines[zak]))

kol = input('choose the quantity! ')
print(pac.Order_form())
print(pac, 'your order =', medecines[zak], 'and your quantity is', kol)


class Pharmacist:
    def __init__(self, name):
        self.name = name

    def add(self):
        return f'the madicine {a} is  added '

    def delete(self, medecines):
        return f'you delete the {b}'

    def __str__(self):
        return f'pharmacist name is {self.name}'


vali = Pharmacist("Vali")
print(vali)

a = input('add the medecine')
print(vali.add())
b = input('what medicine do you want to delete')
print(vali.delete(medecines))


class Doc:
    def __init__(self, name, surname, specialty):
        self.name = name
        self.surname = surname
        self.specialty = specialty

    def recept(self):
        return f' I confirm your recept '

    def __str__(self):
        return f'doctor - {self.name} {self.surname} , specialty is {self.specialty}'


dc = Doc('Dc.Conor', 'Mcgregor', 'Urolog')
print(dc)
print(dc.recept())
print(medecines)

# Pharmacist
# Doctor
# class Pharmacy:
#
#     def __init__(self, drug_name, price, quantity):
#         # print('viberite lekarstvo')
#         self.drug_name = drug_name
#         self.price = price
#         self.quantity = quantity
#
#     drugs = input('viberite lekarsto: ' \
#                   '1- trimol ' \
#                   '2-paracetamol ' \
#                   '3-validol ')
#
#     if drugs == 1:
#         print('trimol')
#     elif drugs == 2:
#         print('trimol')
#     elif drugs == 3:
#         print('trimol')
#
#     # else:
#     #     print('vi ne vibrali lekarstvo ')
#
#     def __str__(self):
#         return f'GrandFrarm {self.drug_name} {self.price} {self.quantity}'
#
# #
# # def generate_pacient(self):
# #     drug_name, price, quantity = self.split(' ')
# #     drugs = input(), input(), input()
# #
# # # pacients = []
# # #
# # while True:
# #     self = ('vvedite nazvanie preparata')
# #     pacients = generate_pacient(self)
# #
# # #
# # pacient = GrandFarm(input('vashi tabletki''-'))
# # print(pacient)
# #
# # # class SuperClient(GrandFarm):
# # #     def __init__(self, name, surname, doctor, drug_name, price, quantity):
# # #         super().__init__(drug_name, price, quantity)
# # #         self.name = name
# # #         self.surname = surname
# # #         self.doctor = doctor
#
# # class Pharmacy:
# #
# #     def __init__(self, drug_name, price, quantity):
# #         self.drug_name = drug_name
# #         self.price = price
# #         self.quantity = quantity
# #
# #     def voice(self):
# #         return 'undefined voice'
# #
# #     def defecate(self):
# #         return 'defined'
# #
# #     def eat(self, value):
# #         self.price += value
# #
# #     def __str__(self):
# #         return f'vali {self.drug_name} {self.price} {self.quantity} '
# #
# #
# # pacient = Pharmacy('trimol', 15, 4500)
# # print(pacient)
# # print(pacient.price)
# # pacient.eat(20)
# # print(pacient.price)
# # print(pacient.defecate())
# # print(pacient.voice())
