from .store import Store


def main():
    print("---------Welcome to Bouquet Shop----------")
    store = Store()

    if store.input_bouquet_designs():
        print('Provide flower availability: ')
        while True:
            flower = input()
            if flower == '':
                break
            if store.validate_flower(flower):
                species, size = flower
                store.add_flower(size, species)
                # store.check_bouquet(size)
            else:
                print('please provide correct flower data')