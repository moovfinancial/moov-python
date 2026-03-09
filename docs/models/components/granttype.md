# GrantType

The type of grant being requested.

  - `client_credentials`: A grant type used by clients to obtain an access token
  - `refresh_token`: A grant type used by clients to obtain a new access token using a refresh token

## Example Usage

```python
from moovio_sdk.models.components import GrantType

value = GrantType.CLIENT_CREDENTIALS
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `CLIENT_CREDENTIALS` | client_credentials   |
| `REFRESH_TOKEN`      | refresh_token        |