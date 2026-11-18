from app.engine.xuankong import get_mountain, get_period, analyze_house

def test_24_mountain_cardinal_centres():
    assert get_mountain(0)[1] == "Tý"
    assert get_mountain(90)[1] == "Mão"
    assert get_mountain(180)[1] == "Ngọ"
    assert get_mountain(270)[1] == "Dậu"

def test_period_nine():
    assert get_period(2024) == 9
    assert get_period(2044) == 1

def test_house_analysis():
    result = analyze_house(2024, 180)
    assert result["period"] == 9
    assert result["facing_mountain"]["name"] == "Ngọ"
    assert result["sitting_mountain"]["name"] == "Tý"
