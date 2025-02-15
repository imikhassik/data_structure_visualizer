from tkinter import *
from tkinter import ttk

from entry_parser import EntryParser
from data_structures.linked_list import LinkedList


class MainWindow:
    def __init__(self):
        self._root = Tk()
        self._example_value = StringVar()
        # self._example_value.trace_add("write", self._parse_user_entry)
        self._configure_window()
        self._create_widgets()
        self._configure_widgets()
        self._grid_widgets()

    def _configure_window(self):
        self._root.columnconfigure(index=0, weight=1)
        self._root.rowconfigure(index=0, weight=1)

    def _create_widgets(self):
        self._content = ttk.Frame(self._root)
        self._example_label = ttk.Label(self._content)
        self._steps_label = ttk.Label(self._content)
        self._example_entry = ttk.Entry(self._content)
        self._canvas = Canvas(self._content)
        self._steps = ttk.Label(self._content)

    def _configure_widgets(self):
        self._content.configure(padding=12)
        self._content.rowconfigure(index=2, weight=1)
        self._content.columnconfigure(index=2, weight=1)
        self._example_label.configure(text="Example:")
        self._steps_label.configure(text="Steps:")
        self._example_entry.configure(textvariable=self._example_value)
        self._example_entry.bind("<Return>", self._parse_user_entry)
        self._canvas.configure(width=1000, height=500, background="white")
        self._steps.configure(text="1. Step number one\n2. Step number two\n3. Step number three")

    def _grid_widgets(self):
        self._content.grid(column=0, row=0, sticky="nsew")
        self._example_label.grid(column=0, row=0, sticky="w")
        self._steps_label.grid(column=2, row=0, padx=10, sticky="w")
        self._example_entry.grid(column=0, row=1, pady=10, sticky="we")
        self._canvas.grid(column=0, row=2, sticky="nsew")
        self._steps.grid(column=2, row=1, rowspan=2, padx=10, pady=10, sticky="new")

    def _parse_user_entry(self, *args):
        parser = EntryParser()
        parser.parse(self._example_value.get())

        for entry in parser.result:
            ll = LinkedList(entry)
            print(ll)

    def start(self):
        self._root.mainloop()


main_window = MainWindow()
main_window.start()
