# PROT_STRATUM_SUSP

> This table stores information about the suspension of a stratum

**Description:** PROT STRATUM SUSP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COMMENT_TXT` | LONGBLOB |  |  | This field contains any comments about the suspension that were deemed appropriate. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PROT_STRATUM_SUSP_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the prot_stratum_susp table. It is an internal system assigned number. |
| 5 | `REASON_CD` | DOUBLE | NOT NULL |  | This field contains the code that identifies the reason the protocol stratum was suspended. |
| 6 | `STRATUM_ID` | DOUBLE | NOT NULL |  | This field identifies the protocol stratum that was suspended. |
| 7 | `SUSP_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the suspesion begins |
| 8 | `SUSP_END_DT_TM` | DATETIME | NOT NULL |  | The date and time when the suspension ends |
| 9 | `SUSP_ID` | DOUBLE | NOT NULL |  | A logical identifier into the prot_stratum_susp table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

