# ListFeePlanAgreementsRequest


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `account_id`                                                      | *str*                                                             | :heavy_check_mark:                                                | ID of the account.                                                |                                                                   |
| `agreement_id`                                                    | *Optional[str]*                                                   | :heavy_minus_sign:                                                | A comma-separated list of agreement IDs to filter the results by. | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                              |
| `status`                                                          | [Optional[models.AgreementStatus]](../models/agreementstatus.md)  | :heavy_minus_sign:                                                | A comma-separated list of statuses to filter the results by.      | active                                                            |