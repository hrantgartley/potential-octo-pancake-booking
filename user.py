
from booking import Booking 

class User:
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bookings = []

    def __str__(self) -> str:
        """
        Returns a string representation of the user object.
        """
        return (
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Email: {self.email}\n"
        )

    def get_first_name(self) -> str:
        """
        Returns the first name of the user.

        :return: The first name of the user.
        :rtype: str
        """
        return self.first_name

    def get_last_name(self) -> str:
        """
        Returns the last name of the user.

        :return: The last name of the user.
        :rtype: str
        """
        return self.last_name

    def get_email(self) -> str:
        """
        Returns the email address of the user.

        :return: The email address of the user.
        :rtype: str
        """
        return self.email

    def get_bookings(self) -> list[Booking]:
        """
        Returns a list of bookings associated with the user.

        :return: A list of Booking objects.
        :rtype: list[Booking]
        """
        return self.bookings

    def add_booking(self, booking: Booking) -> None:
        """
        Adds a booking to the user's list of bookings.

        :param booking: The booking to add.
        """
        self.bookings.append(booking)

    def remove_booking(self, booking: Booking) -> None:
        """
        Removes a booking from the user's list of bookings.

        :param booking: The booking to remove.
        """
        self.bookings.remove(booking)

    def check_user_object(self, other_user: "User") -> bool:
        """
        Checks if another User object is equal to this one.

        :param other_user: The other User object to compare.
        :return: True if the objects are equal, False otherwise.
        :rtype: bool
        """
        return (
            self.first_name == other_user.first_name
            and self.last_name == other_user.last_name
            and self.email == other_user.email
            and self.bookings == other_user.bookings
        )
    
    def hash_sort(self) -> str:
        """
        Returns a hash value based on the user's first name, last name, and email.
        """
        size = [len(self.first_name), len(self.last_name), len(self.email)]
        return "".join(str(s) for s in size)