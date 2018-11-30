"""
Main module
"""

####################### IMPORTS ###############################################
import tkinter as tk
import sqlite3 as sq
###############################################################################

class Application(tk.Frame): # pylint: disable=too-many-ancestors
    """
    Main app class
    """
    def __init__(self, master=None):
        super().__init__(master)

class SQLite():
    """
    My SQLite class
    """
    def __init__(self):
        self._connection = sq.connect('example.db')

        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


    @property
    def connection(self):
        """
        Public connection defenition
        """
        return self._connection

    @property
    def cursor(self):
        """
        Usable cursor property
        """
        return self._cursor

if __name__ == "__master__":
    ROOT = tk.Tk()

    Application(master=ROOT).pack(side="top", fill="both", expand=True)
    ROOT.mainloop()
