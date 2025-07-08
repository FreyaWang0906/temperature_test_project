# Test Plan

## 1. Project Name
Temperature Sensor Automated Testing System

## 2. Objective
To verify the functional correctness and robustness of the system across all major modules:
- Data simulation (temperature generation),
- Error diagnosis (classification of temperature anomalies),
- Report generation (summary export and statistical analysis).

## 3. Scope of Testing
### Included:
- Validity of generated temperature data (format, range)
- Accuracy of error classification logic (boundary values, unstable readings)
- Integrity and completeness of generated reports

### Excluded:
- Real hardware communication (this project uses simulated data)
- User interface (non-UI project)

## 4. Testing Methods
- Unit Testing (via Pytest)
- Black-box testing (edge cases, type errors, invalid inputs)
- Automated CI Testing (via GitHub Actions)

## 5. Input Data
- Simulated temperature logs in CSV format
- Manually crafted arrays for edge testing 

## 6. Expected Output
- Diagnosed categories: `Too Cold`, `Normal`, `Too Hot`, `Unstable`
- Report file (CSV/Excel) including timestamped results and diagnosis summary

## 7. Pass Criteria

| Test Item         | Pass Condition |
|-------------------|----------------|
| Data Simulation   | CSV file generated successfully with correct record count |
| Error Diagnosis   | All input values receive a valid diagnosis without crashes |
| Report Generation | Output file created, includes results + valid summary statistics |

## 8. Environment
- OS: macOS 
- Python: 3.9.7
- Testing Framework: Pytest
- CI Tool: GitHub Actions

## 9. Test Owner
Freya (Author and Test Engineer)

## 10. Risks & Considerations
- Must handle empty, malformed, or extreme-value inputs
- Preserve clean state between test runs (no residual state leaks)
