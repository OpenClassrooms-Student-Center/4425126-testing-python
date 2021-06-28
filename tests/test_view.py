import unittest
import contextlib

from io import StringIO

from calculate.view import View


class TestView(unittest.TestCase):
    def setUp(self):
        self.temp_stdout = StringIO()

    def test_should_print_menu(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_menu()

        output = self.temp_stdout.getvalue()
        expect_out = ("\n=========== MENU ==========="
                      "\n1 - Addition"
                      "\n2 - Soustraction"
                      "\n3 - Multiplication"
                      "\n4 - Division"
                      "\n5 - Quitter"
                      "\n============================\n\n")
        self.assertEqual(output, expect_out)

    def test_should_print_end_message(self):
        with contextlib.redirect_stdout(self.temp_stdout):
            View.end_message()

        output = self.temp_stdout.getvalue()
        expect_out = "=========== GOOD-BYE ===========\n"
        self.assertEqual(output, expect_out)

    def test_should_print_result(self):
        operation = "5+10"
        result = 15
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation, result)

        output = self.temp_stdout.getvalue()
        expect_out = f"RESULTAT : {operation} = {result}\n"
        self.assertEqual(output, expect_out)

    def test_should_print_result_with_error(self):
        operation = "5+10+A"
        result = None
        with contextlib.redirect_stdout(self.temp_stdout):
            View.print_result(operation, result)

        output = self.temp_stdout.getvalue()
        expect_out = f"Votre operation est incorrect ! : {operation}\n"
        self.assertEqual(output, expect_out)


if __name__ == "__main__":
    unittest.main()
