from src.Text_Alignment.utils import text_alignment


def test_case_1():
    result = text_alignment(1)

    assert len(result) == 7


def test_case_2():
    result = text_alignment(3)

    assert isinstance(result, list)


def test_case_3():
    result = text_alignment(5)

    assert result[0].strip() == "H"


def test_case_4():
    result = text_alignment(5)

    assert "HHHHH" in result[5]


def test_case_5():
    result = text_alignment(5)

    assert result[-1].strip() == "H"