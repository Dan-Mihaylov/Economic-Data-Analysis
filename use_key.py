def get_api_key():

    with open("C:/Users/danie/Desktop/fred_api_key.txt", "r") as file:
        key = file.readline()
        return key

