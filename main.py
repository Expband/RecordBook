from Manager import Manager
from flask import request, Flask, request, send_from_directory, make_response, jsonify

app = Flask(__name__)
manager = Manager


@app.route('/')
def root():
    return send_from_directory('templates', 'index.html')


@app.route('/templates/users.html')
def return_users_page():
    return send_from_directory('templates', 'users.html')


@app.route('/templates/user_by_id.html')
def return_finding_page():
    return send_from_directory('templates', 'user_by_id.html')


@app.route('/all')
def call_all_users():
    return manager.get_all_members()


@app.route('/by-id')
def call_get_one_user():
    return manager.get_member_by_id(int(request.args.get('id')))


@app.route('/add', methods=['POST'])
def call_add_user():
    data = request.get_json()
    try:
        manager.insert_member_into_json(data['firstname'], data['lastname'], data['phone'], data['address'])
        response = make_response(jsonify({'message': 'request done'}), 200)
        return response
    except:
        response = make_response(jsonify({'message': 'request failed'}), 400)
        return response


if __name__ == '__main__':
    app.run(debug=True)