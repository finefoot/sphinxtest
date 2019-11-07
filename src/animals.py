"""Various animals"""


class KillerRabbit:
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

        combatant.health -= 10

    def retreat(self):
        """Retreat"""

        return False
