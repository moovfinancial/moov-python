# IssuingAuthorizationStatus

Status of a card issuing authorization.

## Example Usage

```python
from moovio_sdk.models.components import IssuingAuthorizationStatus

value = IssuingAuthorizationStatus.PENDING
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `DECLINED` | declined   |
| `CANCELED` | canceled   |
| `CLEARED`  | cleared    |
| `EXPIRED`  | expired    |