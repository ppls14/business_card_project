#                                                   |Wizytówki|
# 1.Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna 
#   przechowywać podstawowe dane kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej 
#   klasy (BusinessContact) rozszerz klasę bazową o przechowywanie informacji związanych z pracą danej osoby 
#   – stanowisko, nazwa firmy, telefon służbowy.
# 2.Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci 
#   “Wybieram numer +48 123456789 i dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy 
#   numer telefonu, a wizytówka bazowa prywatny.
# 3.Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska 
#   danej osoby.
# 4.Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje 
#   dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.
#-----------------------------------------------------------------------------------------------------------------------
# Biblioteka 'faker' do generowania danych wizytówek
from faker import Faker
fake = Faker()
#-----------------------------------------------------------------------------------------------------------------------
# Definicja klasy 'BaseContact'
class BaseContact: 
    # Domyślny konstruktor
    def __init__(self, name, last_name, priv_phone, email):
        # Powiązanie parametrów z atrybutami 
        self.name = name
        self.last_name = last_name
        self.priv_phone = priv_phone
        self.email = email
    # Metoda '__str__' odpowiadająca za wygląd obiektu klasy 'BaseContact'
    def __str__(self):
        return f"Podstawowe dane kontaktowe:\n{self.name} {self.last_name}\n{self.priv_phone}\n{self.email}\n"
    # Metoda '__rept__' odpowiadająca za to jak obiekt klasy 'BaseContact' przedstawiony jest w interpreterze
    def __repr__(self):
        return f"Interpreter:\nBaseContact(name = {self.name}, last_name = {self.last_name}, priv_phone = {self.priv_phone}, email = {self.email} )\n"
    # Metoda 'contact()' obiektu klasy 'BaseContact' wyświetlająca komunikat
    def contact(self):
        return f"Metoda contact():\nWybieram numer {self.priv_phone} i dzwonię do {self.name} {self.last_name}\n"
    # Dynamiczny atrybut 'label_length' zwraca długość imienia i nazwiska danej osoby
    @property
    def label_length(self):
        print(f"Dynamiczny atrybut label_length:\nSuma znaków imienia i nazwiska wynosi:")
        self._label_length = self.name + self.last_name
        self._label_length = (len(self._label_length) + 1) # + 1 od spacji
        return self._label_length 
#-----------------------------------------------------------------------------------------------------------------------
# Definicja klasy 'BusinessContact' dziedziczącej z klasy 'BaseContact', rozszerzonej o 
# informacje związane z pracą danej osoby - stanowisko, nazwa firmy i telefon służbowy.
class BusinessContact(BaseContact):
    # Domyślny konstruktor
    def __init__(self, occupation, company, business_phone, *args, **kwargs):
        # Odwołanie do klasy 'BaseContact'po której odziedzicza klasa 'BusinessContact'
        super().__init__(*args, **kwargs) 
        # Powiązanie parametrów z atrybutami
        self.occupation = occupation
        self.company = company
        self.business_phone = business_phone
    # Metoda '__str__' odpowiadająca za wygląd obiektu klasy 'BusinessContact'    
    def __str__(self):
        return f"Służbowe dane kontaktowe:\n{self.name} {self.last_name}\n{self.occupation} {self.company}\n{self.business_phone}\n{self.email}\n"
    # Metoda '__rept__' odpowiadająca za to jak obiekt klasy 'BusinessContact' przedstawiony jest w interpreterze
    def __repr__(self):
        return f"Interpreter:\nBusinessContact(name = {self.name}, last_name = {self.last_name}, priv_phone = {self.priv_phone}, email = {self.email}, occupation = {self.occupation}, company = {self.company}, business_phone = {self.business_phone})\n"
    # Metoda 'contact()' obiektu klasy 'BusinessContact' wyświetlająca komunikat
    def contact(self):
        return f"Metoda contact():\nWybieram numer {self.business_phone} i dzwonię do {self.name} {self.last_name}\n"
    # Dynamiczny atrybut 'label_length' zwraca długość imienia i nazwiska danej osoby
    @property  
    def label_length(self):
        return super().label_length
#-----------------------------------------------------------------------------------------------------------------------
# Definicja obiektów dla klasy podstawowej i biznesowej
base_card = BaseContact(name = 'Roksana', last_name = 'Adamczyk', priv_phone = '+48-509-509-509', email = 'RoksanaAdamczyk@armyspy.com')
business_card = BusinessContact(name = 'Roksana', last_name = 'Adamczyk',priv_phone = '+48-509-509-509', email = 'RoksanaAdamczyk@armyspy.com', occupation = 'Copy writer', company = 'Planet Pizza', business_phone = '+48-601-601-601')
#-----------------------------------------------------------------------------------------------------------------------
# Wywołania metod dla obiektów utworzonych na klasach 'BaseContact' i 'BusinessContact'
print(base_card)
print(base_card.__repr__())
print(base_card.contact())
print(base_card.label_length)

print(business_card)
print(business_card.__repr__())
print(business_card.contact())
print(business_card.label_length)
#-----------------------------------------------------------------------------------------------------------------------
# Funkcja 'create_contacts' do generowania losowych wizytówek za pomocą biblioteki 'faker'
def create_contacts(card_type = BaseContact, count = 1):
    # Pusta lista
    contacts = []
    # Pętla tworzy zmienną do której przypisuję obiekt klasy określonej parametrem 'card_type'
    for n in range(0,count):
        contacts.append('card_' + str(n+1))
        if card_type == BaseContact:
            contacts[n] = card_type(name = fake.name(), last_name = fake.last_name(), priv_phone = fake.phone_number(), email = fake.email())
        else:
            contacts[n] = card_type(name = fake.name(), last_name = fake.last_name(), priv_phone = fake.phone_number(), email = fake.email(), occupation = fake.job(), company = fake.company(), business_phone = fake.phone_number())
        return contacts

result = create_contacts(card_type = BusinessContact, count=1)
print(result)