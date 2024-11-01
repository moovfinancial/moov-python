# AccountCapability

Describes an action or set of actions that an account is permitted to perform.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `capability`                                                       | [Optional[models.CapabilityID]](../models/capabilityid.md)         | :heavy_minus_sign:                                                 | Identifier for the capability.                                     |
| `status`                                                           | [Optional[models.CapabilityStatus]](../models/capabilitystatus.md) | :heavy_minus_sign:                                                 | The status of the capability requested for an account.             |