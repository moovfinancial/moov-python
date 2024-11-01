# UpdateIssuedCard


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `state`                                                                            | [Optional[models.UpdateIssuedCardState]](../models/updateissuedcardstate.md)       | :heavy_minus_sign:                                                                 | Updates the state of a Moov issued card. Currently only supports the closed state. |
| `memo`                                                                             | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | Optional descriptive name.                                                         |
| `authorized_user`                                                                  | [Optional[models.CreateAuthorizedUser]](../models/createauthorizeduser.md)         | :heavy_minus_sign:                                                                 | Fields for identifying an authorized individual.                                   |