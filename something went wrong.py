#metoda na wyjątki/błedy programu/kodu
'''

try:
    print(10 + [False])
except:
        print('Błąd 001: dodawanie do 10 stringa')

#metoda na wyjątki/błedy programu/kodu
try:
    name = input('Enter your name')
    year_born = int(input('Year you were born:'))
    age = 2022 - year_born
    print(f'You are {name}. And your age is {age}')
except TypeError: #Blad typu
    print('Błąd Typu')
except ValueError: #błąd wartosci
    print('Błąd wartości')
except ZeroDivisionError: #błąd dzielenia przez zero
    print('Błąd dzielenia przez zero')     
else:
    print('Jesli try zadziała odpalę się')    
finally:
       print('Ten tekst pod koniec zawsze się wyswietla')
'''


from xml.dom.minidom import Element


print('#########################################################################')


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']


print('#########################################################################')


numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
x, *y, z, w= numbers
print('wartosc x: ', x)
print('wartosc y: ', y)
print('wartosc z: ', z)
print('wartosc w: ', w)


print('#########################################################################')


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


print('#########################################################################')


def sum_all(*args):
    s = 0 # 0 dla + i - /  1 dla * i /
    for element in args:
        s += element    # + = dodawanie, - = odejmowanie, * = mnożenie, / = dzielenie
    return s
print(sum_all(5,6,2,65,3,5,3,6,))             # <--- suma tych liczb to 95
print(sum_all(1, 2, 3, 4, 5, 6, 7))              # <--- suma tych liczn to 28


print('#########################################################################')


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]  # bez gwaiazdek listy są nie wypakowane
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]


print('#########################################################################')


country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']



print('#########################################################################')


fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):            #na elementach 2 list jednoczesnie
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


print('#########################################################################')


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
one, *middle, last = names
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
*y, es, ru= names
print('wartosc es: ', es)
print('wartosc y: ', y)
print('wartosc ru: ', ru)


print('#########################################################################')

'''
def sum_all1(*args):
    suma = ''
    for element in args:
        suma += element
        suma += ' '
    return suma

year_born = input('Year you were born: ')  
name = input('Enter your name: ')
country = input('Enter your country: ')
city = input('Enter your city: ')
age = input('Enter your age: ')

print(sum_all1(year_born, name, country, city, age)).split(' ')) '''


print('#########################################################################')

'''
def sum_all1(*args):
    suma = []
    for element in args:
        suma.append (element)
    return suma

year_born = input('Year you were born: ')  
name = input('Enter your name: ')
country = input('Enter your country: ')
city = input('Enter your city: ')
age = input('Enter your age: ')

print(sum_all1(year_born, name, country, city, age))#.split(' '))'''