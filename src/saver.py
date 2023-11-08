import pickle


DATA_CACHE = 'cache'


def read_data(file_name=DATA_CACHE):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return dict()


def save_data(data, file_name=DATA_CACHE):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)
