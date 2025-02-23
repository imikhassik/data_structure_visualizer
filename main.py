from tkinter import *
from tkinter import ttk

from ds_factory import DataStructureFactory
from entry_parser import EntryParser
from utils import Tag, DSType


class MainWindow:
    def __init__(self):
        self._root = Tk()
        self._example_value = StringVar()
        self._ds_type_value = StringVar()

        self._configure_window()
        self._create_widgets()
        self._configure_widgets()
        self._grid_widgets()

    def _configure_window(self):
        self._root.title("Data Structure Visualizer")
        self._root.columnconfigure(index=0, weight=1)
        self._root.rowconfigure(index=0, weight=1)

    def _create_widgets(self):
        self._content = ttk.Frame(self._root)
        self._example_label = ttk.Label(self._content)
        self._steps_label = ttk.Label(self._content)
        self._example_entry = ttk.Entry(self._content)
        self._ds_type_entry = ttk.Combobox(self._content)
        self._canvas = Canvas(self._content)
        self._steps = ttk.Label(self._content)

    def _configure_widgets(self):
        self._content.configure(padding=12)
        self._content.columnconfigure(index=0, weight=1)
        self._content.rowconfigure(index=2, weight=1)

        self._example_label.configure(text="Example:")

        self._steps_label.configure(text="Steps:")

        self._example_entry.configure(textvariable=self._example_value)
        self._example_entry.bind(sequence="<Return>", func=self._map_data_structures_to_canvas)
        self._example_entry.focus()

        self._ds_type_entry.configure(textvariable=self._ds_type_value)
        self._ds_type_entry['values'] = [DSType.LINKED_LIST, DSType.TREE, DSType.GRAPH]
        self._ds_type_entry.state(['readonly'])
        self._ds_type_entry.current(0)
        self._ds_type_entry.bind(sequence="<Key>", func=self._process_ds_type_event)

        self._canvas.configure(width=1000, height=500, background="white")

        self._steps.configure(text="1. Step number one\n2. Step number two\n3. Step number three")

    def _grid_widgets(self):
        self._content.grid(column=0, row=0, sticky="nsew")
        self._example_label.grid(column=0, row=0, sticky="w")
        self._steps_label.grid(column=2, row=0, padx=10, sticky="w")
        self._example_entry.grid(column=0, row=1, pady=10, sticky="we")
        self._ds_type_entry.grid(column=1, row=1, pady=10, padx=(10, 0), sticky="w")
        self._canvas.grid(column=0, row=2, columnspan=2, sticky="nsew")
        self._steps.grid(column=2, row=1, rowspan=2, padx=10, pady=10, sticky="new")

    def _map_data_structures_to_canvas(self, *args):
        self._canvas.delete(Tag.ALL_CANVAS_ITEMS)
        parser = EntryParser(entry=self._example_value.get())
        parser.parse()
        for entry in parser.result:
            factory = DataStructureFactory()
            data_structure = factory.create(entry=entry, ds_type=self._ds_type_value.get())
            data_structure.map_to_canvas(self._canvas)
            print(data_structure)

    def _process_ds_type_event(self, event, *args):
        match event.keysym:
            case "l":
                self._ds_type_entry.current(0)
            case "t":
                self._ds_type_entry.current(1)
            case "g":
                self._ds_type_entry.current(2)
        self._example_entry.focus()

    def start(self):
        self._root.mainloop()


main_window = MainWindow()
main_window.start()
