import re
from collections import defaultdict

from .design import Design


def main():
    print("Welcome to Bouquet System")
    catalog = input_design()
    if len(catalog) != 0:
        print('flower availability: ')
        bucket_s = defaultdict(int)
        bucket_l = defaultdict(int)
        while True:
            flower = input()
            if flower == '':
                break
            else:
                species, size = flower
                if size == 'L':
                    bucket_l[species] += 1
                    # check_bouquet(catalog, bucket_l, size='L')
                elif size == 'S':
                    bucket_s[species] += 1
                    # check_bouquet(catalog, bucket_s, size='S')
                else:
                    print('please provide correct flower data')


def input_design() -> list:
    """
    this functions takes design input from customer and store in the list
    design format:
    <design name><flower size><flower1 max quantity><flower1
    species>...<flowerN max quantity><flowerN species><total quantity>
    :return: list of design_specification instances
    """
    design_list = []

    print("Please provide designs: ")
    while True:
        design = input()
        if design == '':
            break
        else:
            design_obj = generate_design(design)
            if design_obj:
                design_list.append(design_obj)
            else:
                print("invalid design")
    return design_list


def generate_design(design):
    """
    This functions validated design input and populates Design instance
    with values
    :param design: design string provided by user
    :return: design object
    """
    try:
        des_pattern = r"(?P<name>[A-Z])(?P<size>[LS])(?P<species>.*)(?P<total>[1-9][0-9]*)"
        design_pattern = re.compile(des_pattern)
        design_match = design_pattern.match(design)
        design_dict = design_match.groupdict()

        species = re.findall(r"[1-9][0-9]*[a-z]",
                             design_dict["species"])
        d = {i[-1]: int(i[:-1]) for i in species}
        if sum(d.values()) >= int(design_dict["total"]):
            design_dict["species"] = d
            return Design(**design_dict)
        return None
    except AttributeError:
        return None


def check_bouquet(design_list: list, bucket: dict, size: str):
    pass
