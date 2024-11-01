# CreateAuthorizedUser

Fields for identifying an authorized individual.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `first_name`                                         | *str*                                                | :heavy_check_mark:                                   | N/A                                                  | Jane                                                 |
| `last_name`                                          | *str*                                                | :heavy_check_mark:                                   | N/A                                                  | Doe                                                  |
| `birth_date`                                         | [Optional[models.BirthDate]](../models/birthdate.md) | :heavy_minus_sign:                                   | An individual's birthdate.                           |                                                      |