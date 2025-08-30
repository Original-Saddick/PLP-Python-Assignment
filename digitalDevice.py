# ============================================================================
# Part 1: Base Class - DigitalDevice
# ============================================================================

class DigitalDevice:
    """
    A base class representing a generic digital device.
    This class demonstrates encapsulation with the `_is_on` attribute,
    which is intended for internal use (indicated by the leading underscore).
    """

    def __init__(self, brand, model):
        """
        Constructor to initialize a new DigitalDevice object.

        Args:
            brand (str): The brand of the device (e.g., 'Samsung', 'Apple').
            model (str): The model of the device (e.g., 'Galaxy Tab', 'iPad').
        """
        self.brand = brand
        self.model = model
        self._is_on = False  # Encapsulation: Not meant to be accessed directly from outside

    def power_on(self):
        """Turns the device on if it is currently off."""
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        """Turns the device off if it is currently on."""
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def get_status(self):
        """
        Returns a summary of the device's status.
        This method will be overridden in the child class to show polymorphism.
        """
        status = "ON" if self._is_on else "OFF"
        return f"Device: {self.brand} {self.model} | Status: {status}"


# ============================================================================
# Part 2: Inheritance - Smartphone Subclass
# ============================================================================

class Smartphone(DigitalDevice):
    """
    A subclass that inherits from DigitalDevice, representing a smartphone.
    It adds more specific attributes and methods.
    """

    def __init__(self, brand, model, phone_number):
        """
        Constructor for the Smartphone class.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model of the smartphone.
            phone_number (str): The phone number associated with the smartphone.
        """
        # Call the parent class constructor to initialize brand and model
        super().__init__(brand, model)
        self.phone_number = phone_number
        self.apps = []  # A list to store installed applications

    def install_app(self, app_name):
        """Adds an app to the smartphone's list of apps."""
        if app_name not in self.apps:
            self.apps.append(app_name)
            print(f"'{app_name}' has been installed on the {self.model}.")
        else:
            print(f"'{app_name}' is already installed.")

    def make_call(self, contact_name):
        """Simulates making a phone call if the phone is on."""
        if self._is_on:
            print(f"Dialing {contact_name} from {self.phone_number}...")
        else:
            print(f"Cannot make a call. The {self.model} is turned off.")

    def get_status(self):
        """
        Overrides the parent's get_status method to provide a more detailed summary.
        This is an example of Polymorphism, where the same method name ('get_status')
        behaves differently for the subclass.
        """
        status = "ON" if self._is_on else "OFF"
        app_count = len(self.apps)
        return (f"Smartphone: {self.brand} {self.model} | Number: {self.phone_number} | "
                f"Status: {status} | Apps Installed: {app_count}")


# ============================================================================
# Part 3: Creating and Using Objects
# ============================================================================

if __name__ == "__main__":
    # --- Create an instance of the DigitalDevice class ---
    my_tablet = DigitalDevice("Samsung", "Galaxy Tab S9")
    print("--- Generic Digital Device ---")
    print(my_tablet.get_status())
    my_tablet.power_on()
    print(my_tablet.get_status())
    print("-" * 30)

    # --- Create an instance of the Smartphone class ---
    my_phone = Smartphone("Google", "Pixel 8", "555-123-4567")
    print("\n--- Smartphone Device ---")
    print(my_phone.get_status())  # Notice the different output from the overridden method
    my_phone.power_on()
    my_phone.install_app("Maps")
    my_phone.install_app("Music Player")
    my_phone.make_call("Mom")
    print(my_phone.get_status())
    my_phone.power_off()
    print(my_phone.get_status())
    my_phone.make_call("Dad") # This call should fail