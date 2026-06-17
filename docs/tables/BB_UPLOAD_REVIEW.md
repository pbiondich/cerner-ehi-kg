# BB_UPLOAD_REVIEW

> This table will be used to track errors during the history upload of person ABO/Rh's. When an error occurs with the upload, one row will be written to this table.

**Description:** BB Upload Review  
**Table type:** ACTIVITY  
**Primary key:** `BB_UPLOAD_REVIEW_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_UPLOAD_REVIEW_ID` | DOUBLE | NOT NULL | PK | An internal system-assigned number that ensures the uniqueness of each row. |
| 2 | `DEMOG_ABORH_DT_TM` | DATETIME |  |  | Date/Time the demographic ABO/Rh was last resulted or uploaded. |
| 3 | `DEMOG_PERSON_ABORH_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier to the person_aborh table for the previous ABO/Rh value that was inactivated. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `REVIEWED_IND` | DOUBLE | NOT NULL |  | An indicator showing if this row has been reviewed. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPLOAD_DT_TM` | DATETIME | NOT NULL |  | Date/Time the upload occurred. |
| 12 | `UPLOAD_PERSON_ABORH_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique identifier to the person_aborh table for the ABO/Rh value uploaded. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEMOG_PERSON_ABORH_ID` | [PERSON_ABORH](PERSON_ABORH.md) | `PERSON_ABORH_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UPLOAD_PERSON_ABORH_ID` | [PERSON_ABORH](PERSON_ABORH.md) | `PERSON_ABORH_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_UPLOAD_LONG_TEXT_R](BB_UPLOAD_LONG_TEXT_R.md) | `BB_UPLOAD_REVIEW_ID` |
| [BB_UPLOAD_PERSON_ABORH_R](BB_UPLOAD_PERSON_ABORH_R.md) | `BB_UPLOAD_REVIEW_ID` |

