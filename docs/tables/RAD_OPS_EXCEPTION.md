# RAD_OPS_EXCEPTION

> This table contains entries for reports that have not been successfully updated upon signout.

**Description:** Radiology Operations Exception  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | This table contains the key to the clinical event table. It identifies the report. |
| 2 | `FINAL_DT_TM` | DATETIME |  |  | This column contains the date and time that the report was signed out. |
| 3 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | This column contains the foreign key to the rad_report table. It uniquely defines the report that did not process successfully. |
| 4 | `SEVERITY_CD_OCF` | DOUBLE |  |  | This column contains the severity code returned from the event server if an error occurred. |
| 5 | `STATUS_CD_OCF` | DOUBLE |  |  | This column contains the Status_cd returned by the clinical event server if an error has occurred. |
| 6 | `STATUS_TEXT` | VARCHAR(255) |  |  | This column contains the status message returned from the clinical event server if an error has occurred. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |

