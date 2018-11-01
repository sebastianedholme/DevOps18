import tkinter as tk
from tkinter import ttk
import pymysql
from PIL import Image, ImageTk

class Application(tk.Frame): # pylint: disable=too-many-ancestors
    """
    This is the main application entry class
    Aso the structure of the application. I pack up all the windows that i use
    """
    def __init__(self, master=None):
        super().__init__(master)

        # Creating menu objects
        self.topmenu = TopMenu(self)
        self.toolbar = ToolBar(self)
        self.statusbar = StatusBar(self)
        self.mainframe = MainFrame(self)
        self.intro_label = tk.Label(self, text=""" Welcome to this simple GUI app.
        To get information from yuor databse, first go to settings and save your DB information.
        You can then fill the treeview with data from your Databse""",
                                    anchor='w', justify="left", wraplength=200)
        # Packing up
        self.topmenu.pack(side="top", fill=tk.X)
        self.toolbar.pack(side="top", fill=tk.X)
        self.intro_label.pack()
        self.mainframe.pack(fill=tk.BOTH)
        self.statusbar.pack(side="bottom", fill=tk.X)

class MainFrame(tk.Frame): # pylint: disable=too-many-ancestors
    """
    The containg listbox and buttons to add things from DB
    This is seperate from toolbar, statusbar and topmenu
    """
    def __init__(self, master=None):
        super().__init__(master)

        # Btns
        self.add_btn = tk.Button(self, text="Add Record", command=self.add_record_window)
        self.remove_btn = tk.Button(self, text="Remove Item", command=self.remove_item)
        self.update_btn = tk.Button(self, text="Update list", command=self.update_tree)

        # BTNS grid
        self.add_btn.grid(column=0, row=0, sticky=tk.W)
        self.update_btn.grid(column=0, row=0, sticky=tk.E)
        self.remove_btn.grid(column=0, row=2, sticky='we')

        #TTK Tree
        self.tree = ttk.Treeview(self)
        self.tree['show'] = 'headings'
        self.tree['columns'] = ('cat no', 'label', 'artist')
        self.tree['columns'] = ('id', 'cat no', 'label', 'artist', 'img_path')
        self.tree.heading('id', text='id', anchor=tk.W)
        self.tree.heading('cat no', text='Cat No', anchor=tk.W)
        self.tree.heading('label', text='Label', anchor=tk.W)
        self.tree.heading('artist', text='Artist', anchor=tk.W)
        self.tree.column('cat no', width=100)
        self.tree.column('label', width=100)
        self.tree.column('artist', width=100)
        self.tree.column('id', width=30)
        self.tree.bind('<<TreeviewSelect>>', self.on_selected) # How to run?
        self.tree.grid(row=1, column=0, sticky='ns')

        self.show_image('images/vinyl.png')

        # Image
    def show_image(self, image_path):
        """
        Displays an image with a file path
        """
        load = Image.open(image_path)
        load = load.resize((128, 128), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render

        img.grid(row=3, column=0)

    def on_selected(self, event):
        """
        Changes image to show and runs the show image function
        """
        file_path = self.tree.item(self.tree.focus())['values'][4]

        self.show_image(file_path)

    def remove_item(self):
        """
        item_id becomes the id of the item selected in the treeview
        tree.focus returns the item ID of the selected item in the tree.
        tree.item returns a dict with value being a list of all the columns.
        [0] is the ID column in the tree
        """

        sql = ('DELETE FROM record WHERE id = %s')
        try:
            item_id = self.tree.item(self.tree.focus())['values'][0]
            with MySQLConnector() as con:
                if con:
                    #con.cursor.execute(f"""DELETE FROM record WHERE id = {item_id} """)
                    con.cursor.execute(sql, item_id)
                    con.connection.commit()
        except:
            self.master.statusbar.status_text.set(f'Need something selected')

        # Updates the mainframe window
        self.update_tree()

    def update_tree(self):
        """
        Dependent on correctly setup DB in settings menu
        This CLEARS the tree first and then updates it with the
        information that exists in the database
        """
        self.clear_tree() # Simply clears the tree
        with MySQLConnector() as con: # Get the data from DB
            id_count = 0 # num of items from the db.
            if con:
                con.cursor.execute("""SELECT * FROM record""") # SELECT ALL
                for row in con.cursor: # Then inserts into tree
                    self.tree.insert('', 'end', text=str(id_count),
                                     values=(
                                         row['id'], row['cat_no'],
                                         row['label'], row['artist'],
                                         row['img_path']))
                    id_count += 1
            else:
                self.master.statusbar.status_text.set('Connection failed')

    def add_record_window(self):
        """
        Opens a new window to add a new record to the databse
        """
        window = AddRecordFrame(self.master)

    def clear_tree(self):
        """
        This functions simply clears the tree, DOES NOT EDIT THE DB
        """
        for i in self.tree.get_children():
            self.tree.delete(i)

class AddRecordFrame(tk.Frame): # pylint: disable=too-many-ancestors, too-many-instance-attributes
    """
    In this window you can add a record to the database
    """
    def __init__(self, master=None):
        super().__init__(master)

        self.window = tk.Toplevel()

        # Labels
        self.artist_label = tk.Label(self.window, text="Artist Name")
        self.label_label = tk.Label(self.window, text="Label Name")
        self.catno_label = tk.Label(self.window, text="Cat Num")
        self.rel_name_label = tk.Label(self.window, text="Release Name")
        self.imgpath_label = tk.Label(self.window, text="Image Path")
        # Entries
        self.artist_entry = tk.Entry(self.window)
        self.label_entry = tk.Entry(self.window)
        self.catno_entry = tk.Entry(self.window)
        self.imgpath_entry = tk.Entry(self.window)
        # Buttons
        self.save_btn = tk.Button(self.window, text="Save to Databse", command=self.save_to_db)
        self.close_btn = tk.Button(self.window, text="Close", command=self.window.destroy)

        # Test browse
        self.browser_btn = tk.Button(self.window, text="Browse img", command=self.open_browser)

        ############# GRIDS #######################################
        # Grid Labels
        self.artist_label.grid(column=0, row=0)
        self.label_label.grid(column=0, row=1)
        self.catno_label.grid(column=0, row=2)
        self.imgpath_label.grid(column=0, row=3)
        # Grid Entries
        self.artist_entry.grid(column=1, row=0)
        self.label_entry.grid(column=1, row=1)
        self.catno_entry.grid(column=1, row=2)
        self.imgpath_entry.grid(column=1, row=3)
        # Grid Buttons
        self.save_btn.grid(column=0, row=4)
        self.close_btn.grid(column=1, row=4, columnspan=2)
        self.browser_btn.grid(column=2, row=3)

    def open_browser(self):
        """
        Opens a browser and returns the selected file's path
        """
        from tkinter import filedialog # Using built in filedialog

        file_path = filedialog.askopenfilename()
        self.imgpath_entry.insert(0, file_path)

    def save_to_db(self):
        """
        INSERT INTO `record` (`cat_no`, `label`, `artist`, `img_path`)
        VALUES ('EE0004', 'Emotions Electric', 'VA Sounds From The Emotional Underground', NULL);
        """
        cat_no = self.catno_entry.get()
        label = self.label_entry.get()
        artist = self.artist_entry.get()
        img_path = self.imgpath_entry.get()

        try:
            with MySQLConnector() as con:
                if con:
                    sql = """INSERT INTO `record` (`cat_no`, `label`, `artist`, `img_path`)
                                VALUES (%s, %s, %s, %s)"""

                    con.cursor.execute(sql, (cat_no, label, artist, img_path))
                    con.connection.commit()
                    self.master.mainframe.update_tree()
                else:
                    self.master.statusbar.status_text("No connection to the DB")
        except:
            self.master.statusbar.status_text("Could not update the tree")

class TopMenu(tk.Frame): # pylint: disable=too-many-ancestors
    """
    This is the top menu, with file and edit and so on...
    """
    def __init__(self, master=None):
        super().__init__(master)

        self.menu = tk.Menu(self.master)
        root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Settings", command=self.settings_window)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=exit)

    def settings_window(self):
        window = DbSettingsWindow(self.master)

class ToolBar(tk.Frame): # pylint: disable=too-many-ancestors
    """
    This is a toolbar that is autogenerated with icons that exist in the icon
    folder
    """
    def __init__(self, master=None):
        super().__init__(master)

        files_path = 'icons/'

        # Den här dictionaryn innehåller namn på alla knappar
        # jag vill använda, och vilken funktion som ska vara associerad
        # till knappen.
        self.buttons_dictionary = {'user-bookmarks': self.bookmarks,
                                   'user-home': self.home,
                                   'user-trash': self.trash,
                                   'preferences-desktop-display': self.pref}

        buttons_list = [] # Lista som innehåller alla knapp objekt
        for btn_name, function in self.buttons_dictionary.items():
            buttons_list.append(tk.Button(self, command=function))
            b = buttons_list[-1] # Referera till den senast tillagda knappen i listan
            b.image = tk.PhotoImage(file=files_path+btn_name+'.png')
            b.configure(image=b.image)
            b.pack(side="left")


    def bookmarks(self):
        self.master.statusbar.status_text.set("Bookmarks!")

    def home(self):
        self.master.statusbar.status_text.set("Home")

    def trash(self):
        self.master.statusbar.status_text.set("Traash")

    def pref(self):
        self.master.statusbar.status_text.set("Settings")

class StatusBar(tk.Frame): # pylint: disable=too-many-ancestors
    """
    This is the statusbar. It can take messages from master.toolbar.status_text
    """
    def __init__(self, master=None):
        super().__init__(master)

        self.status_text = tk.StringVar()

        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                              textvariable=self.status_text)
        self.status_text.set("Status bar")
        self.label.pack(fill=tk.X)

        def set(self, format, *args):
            self.label.config(text=format % args)
            self.label.update_idletask()

        def clear(self):
            self.label.config(text="")
            self.label.update_idletask()

