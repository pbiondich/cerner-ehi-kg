# IM_DEVICE_MWL_RULE_R

> The im_device_mwl_rule_r table associates devices with mwl rules. A single device can only be associated with a single mwl rule, and a single mwl rule may be associated with multiple devices.

**Description:** Imaging Device MWL Rule Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | The device, such as a modality device, for which service resource is to be associated. Foreign key to im_device table. |
| 2 | `IM_DEVICE_MWL_RULE_R_ID` | DOUBLE | NOT NULL |  | IM DEVICE MWL RULE REALTION TABLE |
| 3 | `IM_MWL_RULE_ID` | DOUBLE | NOT NULL |  | The Modality Worklist Rule, for which device is to be associated. Foreign key to im_mwl_rule table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |

