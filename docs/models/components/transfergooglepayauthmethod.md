# TransferGooglePayAuthMethod

The authentication method used for the Google Pay token.

## Example Usage

```python
from moovio_sdk.models.components import TransferGooglePayAuthMethod

value = TransferGooglePayAuthMethod.PAN_ONLY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `PAN_ONLY`        | PAN_ONLY          |
| `CRYPTOGRAM_3_DS` | CRYPTOGRAM_3DS    |