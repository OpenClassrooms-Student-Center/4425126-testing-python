from calculate.view import View


def test_should_print_menu(capsys):
    View.print_menu()
    out, err = capsys.readouterr()
    expect_out = ("\n=========== MENU ==========="
                  "\n1 - Addition"
                  "\n2 - Soustraction"
                  "\n3 - Multiplication"
                  "\n4 - Division"
                  "\n5 - Quitter"
                  "\n============================\n\n")
    assert out == expect_out


def test_should_print_end_message(capsys):
    View.end_message()
    out, err = capsys.readouterr()
    expect_out = "=========== GOOD-BYE ===========\n"
    assert out == expect_out


def test_should_print_result(capsys):
    operation = "5+10"
    result = 15
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expect_out = f"RESULTAT : {operation} = {result}\n"
    assert out == expect_out


def test_should_print_result_with_error(capsys):
    operation = "5+10+A"
    result = None
    View.print_result(operation, result)
    out, err = capsys.readouterr()
    expect_out = f"Votre operation est incorrect ! : {operation}\n"
    assert out == expect_out