class DbSettingsWindow(tk.Frame): # pylint: disable=too-many-ancestors, too-many-instance-attributes
    """
    This window is to set the database information
    """
    def __init__(self, master=None):
        super().__init__(master)

        self.window = tk.Toplevel()

        self.db_host = tk.StringVar()
        self.db_user = tk.StringVar()
        self.db_passwd = tk.StringVar()
        self.db_db = tk.StringVar()

        self.db_host.set(str(MySQLConnector.HOST))
        self.db_user.set(str(MySQLConnector.USER))
        self.db_passwd.set(str(MySQLConnector.PASSWD))
        self.db_db.set(str(MySQLConnector.DB))

        # Labels
        self.label_host = tk.Label(self.window, text="Host")
        self.label_user = tk.Label(self.window, text="User")
        self.label_passwd = tk.Label(self.window, text="Password")
        self.label_db = tk.Label(self.window, text="Databse")

        # Entries
        self.entry_host = tk.Entry(self.window, textvariable=self.db_host)
        self.entry_user = tk.Entry(self.window, textvariable=self.db_user)
        self.entry_passwd = tk.Entry(self.window, show="*", textvariable=self.db_passwd)
        self.entry_db = tk.Entry(self.window, textvariable=self.db_db)

        # Buttons
        self.connect_btn = tk.Button(self.window, text=("Test connection"),
                                     command=self.test_connection)
        self.close_btn = tk.Button(self.window, text="Close",
                                   command=self.window.destroy)
        self.save_btn = tk.Button(self.window, text="Save",
                                  command=self.save_settings)

        # Grid
        self.label_host.grid(row=1, column=0)
        self.entry_host.grid(row=1, column=1)
        self.label_user.grid(row=2, column=0)
        self.entry_user.grid(row=2, column=1)
        self.label_passwd.grid(row=3, column=0)
        self.entry_passwd.grid(row=3, column=1)
        self.label_db.grid(row=4, column=0)
        self.entry_db.grid(row=4, column=1)

        self.connect_btn.grid(row=6, column=0, columnspan=1, sticky=tk.W)
        self.save_btn.grid(row=6, column=1, columnspan=4, sticky=tk.W)
        self.close_btn.grid(row=6, column=2, columnspan=1, sticky=tk.W)

        #self.pack()

    def save_settings(self):
        try:
            MySQLConnector.HOST = self.entry_host.get()
            MySQLConnector.USER = self.entry_user.get()
            MySQLConnector.PASSWD = self.entry_passwd.get()
            MySQLConnector.DB = self.entry_db.get()

            self.master.statusbar.status_text.set("Saved!")

            self.entry_host.config(bg="green")
            self.entry_user.config(bg="green")
            self.entry_passwd.config(bg="green")
            self.entry_db.config(bg="green")

        except:
            print("Something wen't wrong")

    def test_connection(self):
        try:
            with MySQLConnector() as con:
                if con:
                    self.master.statusbar.status_text.set('Connection OK!')
                else:
                    self.master.statusbar.status_text.set('Connection failed')
        except pymysql.err.OperationalError as e:
            self.master.statusbar.status_text.set(e)


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
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    @property
    def db_info(self):
        return self.db_info

    @db_info.setter
    def db_info(self, *arg):
        self.db_info = [*arg]

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root).pack(side="top", fill="both", expand=True)
    root.mainloop()
