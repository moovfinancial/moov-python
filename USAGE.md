<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import dateutil.parser
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

with Moov() as moov:

    res = moov.accounts.create_account(security=operations.CreateAccountSecurity(
        basic_auth=components.SchemeBasicAuth(
            username="",
            password="",
        ),
    ), account_type=components.AccountType.BUSINESS, profile=components.CreateProfile(
        business={
            "legal_business_name": "Classbooker, LLC",
        },
    ), metadata={
        "optional": "metadata",
    }, terms_of_service={
        "accepted_date": dateutil.parser.isoparse("2024-02-09T13:16:05.687Z"),
        "accepted_ip": "172.217.2.46",
        "accepted_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accepted_domain": "https://remorseful-finger.name/",
    }, customer_support={
        "phone": {
            "number": "8185551212",
            "country_code": "1",
        },
        "email": "jordan.lee@classbooker.dev",
        "address": {
            "address_line1": "123 Main Street",
            "city": "Boulder",
            "state_or_province": "CO",
            "postal_code": "80301",
            "country": "US",
            "address_line2": "Apt 302",
        },
    }, settings={
        "card_payment": {
            "statement_descriptor": "Whole Body Fitness",
        },
        "ach_payment": {
            "company_name": "WholeBodyFitness",
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from moovio_sdk import Moov
from moovio_sdk.models import components, operations

async def main():
    async with Moov() as moov:

        res = await moov.accounts.create_account_async(security=operations.CreateAccountSecurity(
            basic_auth=components.SchemeBasicAuth(
                username="",
                password="",
            ),
        ), account_type=components.AccountType.BUSINESS, profile=components.CreateProfile(
            business={
                "legal_business_name": "Classbooker, LLC",
            },
        ), metadata={
            "optional": "metadata",
        }, terms_of_service={
            "token": "kgT1uxoMAk7QKuyJcmQE8nqW_HjpyuXBabiXPi6T83fUQoxsyWYPcYzuHQTqrt7YRp4gCwyDQvb6U5REM9Pgl2EloCe35t-eiMAbUWGo3Kerxme6aqNcKrP_6-v0MTXViOEJ96IBxPFTvMV7EROI2dq3u4e-x4BbGSCedAX-ViAQND6hcreCDXwrO6sHuzh5Xi2IzSqZHxaovnWEboaxuZKRJkA3dsFID6fzitMpm2qrOh4",
        }, customer_support={
            "phone": {
                "number": "8185551212",
                "country_code": "1",
            },
            "email": "jordan.lee@classbooker.dev",
            "address": {
                "address_line1": "123 Main Street",
                "city": "Boulder",
                "state_or_province": "CO",
                "postal_code": "80301",
                "country": "US",
                "address_line2": "Apt 302",
            },
        }, settings={
            "card_payment": {
                "statement_descriptor": "Whole Body Fitness",
            },
            "ach_payment": {
                "company_name": "WholeBodyFitness",
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->