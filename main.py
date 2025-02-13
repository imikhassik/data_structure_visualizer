from tkinter import *
from tkinter import ttk


class MainWindow:
    def __init__(self):
        self._root = Tk()
        self._example_value = StringVar()
        self._example_value.trace_add("write", self._parse_user_entry)
        self._configure()
        self._grid()

    def _configure(self):
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(2, weight=1)

    def _populate(self):
        self._content = ttk.Frame(self._root, padding=12)
        self._example_label = ttk.Label(self._content, text="Example:")
        self._steps_label = ttk.Label(self._content, text="Steps:")
        self._example_entry = ttk.Entry(self._content, textvariable=self._example_value)

    def _grid(self):
        self._populate()
        self._content.grid(column=0, row=0, sticky="nsew")
        self._example_label.grid(column=0, row=0, sticky="w")
        self._steps_label.grid(column=2, row=0, sticky="w")
        self._example_entry.grid(column=0, row=1, columnspan=2, sticky="we")

    def _parse_user_entry(self, *args):
        print(self._example_value.get().split(','))

    def start(self):
        self._root.mainloop()


main_window = MainWindow()
main_window.start()
