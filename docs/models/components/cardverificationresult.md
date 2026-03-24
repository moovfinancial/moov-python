# CardVerificationResult

The result of a card verification check.

## Example Usage

```python
from moovio_sdk.models.components import CardVerificationResult

value = CardVerificationResult.NO_MATCH
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `NO_MATCH`      | noMatch         |
| `MATCH`         | match           |
| `NOT_CHECKED`   | notChecked      |
| `UNAVAILABLE`   | unavailable     |
| `PARTIAL_MATCH` | partialMatch    |