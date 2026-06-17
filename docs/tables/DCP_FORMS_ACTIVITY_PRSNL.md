# DCP_FORMS_ACTIVITY_PRSNL

> List all prsnl that have contributed to a form

**Description:** DCP FORMS ACTIVITY PRSNL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date/Time person contributed. |
| 2 | `ACTIVITY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 3 | `DCP_FORMS_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Activity form that the person contributed to. |
| 4 | `DCP_FORMS_ACTIVITY_PRSNL_ID` | DOUBLE | NOT NULL |  | unique identifier |
| 5 | `PROXY_ID` | DOUBLE | NOT NULL | FK→ | Id of proxy prsnl when necessary |
| 6 | `PRSNL_FT` | VARCHAR(100) |  |  | Free Text name of prsnl. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | ID of prsnl |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_FORMS_ACTIVITY_ID` | [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `DCP_FORMS_ACTIVITY_ID` |
| `PROXY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

