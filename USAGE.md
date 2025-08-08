<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime


with Moov(
    x_moov_version="v2024.01.00",
    security=components.Security(
        username="",
        password="",
    ),
) as moov:

    res = moov.accounts.create(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
        business=components.CreateBusinessProfile(
            legal_business_name="Whole Body Fitness LLC",
        ),
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://esteemed-velocity.net",
    }, customer_support={
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "jordan.lee@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "address_line2": "Apt 302",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
        },
    }, settings={
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    }, mode=components.Mode.PRODUCTION)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from moovio_sdk import Moov
from moovio_sdk.models import components
from moovio_sdk.utils import parse_datetime

async def main():

    async with Moov(
        x_moov_version="v2024.01.00",
        security=components.Security(
            username="",
            password="",
        ),
    ) as moov:

        res = await moov.accounts.create_async(account_type=components.CreateAccountType.BUSINESS, profile=components.CreateProfile(
            business=components.CreateBusinessProfile(
                legal_business_name="Whole Body Fitness LLC",
            ),
        ), metadata={
            "optional": "metadata",
        }, terms_of_service={
            "accepted_date": parse_datetime("2023-05-21T04:53:54.554Z"),
            "accepted_ip": "172.217.2.46",
            "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
            "accepted_domain": "https://esteemed-velocity.net",
        }, customer_support={
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "jordan.lee@classbooker.dev",
            "address": {
                "address_line1": "123 Main Street",
                "address_line2": "Apt 302",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
            },
        }, settings={
            "card_payment": {
                "statement_descriptor": "Whole Body Fitness",
            },
            "ach_payment": {
                "company_name": "WholeBodyFitness",
            },
        }, mode=components.Mode.PRODUCTION)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->