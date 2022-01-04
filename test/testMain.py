import main


def test_days_to_unit():
    assert main.days_to_unit(10, minutes)== "14400 minutes"
    assert main.days_to_unit(25, hours)== "600 hours"
    assert main.days_to_unit(30, hour)=="Please enter a proper unit of conversion(hours or minutes)"
