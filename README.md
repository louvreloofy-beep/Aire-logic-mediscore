# Aire-logic-mediscore

A Python-based implementation of the NEWS2 system, designed to calculate a patient's risk score based on several physiological factors.

## Features:

* **test-driven development**: built using `pytest` to ensure 100% accuracy.
* **complex spo2 logic**: handles the conditional scoring for patients on both air and supplemental oxygen.
* **data validation**: includes rounding for temperature as per requirements.
* **Bonus: CBG Scoring**: implemented context aware capillary blood glucose scoring with dual range support (fasting or after eating).
* **Bonus: Trend Alerting**: built-in mechanism to flag an additional risk if a patient's score rises by more than 2 points (indicating rapid deterioration).

## installation and setup:
1. ensure you have Python 3.14+ installed.
2. install the testing framework:
   ```bash
   pip install pytest

## running tests:
3. run 'python -m pytest' in the terminal.