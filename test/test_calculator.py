from src.calculator import (
    calculate_medi_score, 
    get_respiration_score, 
    get_spo2_score, 
    get_temperature_score,
    get_cbg_score
)

# testing respiration score
def test_respiration_normal():
    assert get_respiration_score(15) == 0
def test_respiration_high():
    assert get_respiration_score(30) == 3

# testing spo2 score
def test_spo2_at_95_on_air():
    assert get_spo2_score(95,0) == 0
def test_spo2_at_95_on_oxygen():
    assert get_spo2_score(95,2) == 2

# testing temperature score
def test_temp_low():
    assert get_temperature_score(34.5) == 3
def test_temp_rounding_logic():
    assert get_temperature_score(35.04) == 3
def test_temp_high():
    assert get_temperature_score(39.5) == 2

# testing main calculator
def test_patient_1():
    patient = {"air_or_oxygen": 0, "consciousness": 0, "respiration_rate": 15, "spo2": 95, "temperature": 37.1}
    score, alert = calculate_medi_score(patient) 
    assert score == 0
    assert alert is False

def test_patient_2():
    patient = {"air_or_oxygen": 2, "consciousness": 0, "respiration_rate": 17, "spo2": 95, "temperature": 37.1}
    score, alert = calculate_medi_score(patient)
    assert score == 4
    assert alert is False

def test_patient_3():
    patient = {"air_or_oxygen": 2, "consciousness": 1, "respiration_rate": 23, "spo2": 88, "temperature": 38.5}
    score, alert = calculate_medi_score(patient)
    assert score == 8
    assert alert is False

# bonus task testing
def test_cbg_fasting_normal():
    assert get_cbg_score(4.5, True) == 0

def test_cbg_after_eating_high():
    # 9.0 or above after eating is Score 3
    assert get_cbg_score(9.5, False) == 3

# bonus task testing for trend alerting
def test_trend_alert_trigger():
    patient = {"air_or_oxygen": 0, "consciousness": 0, "respiration_rate": 26, "spo2": 95, "temperature": 37.0}
    score, alert = calculate_medi_score(patient, previous_total=0)
    assert score == 3
    assert alert is True

def test_trend_no_alert():
    patient = {"air_or_oxygen": 0, "consciousness": 0, "respiration_rate": 15, "spo2": 95, "temperature": 37.1}
    score, alert = calculate_medi_score(patient, previous_total=1)
    assert score == 0
    assert alert is False