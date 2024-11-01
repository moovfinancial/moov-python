<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from moov import Moov
import os

s = Moov(
    gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
)

res = s.signup.self_signup(request={
    "email": "amanda@classbooker.dev",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from moov import Moov
import os

async def main():
    s = Moov(
        gateway_auth=os.getenv("MOOV_GATEWAY_AUTH", ""),
    )
    res = await s.signup.self_signup_async(request={
        "email": "amanda@classbooker.dev",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->