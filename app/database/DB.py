import sqlite3


class DB:
    def __init__(self, db_name):
        self.__db_url: str = db_name
        self.__conn: sqlite3.Connection = None
        self.__cur: sqlite3.Cursor = None

    def connect(self) -> bool:
        """
        establish connection with sqlite3 database -> True
        in case of error print it -> False
        """
        if self.__conn == None:
            try:
                conn = sqlite3.connect(self.__db_url)  # create connection
                cur = conn.cursor()  # create cursor
                self.__conn = conn  # set connection as self.__conn
                self.__cur = cur  # set cursor as self.__cur
                return True
            except sqlite3.OperationalError as e:  # handle error
                print(f"Connection to DB error: {e}")
                return False

    def close(self) -> bool:
        """
        close connection to sqlite3 database
        """
        if self.__conn:
            self.__conn.close()
            self.__cur = None
            self.__conn = None

    def execute_script(self, sql_script: str) -> bool:
        if not self.__conn:
            print("connection error")
            return False
        try:
            self.__cur.executescript(sql_script)
            self.__conn.commit()
            return True
        except sqlite3.OperationalError as e:
            print(f"SCRIPT error: {e}")
            return False

    def _execute(self, sql_str: str, params: tuple[any, ...] = ()) -> bool:
        if not self.__conn:
            print("connection error")
            return False
        try:
            self.__cur.execute(sql_str, params)
            self.__conn.commit()
            return True
        except sqlite3.OperationalError as e:
            print(e)
            return False

    def read(self, sql_str: str, params: tuple[any, ...] = ()) -> list[any]:
        """
        the function receives arguments for executing READ request and executes it -> [result]
        in case of error -> []
        """
        if not self.__conn:
            print("connection error")
            return []
        try:
            self.__cur.execute(sql_str, params)
            return self.__cur.fetchall()
        except sqlite3.OperationalError as e:
            print(f"READ error: {e}")
            return []

    def create(self, sql_str: str, params: tuple[any, ...] = ()) -> bool:
        """
        the function receives arguments for executing CREATE request and executes it -> true
        in case of error -> false
        """
        return self._execute(sql_str, params)

    def update(self, sql_str: str, params: tuple[any, ...] = ()) -> bool:
        """
        the function receives arguments for executing UPDATE request and executes it -> true
        in case of error -> false
        """
        return self._execute(sql_str, params)


db = DB("./DB.sql")


def setup_database():
    if not db.connect():
        print("connection error in setup_database")
        return False
    try:
        sql_create_users_table = """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                join_date TIMESTAMP,
                is_generating INTEGER DEFAULT 0,
                is_last_image_unlocked INTEGER DEFAULT 1,
                total INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS generations (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                image_url TEXT,
                prompt TEXT,
                is_resolved INTEGER
            );
            """
        success = db.execute_script(sql_create_users_table)
        if success:
            print(" tables created")
        else:
            print("error while creating tables")
        return success
    except sqlite3.OperationalError as e:
        print(e)
        return False
