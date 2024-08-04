import random
import string
import stringprep


class Booking:
    def __init__(self) -> None:
        self.booking_id = self.generate_booking_id()
        self.status = "pending"
        self.payment_status = "pending"
        self.payment_id = None

    def __str__(self) -> str:
        return (
            f"Booking ID: {self.booking_id}\n"
            f"Status: {self.status}\n"
            f"Payment Status: {self.payment_status}\n"
            f"Payment ID: {self.payment_id}\n"
        )

    def generate_booking_id(self) -> str:
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def create_booking(self, status, payment_status, payment_id) -> None:
        self.status = status
        self.payment_status = payment_status
        self.payment_id = payment_id

    def check_booking_object(self, booking: "Booking") -> bool:
        class_vars = vars(self)
        booking_vars = vars(booking)

        for var_name, var_value in class_vars.items():
            if var_name in booking_vars:
                if var_value != booking_vars[var_name]:
                    return False
        return True
