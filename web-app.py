from flask import abort, Flask, render_template

app = Flask(__name__)

test_users = [
    {
        "id": 1,
        "first_name": "Jackson",
        "last_name": "Arnold",
        "street": "803 Vitae, Ave",
        "city": "Arbre",
        "country": "Guatemala",
        "phone": "(01799) 90643",
        "email": "elit.Curabitur.sed@necleo.net"
    },
    {
        "id": 2,
        "first_name": "Judith",
        "last_name": "Pearson",
        "street": "128-9687 Donec Street",
        "city": "Virginal-Samme",
        "country": "United States",
        "phone": "(016977) 3415",
        "email": "nisl.Maecenas.malesuada@Aeneaneuismod.net"
    },
    {
        "id": 3,
        "first_name": "Emery",
        "last_name": "Buck",
        "street": "3198 In Street",
        "city": "Sarreguemines",
        "country": "Guatemala",
        "phone": "0845 46 42",
        "email": "semper@neccursus.edu"
    },
    {
        "id": 4,
        "first_name": "Sylvester",
        "last_name": "Wilkins",
        "street": "689-6848 Viverra. Av.",
        "city": "Whittlesey",
        "country": "Libya",
        "phone": "0800 569 3215",
        "email": "orci.luctus@ultriciesadipiscingenim.co.uk"
    },
]


@app.route('/')
@app.route('/users/')
def users_list():
    """Render page with the list of users"""
    return render_template('users-list.html', users=test_users)


@app.route('/users/<int:user_id>')
def user_details(user_id):
    """Render page with details of a single user"""
    try:
        user = next(user for user in test_users if user["id"] == user_id)
        return render_template('users-details.html', user=user)
    except StopIteration:
        abort(404, "User with id {} doesn't exist".format(user_id))


@app.errorhandler(404)
def page_not_found(message):
    """Render error page"""
    return render_template('page_not_found.html', message=message), 404
