# Versions

Moov API versions. 

API versioning follows the format `vYYYY.QQ.BB`, where 
  - `YYYY` is the year
  - `QQ` is the two-digit month for the first month of the quarter (e.g., 01, 04, 07, 10)
  - `BB` is an optional build number starting at `.01` for subsequent builds in the same quarter. 
    - If no build number is specified, the version refers to the initial release of the quarter.

The `latest` version represents the most recent development state. It may include breaking changes and should be treated as a beta release.


## Values

| Name       | Value      |
| ---------- | ---------- |
| `V2024_01` | v2024.01   |
| `V2025_01` | v2025.01   |
| `V2025_04` | v2025.04   |
| `V2025_07` | v2025.07   |
| `V2025_10` | v2025.10   |
| `LATEST`   | latest     |