# ResetPassword

Email to send recover instructions to


## Fields

| Field                           | Type                            | Required                        | Description                     | Example                         |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `email`                         | *str*                           | :heavy_check_mark:              | Email address.                  | amanda@classbooker.dev          |
| `token`                         | *str*                           | :heavy_check_mark:              | Base64 string of data.          | U3dhZ2dlciByb2Nrcw==            |
| `password`                      | *str*                           | :heavy_check_mark:              | Describes a password for a user | horse Battery st@ple 123        |