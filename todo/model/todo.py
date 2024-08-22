# TODO: Add code here

class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed = False
        self.tags = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print("Ya esta en la lista")

    def __str__(self):
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self, todos):


prueba = Todo(1, 'hh', 'jj')
print(prueba.tags)
prueba.add_tag('Sapoperro')
print(prueba.tags)
prueba.add_tag('Sapoperro')
print(prueba.tags)







