# Setup

Properties for password authentication


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Base64 string of data.                                              | U3dhZ2dlciByb2Nrcw==                                                |
| `password`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Describes a password for a user                                     | horse Battery st@ple 123                                            |
| `given_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name this person was given. This is usually the same as first name. | Amanda                                                              |
| `family_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Family name of this person. This is usually the same as last name.  | Yang                                                                |
| `fingerprint`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Device hash generated by a frontend library.                        | fBkwz3q43jlTHB8wFtiDgxT0WMpjUmDvMsTbQbz1                            |