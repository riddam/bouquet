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

        print("Please provide bouquet designs(or blank to exit): ")
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
            if sum(d.values()) >= int(design_dict["total"]) >= len(d):
                design_dict["species"] = d
                return Design(**design_dict)
            return None
        except AttributeError:
            return None

    def check_bouquet(self, size: str) -> list:
        """
        check for the possibility of bouquet formation with following
        conditions
        - A bouquet must have all and only flower species required
        by the corresponding design
        (i.e. comply with the implicit flower min quantities).
        - Every required flower species in a bouquet
        must be in the flower quantity that is less or
        equal to the flower max quantity specified by the design.
        -The sum of the flower quantities in a bouquet should be equal
        to the total quantity of flowers in the corresponding design.
        :param size: flower size allowed in the bouquet
        :return: list of bouquet
        """
        result = []
        bucket = self.flower_bucket[size]

        def _is_bouquet():
            if bouquet_total == design.total:
                bouquet_str = Store.prepare_bouquet(name=design.name,
                                                    size=size,
                                                    flowers=bouquet)
                result.append(bouquet_str)
                Store.deduct_from_bucket(bouquet, bucket)
                return True
            return False

        for design in self.list_of_designs:
            all_set = set(bucket)
            if design.size == size and design.species_set.issubset(all_set):
                bouquet = dict.fromkeys(design.species_set, 1)
                bouquet_total = len(bouquet)
                if _is_bouquet():
                    continue
                for key, value in design.species.items():
                    current_a = bucket[key] - 1
                    current_b = value - 1

                    # balance to fill bouquet total
                    bal = current_a if current_a <= current_b else current_b
                    if bouquet_total + bal > design.total:
                        bal -= (bouquet_total + bal) - design.total
                    bouquet[key] += bal
                    bouquet_total += bal

                    if _is_bouquet():
                        break

        return result

    @staticmethod
    def deduct_from_bucket(bouquet, bucket):
        """
        this function reduce the flower from bucket which were used in
        making bouquet
        :param bouquet: dictionary of bouquet flower with count
        :param bucket: dictionary of available flower in bucket with count
        :return: None
        """
        for species, count in bouquet.items():
            bucket[species] -= count
            if bucket[species] == 0:
                bucket.pop(species)

    @staticmethod
    def prepare_bouquet(name: str, size: str, flowers: dict) -> str:
        """
         This function prepares bouquet as a single line of characters with
         the following format:
        <design name><flower size><flower1 quantity><flower1 species>...
        <flowerN quantity><flowerN species>
        :param name: name of the bouquet design
        :param size: size of the flowers
        :param flowers: dictionary of flowers species and its count
        :return:
        """
        flowers = ''.join([str(flowers[k]) + k for k in sorted(flowers)])
        bouquet = name + size + flowers
        return bouquet
