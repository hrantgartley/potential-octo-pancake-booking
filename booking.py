import random
import string


class Booking:
    """
    Represents a booking object.
    Attributes:
        booking_id (str): The unique ID of the booking.
        status (str): The status of the booking.
        payment_status (str): The payment status of the booking.
        payment_id (int): The ID of the payment associated with the booking.
    Methods:
        __init__(): Initializes a new instance of the Booking class.
        __str__(): Returns a string representation of the booking object.
        get_booking_id(): Returns the booking ID.
        get_status(): Returns the status of the booking.
        get_payment_status(): Returns the payment status of the booking.
        get_payment_id(): Returns the payment ID associated with the booking.
        generate_booking_id(): Generates a unique booking ID.
        create_booking(status, payment_status, payment_id): Creates a new booking with the given status, payment status, and payment ID.
        check_booking_object(booking): Checks if the given booking object is equal to the current booking object.
    """

    def __init__(self) -> None:
        self.booking_id = self.generate_booking_id()
        self.status = "pending"
        self.payment_status = "pending"
        self.payment_id = None

    def __str__(self) -> str:
        """
        Returns a string representation of the booking object.
        """
        return (
            f"Booking ID: {self.booking_id}\n"
            f"Status: {self.status}\n"
            f"Payment Status: {self.payment_status}\n"
            f"Payment ID: {self.payment_id}\n"
        )

    def get_booking_id(self) -> str | None:
        """
        Returns the booking ID.

        :return: The booking ID as a string, or None if no booking ID is set.
        """
        return self.booking_id

    def get_status(self) -> str:
        """
        Returns the status of the booking.

        :return: The status of the booking.
        :rtype: str
        """
        return self.status

    def get_payment_status(self) -> str:
        """
        Returns the payment status of the booking.

        :return: A string representing the payment status.
        """
        return self.payment_status

    def get_payment_id(self) -> int:
        """
        Returns the payment ID associated with the booking.

        :return: The payment ID.
        :rtype: int
        """
        return self.payment_id

    def generate_booking_id(self) -> str:
        """
        Generates a unique booking ID.

        Returns:
            str: The generated booking ID.
        """
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def create_booking(self, status, payment_status, payment_id) -> None:
        """
        Creates a booking with the given status, payment status, and payment ID.

        Parameters:
        - status (str): The status of the booking.
        - payment_status (str): The payment status of the booking.
        - payment_id (int): The ID of the payment associated with the booking.

        Returns:
        None
        """
        self.status = status
        self.payment_status = payment_status
        self.payment_id = payment_id

    def check_booking_object(self, booking: "Booking") -> bool:
        """
        Check if the given booking object matches the current object.
        Parameters:
            booking (Booking): The booking object to compare with.
        Returns:
            bool: True if the booking object matches the current object, False otherwise.
        """
        class_vars = vars(self)
        booking_vars = vars(booking)

        for var_name, var_value in class_vars.items():
            if var_name in booking_vars:
                if var_value != booking_vars[var_name]:
                    return False
        return True
