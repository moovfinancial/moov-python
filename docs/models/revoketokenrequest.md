# RevokeTokenRequest

Allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `token`                                                                 | *str*                                                                   | :heavy_check_mark:                                                      | String passed to the authorization server to gain access to the system. | i1qxz68gu50zp4i8ceyxqogmq7y0yienm52351c6...                             |
| `token_type_hint`                                                       | [Optional[models.TokenTypeHint]](../models/tokentypehint.md)            | :heavy_minus_sign:                                                      | A hint about the type of the token submitted for revocation             |                                                                         |
| `client_id`                                                             | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | If not specified in `Authorization: Basic` it can be specified here     | 5clTR_MdVrrkgxw2                                                        |
| `client_secret`                                                         | *OptionalNullable[str]*                                                 | :heavy_minus_sign:                                                      | If not specified in `Authorization: Basic` it can be specified here     | dNC-hg7sVm22jc3g_Eogtyu0_1Mqh_4-                                        |