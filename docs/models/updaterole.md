# UpdateRole

Arguments to update an existing role.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Descriptive name allowing spaces.                  | Amanda Yang                                        |
| `subjects`                                         | List[*str*]                                        | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `policies`                                         | List[[models.RolePolicy](../models/rolepolicy.md)] | :heavy_check_mark:                                 | N/A                                                |                                                    |