# SCH_ROUTE_LIST

> List the reports associated with a scheduling routing

**Description:** Scheduling Route List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `CHILD_SCH_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier corresponding to the child routing. |
| 8 | `EMAIL` | VARCHAR(100) |  |  | FREE TEXT EMAIL. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NBR_COPIES` | DOUBLE |  |  | The requested number of copies. |
| 11 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 12 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the output destination (printer, fax, etc.) |
| 13 | `SCH_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling report. |
| 14 | `SCH_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a scheduling route. |
| 15 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 16 | `SUFFIX` | VARCHAR(50) |  |  | This field hold the phone number when ad-hoc faxing is used. |
| 17 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the notification should be sent. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_SCH_ROUTE_ID` | [SCH_ROUTE](SCH_ROUTE.md) | `SCH_ROUTE_ID` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `SCH_REPORT_ID` | [SCH_REPORT](SCH_REPORT.md) | `SCH_REPORT_ID` |
| `SCH_ROUTE_ID` | [SCH_ROUTE](SCH_ROUTE.md) | `SCH_ROUTE_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

