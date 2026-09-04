# CreateBankAccountAttestation

Request body for creating a R29 re-authorization attestation for an errored bank account.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `attested_at`                                                                            | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)             | :heavy_check_mark:                                                                       | Date on which new authorization was obtained from the receiver, formatted as YYYY-MM-DD. | 2026-05-15                                                                               |
| `description`                                                                            | *str*                                                                                    | :heavy_check_mark:                                                                       | Freeform text description describing how the authorization was obtained.                 |                                                                                          |