# TODO: test
# TODO: add error handling for user input
class EntryParser:
    def __init__(self, entry):
        self.result = []
        self.entry = entry
        self._skip_invalid_start_chars()
        self._validate_entry()

    def _skip_invalid_start_chars(self):
        start = 0
        while start < len(self.entry) and self.entry[start] != '[':
            start += 1

        if start >= len(self.entry):
            raise ValueError("Entry does not contain a list.")

        self.entry = self.entry[start:]

    def _validate_entry(self):
        if not self.entry:
            raise ValueError("Entry can't be empty.")

        brackets = []
        for c in self.entry:
            if c == "[":
                brackets.append(c)
            elif c == "]":
                if brackets:
                    brackets.pop()
                else:
                    raise ValueError("Entry must be a valid list or lists separated by comma or white space.")

        if brackets:
            raise ValueError("Entry must be a valid list or lists separated by comma or white space.")


    def parse(self):
        node_value = ""
        ignore = False
        for c in self.entry:
            if c == "[":
                self.result.append([])
                node_value = ""
                ignore = False
            elif c.isalnum():
                node_value += c
            elif not ignore and c in [',', ']']:
                self.result[-1].append(node_value)
                node_value = ""
                if c == ']':
                    ignore = True
