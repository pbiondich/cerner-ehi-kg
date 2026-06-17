# MSG_CFG_CAT_RELTN

> Defines which categories are related to a configuration

**Description:** Messaging Configuration Category Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MSG_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Message Catgetory ID |
| 2 | `MSG_CFG_CAT_R_ID` | DOUBLE | NOT NULL |  | Primary key |
| 3 | `MSG_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | Message Config ID |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_CATEGORY_ID` | [MSG_CATEGORY](MSG_CATEGORY.md) | `MSG_CATEGORY_ID` |
| `MSG_CONFIG_ID` | [MSG_CONFIG](MSG_CONFIG.md) | `MSG_CONFIG_ID` |

