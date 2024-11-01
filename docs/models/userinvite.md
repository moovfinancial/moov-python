# UserInvite

Information about an invitation sent to the user


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `invite_id`                                                          | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | UUID v4                                                              | ec7e1848-dc80-4ab0-8827-dd7fc0737b43                                 |
| `account_id`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | ID of account.                                                       |                                                                      |
| `display_name`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Descriptive name allowing spaces.                                    | Amanda Yang                                                          |
| `email`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Email address.                                                       | amanda@classbooker.dev                                               |
| `expires_on`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |                                                                      |