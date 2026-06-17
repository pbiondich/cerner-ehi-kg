# WARNING_LABEL

> Stores Warning Label details which could be associated to drugs/pharmacy medications

**Description:** Warning Label  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LABEL_FULL_TEXT` | VARCHAR(255) |  |  | Full Text of Labels |
| 6 | `LABEL_NBR` | DOUBLE |  |  | Label Number |
| 7 | `LABEL_NBR_SEQ` | DOUBLE | NOT NULL |  | Sequence which will allow multiple rows with the same label_nbr and language_cd to be unique. |
| 8 | `LABEL_TEXT` | VARCHAR(100) |  |  | Truncated Label Text |
| 9 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The language the label_text field is written in. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WARNING_LABEL_ID` | DOUBLE | NOT NULL |  | Warning Label Id |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

