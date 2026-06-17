# CV_XREF_VALIDATION

> THE Xref Validation table

**Description:** Xref Validation table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHILD_RESPONSE_ID` | DOUBLE | NOT NULL |  | Child Response idColumn |
| 7 | `CHILD_XREF_ID` | DOUBLE | NOT NULL |  | Child Xref idColumn |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `OFFSET_NBR` | DOUBLE |  |  | Used to get the offset for the Parent or the Child depending on the Relationship flag. For dates it is expressed in days |
| 10 | `REQD_FLAG` | DOUBLE |  |  | Sets the log level |
| 11 | `RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key . It the unique identifier to cv_response table |
| 12 | `RLTNSHIP_FLAG` | DOUBLE |  |  | Relationship FlagColumn |
| 13 | `UPDT_APP` | DOUBLE |  |  | The application number that is responsible for the row update. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_REQ` | DOUBLE |  |  | The registered (assigned)request number for the process that inserted or updated the row. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `XREF_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to this table. Xref_id is the unique row identifier for Cv_xref table |
| 21 | `XREF_VALIDATION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the cv_xref_validation. It is an internal system assigned number |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESPONSE_ID` | [CV_RESPONSE](CV_RESPONSE.md) | `RESPONSE_ID` |
| `XREF_ID` | [CV_XREF](CV_XREF.md) | `XREF_ID` |

