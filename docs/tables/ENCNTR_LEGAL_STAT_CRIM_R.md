# ENCNTR_LEGAL_STAT_CRIM_R

> This table will hold the relationship between legal statuses and criminal codes.

**Description:** Encounter legal status criminal relation.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRIMINAL_CD` | DOUBLE | NOT NULL |  | The facility defined criminal code. |
| 2 | `LEGAL_STATUS_CRIMINAL_R_ID` | DOUBLE | NOT NULL |  | The unique identifier for the encntr_legal_stat_crim_r table. |
| 3 | `LEGAL_STATUS_R_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the encntr_legal_status_r table. |
| 4 | `OCCURRENCES_NBR` | DOUBLE |  |  | The number of occurrences of the offense. |
| 5 | `OFFENSE_DT_TM` | DATETIME |  |  | The date and time of the offense. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LEGAL_STATUS_R_ID` | [ENCNTR_LEGAL_STATUS_R](ENCNTR_LEGAL_STATUS_R.md) | `LEGAL_STATUS_R_ID` |

