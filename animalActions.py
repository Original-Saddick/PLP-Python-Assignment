# ============================================================================
# Part 1: The Parent Class (Superclass)
#
# This class defines the basic structure that all our animal classes will share.
# It has an initializer (__init__) and a 'move' method that child classes
# are expected to override.
# ============================================================================

class Animal:
    """A base class for all animals."""

    def __init__(self, name):
        """
        Constructor for the Animal class.

        Args:
            name (str): The name of the animal (e.g., 'Polly', 'Nemo').
        """
        self.name = name

    def move(self):
        """
        Defines a generic move action.
        This method is intended to be overridden by subclasses. If a subclass
        forgets to implement it, this message will be shown.
        """
        print(f"{self.name} moves in a generic way.")


# ============================================================================
# Part 2: The Child Classes (Subclasses)
#
# Each of these classes inherits from the Animal class. They call the parent's
# constructor using super().__init__() and provide their own specific
# implementation of the move() method. This is polymorphism.
# ============================================================================

class Bird(Animal):
    """Represents a bird that flies."""

    def move(self):
        """Overrides the parent move() method to describe flying."""
        print(f"{self.name} the bird is Flying 🐦...")


class Fish(Animal):
    """Represents a fish that swims."""

    def move(self):
        """Overrides the parent move() method to describe swimming."""
        print(f"{self.name} the fish is Swimming 🐠...")


class Lion(Animal):
    """Represents a lion that runs."""

    def move(self):
        """Overrides the parent move() method to describe running."""
        print(f"{self.name} the lion is Running 🦁...")


# ============================================================================
# Part 3: Demonstrating Polymorphism
#
# Here, we create objects of different classes and treat them as if they
# are the same type (Animal). We can call the same method, move(), on each
# one, and Python executes the correct version for that object's class.
# ============================================================================

if __name__ == "__main__":
    # Create instances of each animal class
    polly = Bird("Polly")
    nemo = Fish("Nemo")
    simba = Lion("Simba")

    # Create a list containing these different objects
    animals = [polly, nemo, simba]

    print("--- Demonstrating Polymorphic Behavior ---")

    # Loop through the list and call the move() method on each object.
    # Notice that we don't need to check what type of animal it is.
    # The correct method is called automatically.
    for animal in animals:
        animal.move()