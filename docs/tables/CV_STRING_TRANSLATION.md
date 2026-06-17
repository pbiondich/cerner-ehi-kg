# CV_STRING_TRANSLATION

> Stores mapping between strings and corresponding cerner values.

**Description:** String Translation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERNER_VAL` | VARCHAR(250) | NOT NULL |  | Cerner value for string information. |
| 2 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Name of the source contributor. |
| 3 | `CONTRIBUTOR_VAL` | VARCHAR(250) | NOT NULL |  | Contributor value for string information. |
| 4 | `CV_STRING_TRANSLATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CV_STRING_TRANSLATION table. |
| 5 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Type of string information. It can Medication or Provider information. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

