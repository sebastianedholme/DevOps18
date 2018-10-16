from tkinter import *
from tkinter.ttk import *
import pymysql

class Application(Frame):
    """
    This is the main application window
    """
    def __init__(self, master=None):
        super().__init__(master)

        # Styling
        s = Style()
        s.configure("BW.TLabel", foreground="", background="gray")

        # The main window
        self.mainframe = Frame(self.master, padding="12 12 12 12", style="BW.TLabel") # Paddingen mot root
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        #self.login_window()

        # Main menu
        menu = Menu(master)
        master.config(menu=menu) # Konfiguera meny i root fönstret

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        new = Menu(file_menu)
        file_menu.add_cascade(label="Database connections", menu=new)

        new.add_command(label="New connection", command=DbSettingsWindow)

        file_menu.add_separator()
        file_menu.add_command(label="Login", command=LoginWindow) # Creates new login window object
        file_menu.add_command(label="Exit", command=self.master.quit) # Make an exit


    def donothing(self):
        pass

    def welcome_screen(self):
        pass

class DbSettingsWindow(Frame):
    """
    Window for Database settings
    """
    def __init__(self, master=None):
        super().__init__(master)

        # Labels
        self.label_host = Label(self, text="Host")
        self.label_user = Label(self, text="User")
        self.label_passwd = Label(self, text="Password")
        self.label_db = Label(self, text="Databse")

        # Entries
        self.entry_host = Entry(self)
        self.entry_user = Entry(self)
        self.entry_passwd = Entry(self, show="*")
        self.entry_db = Entry(self)

        # Grid Labels
        self.label_host.grid(row=0, sticky=E)
        self.label_user.grid(row=1, sticky=E)
        self.label_passwd.grid(row=2, sticky=E)
        self.label_db.grid(row=3, sticky=E)

        # Grid Entries
        self.entry_host.grid(row=0, column=1)
        self.entry_user.grid(row=1, column=1)
        self.entry_passwd.grid(row=2, column=1)
        self.entry_db.grid(row=3, column=1)

        # Buttons
        self.connect_btn = Button(self, text=("Connect"), command=self.connect_db)
        self.connect_btn.grid(row=4, column=1, columnspan=2, sticky=W)

        #self.disconnect_btn = Button(self, text=("Disconnect"), command=self.disconnect_db)
        #self.disconnect_btn.grid(row=4, column=2, columnspan=2, sticky=W)

        self.grid()

    def connect_db(self):
        host = self.entry_host.get()
        user = self.entry_user.get()
        passwd = self.entry_passwd.get()
        db_name = self.entry_db.get()

        with MySQLConnector(host, user, passwd, db_name) as db:
            if db:
                print("Connected")
            else:
                print("Nope")

    #def disconnect_db(self):
        #"""
        #Closes the db connection
        #"""
        #self.db.close_connection()

class LoginWindow(Frame):
    """
    This is a login window
    """

    def __init__(self, master=None):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)

        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.login_btn = Button(self, text="Login", command=self._login_btn_clicked)
        self.login_btn.grid(columnspan=2)

        self.quit_login_btn = Button(self, text="Exit", command=quit)
        self.quit_login_btn.grid(row=3, columnspan=2)

        self.grid()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()


        # For now just print
        print(username)
        print(password)

class MySQLConnector:
    """
    My databse connector
    """

    def __init__(self, hostname, user_name, passwd, database):
        self._connection = pymysql.connect(host=hostname,
                                          user=user_name,
                                          passwd=passwd,
                                          db=database,
                                          cursorclass=pymysql.cursors.DictCursor)

        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Makes it so that every time i exit out from a with it closes the db connection
        """
        self.connection.close()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor


def main():
    root = Tk()
    root.geometry("400x400")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
