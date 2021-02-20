
class Design:

    def __init__(self, name: str, size: str, species: dict, total: str):
        """
        Initialize design instance
        :param name: design name is indicated by a single,
                            uppercase letter: A - Z
        :param size: A flower size is indicated by a single,
                            uppercase letter: L (large) and S (small)
        :param species: A flower species is identified by a single,
                            lowercase letter:  a - z
        :param total: The total quantity of flowers
        """
        self.name = name
        self.size = size
        self.species = species
        self.total = int(total)

    @property
    def species_set(self) -> set:
        """
        Set of flower species
        :return: set of flower species required in the bouquet
        """
        return set(self.species)

    def __str__(self):
        return f'{self.name}-{self.size}-{self.species_set}-{self.total}'