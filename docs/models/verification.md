# Verification

Describes identity verification status and relevant identity verification documents.


## Fields

| Field                                                                                                                                                                                      | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ~~`status`~~                                                                                                                                                                               | [models.VerificationStatus](../models/verificationstatus.md)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated and will be removed in a future release. |
| ~~`verification_status`~~                                                                                                                                                                  | [Optional[models.AccountVerificationStatus]](../models/accountverificationstatus.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated and will be removed in a future release. |
| ~~`details`~~                                                                                                                                                                              | [Optional[models.VerificationStatusDetails]](../models/verificationstatusdetails.md)                                                                                                       | :heavy_minus_sign:                                                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>This field is deprecated and will be removed in a future release. |
| `documents`                                                                                                                                                                                | List[[models.Document](../models/document.md)]                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                         | N/A                                                                                                                                                                                        |