
import random


class Note():
    def __init__(self, txt):
        self.id = random.getrandbits(28)
        self.txt = txt

    def __str__(self):
        return f"{self.id}-{self.txt[:10]}"

    def serialize(self):
        return {
            "id":self.id,
            "txt":self.txt
        }