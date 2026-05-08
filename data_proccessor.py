import pickle

def process(items):
    result = []
    for i in range(len(items)):  # should use enumerate
        if items[i] != None:     # should use 'is not None'
            result.append(items[i])
    return result

def load_data(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)  # unsafe deserialization

def calculate(numbers):
    total = 0
    for n in numbers:
        total = total + n  # should use sum()
    return total / len(numbers)  # no empty list check
