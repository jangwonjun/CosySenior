from modules.database import *
from flask_login import UserMixin
from abc import *
import time


def create(table_name, **kwargs):
    db = get_db()
    query = f"INSERT INTO {table_name}({', '.join(kwargs.keys())}) VALUES({', '.join(['%s']*len(kwargs))});"
    print(query)
    db.execute(query, tuple(
        kwargs.values()))
    commit()


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

    def __init__(self, id, email, password, name, phone_number, help_phone_number):
        self.id = int(id)
        self.email = email
        self.name = name
        self.password = password
        self.phone_number = phone_number
        self.help_phone_number = help_phone_number

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
    def create(email, password, name, phone_number, help_phone_number):
        create(User.TABLE_NAME, email=email, password=password, name=name,
               phone_number=phone_number, help_phone_number=help_phone_number)
        return User.find_id_by_email(email)


class CallLog(RDMS):
    TABLE_NAME = 'send_log'

    def __init__(self, user_id, send_time):
        self.user_id = int(user_id)
        self.send_time = time.strptime(send_time, "%H:%M:%S")

    @staticmethod
    def get(user_id):
        calls = CallLog.get_all_raw('user_id', user_id, CallLog.TABLE_NAME)
        if calls:
            return None
        print(calls)
        return [CallLog(*call) for call in calls]

    @staticmethod
    def create(user_id, ):
        db = get_db()
        db.execute(f"INSERT INTO {CallLog.TABLE_NAME}(email, password, name, phone_number, help_phone_number) VALUES(%s, %s, %s, %s, %s);", (
            email, password, name, phone_number, help_phone_number))
        commit()
        return User.find_id_by_email(email)
