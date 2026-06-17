# SA_DISPLAY_RESULT

> Contains records that document when results are available to be displayed in an anesthesia record and who/when they were viewed Based on the # of results (labs,etc) that are resulted while the patient is in the OR. Estimate 2:1 with SA_ANESTHESIA_RECORD . 52,200

**Description:** SA Display Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The clinical_event_id to the result that is being displayed |
| 6 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The anesthesia record that the result was displayed on |
| 7 | `SA_DISPLAY_RESULT_ID` | DOUBLE | NOT NULL |  | Unique value that identifies the result being displayed |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `VIEWED_DT_TM` | DATETIME |  |  | The date/time the result was viewed |
| 14 | `VIEWED_IND` | DOUBLE |  |  | Indicates whether the user viewed the result or not (1=viewed, 0=not viewed) |
| 15 | `VIEWED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user that viewed the result |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_EVENT_ID` | [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CLINICAL_EVENT_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |
| `VIEWED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

