"""
This is my MySQLConnector class
"""

class MySQLConnector():
    """
    My databse connector
    Use the save settings in DB from GUI to have DB to connect to
    """
    HOST = 'localhost'
    USER = 'recordbox'
    PASSWD = 'recordbox'
    DB = 'recordbox'

    def __init__(self):
        self._connection = pymysql.connect(host=self.HOST,
                                           user=self.USER,
                                           passwd=self.PASSWD,
                                           db=self.DB,
                                           cursorclass=pymysql.cursors.DictCursor)

        self._cursor = self._connection.cursor ()

    def __enter__(self):
        """
        This makes it possible to use a with statement with the SQL connectio
        without having to create the object first. The exit will make sure
        the connection is closed.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Makes it so that every time i exit out from a with it closes the db connection
        """
        self.connection.close()

    @property
    def connection(self):
        """
        Simply returns itself so i can call, conn.connection.commit and so on
        """
        return self._connection

    @property
    def cursor(self):
        """
        The cursor object
        """
        return self._cursor

    @property
    def db_info(self):
        return self.db_info

    @db_info.setter
    def db_info(self, *arg):
        self.db_info = [*arg]
