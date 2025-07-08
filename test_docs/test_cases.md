# Test Cases

## 1. Temperature Data Simulation Tests

| Test Case ID | Description                      | Input                      | Expected Output                           | Purpose                                    |
|--------------|--------------------------------|----------------------------|-------------------------------------------|--------------------------------------------|
| TC_SIM_01    | Generate 50 temperature records | num_records=50              | CSV file with 50 rows, correct timestamp & temp format | Verify correct data generation & formatting |
| TC_SIM_02    | Generate zero records           | num_records=0               | CSV file created but empty except header  | Test boundary condition for zero records  |
| TC_SIM_03    | Generate data with temp range   | Random temp within [15, 30] | Temperatures mostly between 22-28, occasional outside | Test randomness & range compliance         |

---

## 2. Error Diagnosis Tests

| Test Case ID | Description                   | Input                            | Expected Output                            | Purpose                                  |
|--------------|-------------------------------|---------------------------------|--------------------------------------------|------------------------------------------|
| TC_DIAG_01   | Diagnose normal temperature   | [22, 23, 24]                    | ["Normal", "Normal", "Normal"]              | Confirm normal temps classified correctly |
| TC_DIAG_02   | Diagnose too cold temperature | [10, 17, 18]                   | ["Too Cold", "Too Cold", "Normal"]          | Verify lower boundary classification      |
| TC_DIAG_03   | Diagnose too hot temperature  | [33, 34, 40]                   | ["Too Hot", "Too Hot", "Too Hot"]            | Verify upper boundary classification      |
| TC_DIAG_04   | Diagnose unstable temperature | [20, 27, 21]                   | ["Normal", "Unstable", "Normal"]             | Detect rapid temp fluctuations             |
| TC_DIAG_05   | Empty input list              | []                             | []                                          | Handle empty input gracefully              |
| TC_DIAG_06   | Invalid types                | ["a", None, 25]                 | Raise TypeError or ValueError                | Validate input type checks                  |

---

## 3. Report Generation Tests

| Test Case ID | Description                      | Input CSV file                   | Expected Output file                          | Purpose                                    |
|--------------|----------------------------------|---------------------------------|----------------------------------------------|--------------------------------------------|
| TC_REP_01    | Generate report for normal data   | CSV with normal temperatures     | CSV report with correct diagnosis column and summary | Verify successful report creation           |
| TC_REP_02    | Generate report for empty data    | Empty CSV file                   | Empty report with headers only                 | Test handling of empty input data           |
| TC_REP_03    | Invalid input file path           | Non-existent CSV path            | Raise FileNotFoundError                        | Test file handling and error reporting      |

---

## Notes:
- All tests should be automated using Pytest where applicable.
- Include boundary and edge cases.
- Validate output file existence and content correctness.
