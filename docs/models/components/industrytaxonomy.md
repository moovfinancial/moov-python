# IndustryTaxonomy

A structured industry taxonomy entry with category and mapped to a default MCC code.


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `industry`                           | *str*                                | :heavy_check_mark:                   | URL-safe identifier for the industry | clothing-accessories                 |
| `display_name`                       | *str*                                | :heavy_check_mark:                   | Display name of the industry         | Clothing & Accessories               |
| `category`                           | *str*                                | :heavy_check_mark:                   | Category slug                        | retail                               |
| `category_display_name`              | *str*                                | :heavy_check_mark:                   | Human-readable category label        | Retail                               |
| `default_mcc`                        | *str*                                | :heavy_check_mark:                   | Default Merchant Category Code       | 5651                                 |