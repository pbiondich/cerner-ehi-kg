# IMPLANT_HISTORY_REVIEW

> This table tracks the review of the items that are permanently implanted in the patient

**Description:** IMPLANT_HISTORY_REVIEW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `IMPLANT_HISTORY_ID` | DOUBLE | NOT NULL | FK→ | implant_history_id from implant_history table |
| 3 | `IMPLANT_HISTORY_REVIEW_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Provider who reviewed an implanted Item |
| 5 | `REVIEW_DT_TM` | DATETIME |  |  | Indicates the review date time |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMPLANT_HISTORY_ID` | [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `IMPLANT_HISTORY_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

