from src.section_enums import Label, Sample


def test_sample():
    """
    SPECIFICATION: the sample provides the volume in m³ and liters

    ASSUMPTION: implementation is correct
    TASK: patch the test
    """
    sample = Sample("New", 123.4)
    assert sample.volume__m3 == 123.4
    assert sample.volume__l == 123.4*1e3 # 2e3 ist Quatsch :)


def test_labels():
    """
    ASSUMPTION: implementation is correct
    TASK: patch the test
    """
    sample = Sample("New", 123.4, Label.FULL)
    assert sample.label == Label.FULL # Value ungleich Enum Wert
