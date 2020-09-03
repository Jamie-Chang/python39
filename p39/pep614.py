# 🤷‍♂️
from contextlib import contextmanager
from dataclasses import dataclass

@dataclass
class QPushButton:
    name: str

    @contextmanager
    def connect(self):
        print(f"[{self.name}] Before")
        yield
        print(f"[{self.name}] After")


buttons = [QPushButton(f'Button {i}') for i in range(10)]

# Do stuff with the list of buttons...

@buttons[0].connect()
def spam():
    ...

@buttons[1].connect()
def eggs():
    ...


spam()
eggs()
