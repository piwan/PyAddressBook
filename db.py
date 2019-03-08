import mysql.connector

db_name = "contacts"
db_user = "root"
db_password = "Passw0rd"
db_host = "localhost"


def init_db():
    """Initialize Contacts database"""
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INT NOT NULL AUTO_INCREMENT, first_name TEXT, last_name TEXT, street TEXT, city TEXT, country TEXT,
                 phone TEXT, email TEXT, PRIMARY KEY (id))''')
    cursor.close()
    conn.close()


def create_contact(contact):
    """
    CRUD create
    :param contact: to be created
    :return: None
    """
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contacts(id, first_name, last_name, street, city, country, phone, email) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',
                   (contact['id'], contact['first_name'], contact['last_name'], contact['street'], contact['city'],
                    contact['country'],
                    contact['phone'], contact['email']))
    conn.commit()
    cursor.close()
    conn.close()


def list_contacts():
    """
    :return: list of contact dicts
    """
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    result = []
    for row in cursor.fetchall():
        result.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "street": row[3],
            "city": row[4],
            "country": row[5],
            "phone": row[6],
            "email": row[7]
        })
    cursor.close()
    conn.close()

    return result


def get_contact(id):
    """
    :param id: contact.id
    :return: contact dict
    """
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
    row = cursor.fetchone()
    if row:
        result = {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "street": row[3],
            "city": row[4],
            "country": row[5],
            "phone": row[6],
            "email": row[7]
        }
    else:
        raise ContactNotFound(id)
    conn.close()

    return result


def update_contact(contact):
    """
    :param contact: object to be updated
    :return: None
    """
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts "
                   "SET first_name=%s, last_name=%s, street=%s, city=%s, country=%s, phone=%s, email=%s "
                   "WHERE id=%s",
                   (contact['first_name'], contact['last_name'], contact['street'], contact['city'], contact['country'],
                    contact['phone'], contact['email'], contact['id']))
    cursor.close()
    conn.commit()
    conn.close()


def delete_contact(id):
    """
    :param id: contact identifier
    :return: None
    """
    conn = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    cursor.close()
    conn.commit()
    conn.close()


class ContactNotFound(Exception):
    """Exception raised when BAN was not found in the DB"""

    def __init__(self, ban):
        super().__init__("Account {} not found".format(ban))
