"""Various animals"""


class Rabbit:
    """The Killer Rabbit of Caerbannog

    The Killer Rabbit of Caerbannog is a fictional character in the
    Monty Python film Monty Python and the Holy Grail.
    """

    VICIOUSNESS = 100

    def __init__(self, health):
        """Initialize"""

        self.health = health

    def attack(self, combatant):
        """Attack"""

        return 2 + id(self)

    def retreat(self, xnumber):
        """Retreat"""

        return False
