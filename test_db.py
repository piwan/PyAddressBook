from db import init_db, list_contacts, get_contact, update_contact, delete_contact, ContactNotFound, create_contact

c1 = {
    "id": 1000,
    "first_name": "Jackson",
    "last_name": "Arnold",
    "street": "803 Vitae, Ave",
    "city": "Arbre",
    "country": "Guatemala",
    "phone": "(01799) 90643",
    "email": "elit.Curabitur.sed@necleo.net"
}

init_db()
print(list_contacts())
try:
    print(get_contact(c1['id']))
except ContactNotFound:
    print("The exception was raised, as expected")

create_contact(c1)
c1 = get_contact(c1['id'])
print(list_contacts())

c1['phone'] = "(0123) 123 123 123"
c1['last_name'] = "Smith"
update_contact(c1)

print(list_contacts())

delete_contact(c1['id'])
try:
    print(get_contact(c1['id']))
except ContactNotFound:
    print("The exception was raised, as expected")
