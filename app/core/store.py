from collections import defaultdict
import re
from .design import Design


class Store:

    def __init__(self):
        self.list_of_designs = list()
        self.flower_bucket = {'L': defaultdict(int), 'S': defaultdict(int)}

    def input_bouquet_designs(self) -> bool:
        """
        This functions takes design input from customer and store in the list
        design format:
        <design name><flower size><flower1 max quantity><flower1
        species>...<flowerN max quantity><flowerN species><total quantity>
        :return: False if list is empty otherwise True
        """

        print("Please provide bouquet designs: ")
        while True:
            design = input()
            if design == '':
                break

            design_obj = Store.generate_design(design)
            if design_obj:
                self.list_of_designs.append(design_obj)
            else:
                print('please provide valid design')

        return bool(self.list_of_designs)

    def add_flower(self, size, species):
        """
        Add flowers in the store bucket as per size and species
        :param size: flower size
        :param species: flower species
        :return: None
        """
        self.flower_bucket[size][species] += 1

    def validate_flower(self, flower):
        """
        Validate input provide by the user
        A flower is identified by a flower species and a flower size:
        for example, rL, aS
        :param flower: string provided by user as flower
        :return: True if value is valid otherwise False
        """
        try:
            species, size = flower
            check_size = size in self.flower_bucket
            check_flower = bool(re.match(r'[a-z]', species))
            return check_size and check_flower
        except ValueError:
            return False

    @staticmethod
    def generate_design(design):
        """
        This functions validated design input and populates Design instance
        with values
        :param design: design string provided by user
        :return: design object
        """
        try:
            design_pattern = Design.design_pattern
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
