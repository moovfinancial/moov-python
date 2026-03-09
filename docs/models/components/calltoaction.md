# CallToAction

The text to be displayed on web form's submit button.

If set to "auto" the UI will automatically select between 
"pay" and "confirm" for payments and payouts respectively.

## Example Usage

```python
from moovio_sdk.models.components import CallToAction

value = CallToAction.PAY
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PAY`       | pay         |
| `BOOK`      | book        |
| `SUBSCRIBE` | subscribe   |
| `DONATE`    | donate      |
| `CONFIRM`   | confirm     |
| `AUTO`      | auto        |