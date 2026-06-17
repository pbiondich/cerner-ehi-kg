# MARS_SUITE_RESPONSE

> Identifies an execution Response of a suite.

**Description:** MARS Suite Response  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `MARS_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Report this response applies to |
| 6 | `MARS_SUITE_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the specific execution of a suite of reports |
| 7 | `MARS_SUITE_RESPONSE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `MARS_TYPE_CD` | DOUBLE |  |  | TBD - currently the code value isn't tied to anything. We plan to leave it as we expect there will be a use for it |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique person/patient ID from the PERSON table |
| 10 | `RESPONSE_BLOB` | LONGBLOB |  |  | Report output - XML if the report completes successfully. A message as to the nature of the failure if unsuccessful. |
| 11 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status of the report execution. On Success the Blob will contain the XML output. |
| 12 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_REPORT_ID` | [MARS_REPORT](MARS_REPORT.md) | `MARS_REPORT_ID` |
| `MARS_SUITE_ACTIVITY_ID` | [MARS_SUITE_ACTIVITY](MARS_SUITE_ACTIVITY.md) | `MARS_SUITE_ACTIVITY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

