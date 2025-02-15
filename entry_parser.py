# TODO: test
# TODO: add error handling for user input
class EntryParser:
    def __init__(self):
        self.result = []
        self.index = 0

    def parse(self, entry_value):
        for c in entry_value:
            if c == "[":
                self.result.append([])
                self.index = len(self.result) - 1
            elif c.isalnum():
                self.result[self.index].append(c)
