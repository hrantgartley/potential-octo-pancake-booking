import unittest
from booking import Booking


class TestBooking(unittest.TestCase):

    def test_generate_booking_id(self):
        booking = Booking()
        booking_id = booking.generate_booking_id()
        self.assertEqual(len(booking_id), 6)
        self.assertTrue(all(c.isalnum() for c in booking_id))

    def test_create_booking(self):
        booking = Booking()
        booking.create_booking("confirmed", "paid", 12345)
        self.assertEqual(booking.status, "confirmed")
        self.assertEqual(booking.payment_status, "paid")
        self.assertEqual(booking.payment_id, 12345)

    def test_check_booking_object(self):
        booking1 = Booking()
        booking2 = Booking()
        booking2.booking_id = booking1.booking_id
        booking2.status = booking1.status
        booking2.payment_status = booking1.payment_status
        booking2.payment_id = booking1.payment_id
        self.assertTrue(booking1.check_booking_object(booking2))

        booking2.status = "confirmed"
        self.assertFalse(booking1.check_booking_object(booking2))

    def test_get_booking_id(self):
        booking = Booking()
        self.assertEqual(booking.get_booking_id(), booking.booking_id)

    def test_get_status(self):
        booking = Booking()
        self.assertEqual(booking.get_status(), booking.status)

    def test_get_payment_status(self):
        booking = Booking()
        self.assertEqual(booking.get_payment_status(), booking.payment_status)

    def test_get_payment_id(self):
        booking = Booking()
        self.assertEqual(booking.get_payment_id(), booking.payment_id)

    def test_str(self):
        booking = Booking()
        expected_str = (
            f"Booking ID: {booking.booking_id}\n"
            f"Status: {booking.status}\n"
            f"Payment Status: {booking.payment_status}\n"
            f"Payment ID: {booking.payment_id}\n"
        )
        self.assertEqual(str(booking), expected_str)


if __name__ == "__main__":
    unittest.main()
