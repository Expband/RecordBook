import json


class Manager:
    @staticmethod
    def read_json() -> dict:
        with open('members.json', 'r') as file:
            members_json = json.load(file)
            return members_json

    @staticmethod
    def write_json(json_data: dict) -> None:
        with open('members.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

    @staticmethod
    def get_members_lenght() -> int:
        json_data = Manager.read_json()
        return len(json_data['members'])

    @staticmethod
    def insert_member_into_json(firstname: str, lastname: str,  phone: str, adress: str) -> None:
        json_data = Manager.read_json()
        json_data['members'].append({'id': Manager.get_members_lenght(),
                                   'firstname': firstname, 'lastname': lastname, 'phone': phone, 'adress': adress})
        Manager.write_json(json_data)

    @staticmethod
    def get_all_members():
        json_data = Manager.read_json()
        return json_data['members']

    @staticmethod
    def get_member_by_id(id: int) -> dict:
        json_data = Manager.read_json()
        for user in json_data['members']:
            if user['id'] == id:
                return user
