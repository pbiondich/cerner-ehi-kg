# PFT_REPORT_INSTANCE

> This activity table stores information about a specific instance of a report

**Description:** PFT REPORT INSTANCE  
**Table type:** ACTIVITY  
**Primary key:** `PFT_REPORT_INSTANCE_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | Date/Time that report instance was created |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `ERROR_IND` | DOUBLE | NOT NULL |  | Indicates error running reports |
| 9 | `ERROR_MSG` | VARCHAR(2000) |  |  | Error message from executing report |
| 10 | `INSTANCE_NAME` | VARCHAR(250) |  |  | Name of report from event param |
| 11 | `ITEM_STATUS_CD` | DOUBLE | NOT NULL |  | Current state of the custom batch entity |
| 12 | `PARAMS_VALUE` | VARCHAR(2000) |  |  | Value of param string passed into pft_run_report |
| 13 | `PERSISTENT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the report file associated with this instance is persistent |
| 14 | `PFT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Pft_Event table |
| 15 | `PFT_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Pft_Report table |
| 16 | `PFT_REPORT_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique identifier of this table |
| 17 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the Person table |
| 18 | `RETENTION_DAYS` | DOUBLE | NOT NULL |  | Number of days the persistent report file is kept on system |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_EVENT_ID` | [PFT_EVENT](PFT_EVENT.md) | `PFT_EVENT_ID` |
| `PFT_REPORT_ID` | [PFT_REPORT](PFT_REPORT.md) | `PFT_REPORT_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `PFT_REPORT_INSTANCE_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `PFT_REPORT_INSTANCE_ID` |
| [PFT_RPT_BLOB_RELTN](PFT_RPT_BLOB_RELTN.md) | `PFT_REPORT_INSTANCE_ID` |

