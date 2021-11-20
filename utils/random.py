import random
import string
from mirage.config import Config


class RandomIdGenerator:
    def __init__(self):
        self.chars = string.ascii_lowercase + string.digits
        self.length = Config.DEFAULT_CODE_LENGTH

    def generate(self):
        res = ""
        for i in range(self.length):
            res += random.choice(self.chars)
        return res


def get_random_id_generator():
    return RandomIdGenerator()
