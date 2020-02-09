import json
import random

ALL_DATA = []

def load_data(filename):
    global ALL_DATA
    with open(filename) as f:
        ALL_DATA = json.load(f)

def get_data():
    return list(filter(lambda _: random.random() < 0.99, ALL_DATA))