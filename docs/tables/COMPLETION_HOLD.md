# COMPLETION_HOLD

> Store hold start time, hold stop time, hold reason, hold type, etc for each completion hold

**Description:** Stores hold information based on hold type  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMPLETION_HOLD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the completion hold table. It is an internal system assigned number. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the clinical_event table. It is an internal system assigned number. |
| 10 | `HOLD_REASON_CD` | DOUBLE | NOT NULL |  | This is the reason the hold was created |
| 11 | `HOLD_START_DT_TM` | DATETIME |  |  | This is the date and time that the hold is started |
| 12 | `HOLD_STOP_DT_TM` | DATETIME |  |  | This is the date and time that the hold will stop |
| 13 | `HOLD_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of hold that this is (i.e. physician, document, request or, visit) |
| 14 | `MEDIA_MASTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number. |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 16 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | This is the physician on hold. This is the value of the unique primary identifier of the prsnl table. It is an internal system assigned number. |
| 17 | `REQUEST_ID` | DOUBLE | NOT NULL |  | this is the value of the unique prinary identifier to the ROI request table. It is an internal system assigned number. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

