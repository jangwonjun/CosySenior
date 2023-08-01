from modules.database import *
from flask_login import UserMixin
from abc import *

class RDMS(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def get_one_raw(param_name, identifier, destination) -> list:
        db = get_db()
        db.execute(
            f"SELECT * FROM `{destination}` WHERE {param_name} = %s LIMIT 1", (
                identifier, )
        )
        value = db.fetchone()
        return value

    @staticmethod
    def get_all_raw(param_name, identifier, destination) -> list:
        db = get_db()

        db.execute(
            f"SELECT * FROM `{destination}` WHERE {param_name} = %s", (
                identifier, )
        )
        # values = db.fetchone()
        values = db.fetchall()
        return values

    @abstractmethod
    def get(identifier):
        pass

    @staticmethod
    def delete(param_name, identifier, destination):
        db = get_db()
        db.execute(
            f"DELETE FROM `{destination}` WHERE `{param_name}` = %s",
            (identifier),
        )
        db.commit()


class User(UserMixin, RDMS):
    TABLE_NAME = 'noin_user'

    def __init__(self, id, email, password, name, phone_number):
        self.id = int(id)
        self.email = email
        self.name = name
        self.password = password
        self.phone_number = phone_number

    def __repr__(self):
        return f"User_{self.id}({self.name}: email={self.email})"

    @staticmethod
    def get(user_id):
        user = User.get_one_raw('id', user_id, User.TABLE_NAME)
        if not user:
            return None
        print(user)
        return User(*user)
    
    @staticmethod
    def find_id_by_email(email):
        user = User.get_one_raw('email', email, User.TABLE_NAME)
        if not user:
            return None
        print(user)
        return User(*user)
    
    @staticmethod
    def create(email, password, name, phone_number):
        db = get_db()
        db.execute(f"INSERT INTO {User.TABLE_NAME}(email, password, name, phone_number) VALUES(?, ?, ?, ?);", (email, password, name, phone_number))
        commit()
        return User.find_id_by_email(email)