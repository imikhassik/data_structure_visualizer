import re

# TODO: test
# TODO: add error handling for user input
class EntryParser:
    def __init__(self):
        self.result = []
        self.index = 0

    def parse(self, entry_value):
        p = re.compile(r'\w')
        self.result = re.findall(p, entry_value)
        print(self.result)
        # for c in entry_value:
        #     if c == "[":
        #         self.result.append([])
        #         self.index = len(self.result) - 1
        #     elif c.isalnum():
        #         self.result[self.index].append(c)
