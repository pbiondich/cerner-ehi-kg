# TL_TAB_MEDICATION

> Holds all specific medications for a specific tab for the tasklist.

**Description:** TL TAB MEDICATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog_cd from the orders table that identifies a specific medication.Column |
| 2 | `ORDER_CATALOG_DESCRIPTION` | VARCHAR(100) |  |  | The description of the specific medication identified by the catalog_cd.Column |
| 3 | `TL_TAB_ID` | DOUBLE | NOT NULL | FK→ | A unique, generated number that identifies a specific tab.Column |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TL_TAB_ID` | [TL_TAB_CONTENT](TL_TAB_CONTENT.md) | `TL_TAB_ID` |

