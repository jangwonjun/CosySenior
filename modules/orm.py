from modules.database import *
from flask_login import UserMixin
from abc import *
import time


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
        return User(*user)

    @staticmethod
    def find_id_by_email(email):
        user = User.get_one_raw('email', email, User.TABLE_NAME)
        if not user:
            return None
        return User(*user)

    @staticmethod
    def create(email, password, name, phone_number, help_phone_number):
        create_column(User.TABLE_NAME, email=email, password=password, name=name,
                      phone_number=phone_number, help_phone_number=help_phone_number)
        return User.find_id_by_email(email)


class CallLog(RDMS):
    TABLE_NAME = 'send_log'

    def __init__(self, user_id, send_time: str):
        self.user_id = int(user_id)
        self.send_time = time.strptime(send_time, "%H:%M:%S")

    @staticmethod
    def get_phone_by_call_time(time_value):
        conn, cur = get_db_direct()
        cur.execute(f"USE {SQL.DB_NAME}")
        query = f"""
            SELECT noin_user.phone_number
            FROM send_log LEFT JOIN noin_user 
            ON noin_user.id = send_log.user_id
            WHERE send_time=%s;
        """
        calls = search_all(query, (time_value, ), lambda: cur)

        if not calls:
            return tuple()
        return calls

    @staticmethod
    def create(user_id, send_time: str):
        create_column(CallLog.TABLE_NAME, user_id=user_id, send_time=send_time)
