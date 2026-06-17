# BB_UPLOAD_PERSON_ABORH_R

> This table will be used in the case where multiple, active ABO/Rh rows where found prior to an upload. There will be one row per active ABO/Rh rows.

**Description:** BB Upload Person ABO/Rh  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_UPLOAD_PERSON_ABORH_R_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number that ensures the uniqueness of each row. |
| 2 | `BB_UPLOAD_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier to the bb_upload_review table. |
| 3 | `DEMOG_ABORH_DT_TM` | DATETIME | NOT NULL |  | Tells when the demographic ABO/Rh was last resulted/uploaded. |
| 4 | `PERSON_ABORH_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier for a previously active ABO/Rh row. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_UPLOAD_REVIEW_ID` | [BB_UPLOAD_REVIEW](BB_UPLOAD_REVIEW.md) | `BB_UPLOAD_REVIEW_ID` |
| `PERSON_ABORH_ID` | [PERSON_ABORH](PERSON_ABORH.md) | `PERSON_ABORH_ID` |

