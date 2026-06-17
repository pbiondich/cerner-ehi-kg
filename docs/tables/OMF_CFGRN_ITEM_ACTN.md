# OMF_CFGRN_ITEM_ACTN

> Action(s) associated with a configuration item.

**Description:** OMF Configuration Item Action  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTN_FLAG` | DOUBLE | NOT NULL |  | The action type for this item/sequence pairing. |
| 2 | `CFGRN_ITEM_ACTN_ID` | DOUBLE | NOT NULL |  | The unique identifier of the item associated with this configuration action. |
| 3 | `CFGRN_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the Configuration Item. |
| 4 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Sequences multiple actions for an item. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VAL1` | VARCHAR(255) |  |  | Almost always a script to be executed by an action. May also be a value passed in to action script. |
| 11 | `VAL2` | VARCHAR(255) |  |  | Passed in string value to action script. |
| 12 | `VAL3` | VARCHAR(255) |  |  | Passed in string value to action script. |
| 13 | `VAL4` | VARCHAR(255) |  |  | Passed in string value to action script. |
| 14 | `VAL5` | VARCHAR(255) |  |  | Passed in string value to action script. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CFGRN_ITEM_ID` | [OMF_CFGRN_ITEM](OMF_CFGRN_ITEM.md) | `CFGRN_ITEM_ID` |

