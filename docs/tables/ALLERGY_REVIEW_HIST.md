# ALLERGY_REVIEW_HIST

> This table is used to store Allergy Review History information for each instance of the Allergy . This project involves displaying Reviewed date and time , reviewed prsnl name for each instance of the allergy.

**Description:** Allergy Review History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLERGY_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | Instance id of the Allergy of which are storing review history |
| 2 | `ALLERGY_REVIEW_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `REVIEWED_DT_TM` | DATETIME | NOT NULL |  | Reviewed date and time |
| 4 | `REVIEWED_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the prsnl who reviewed the allergy |
| 5 | `REVIEWED_TZ` | DOUBLE |  |  | Reviewed date time zone |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALLERGY_INSTANCE_ID` | [ALLERGY](ALLERGY.md) | `ALLERGY_INSTANCE_ID` |

