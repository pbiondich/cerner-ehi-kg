# OMF_CFGRN_ITEM_SETNG

> Current option setting for each configuration item.

**Description:** OMF Configuration Item Setting  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CFGRN_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the configuration item. |
| 2 | `CFGRN_ITEM_SETNG_ID` | DOUBLE | NOT NULL |  | The system assigned unique identifier for the item setting. |
| 3 | `CUR_ITEM_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | The current option value. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CFGRN_ITEM_ID` | [OMF_CFGRN_ITEM](OMF_CFGRN_ITEM.md) | `CFGRN_ITEM_ID` |

