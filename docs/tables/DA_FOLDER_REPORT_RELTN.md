# DA_FOLDER_REPORT_RELTN

> Defines the relationship between Reports and folders in Discern Analytics 2.0.

**Description:** Discern Analytics Folder Report Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_FOLDER_ID` | DOUBLE | NOT NULL | FK→ | The folder that this report resides in. |
| 2 | `DA_FOLDER_REPORT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_FOLDER_REPORT_RELTN table. |
| 3 | `DA_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Report that resides in this folder. |
| 4 | `REPORT_ALIAS_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Report as it will be shown in the folder. |
| 5 | `REPORT_SERVICE_CD` | DOUBLE | NOT NULL |  | reference to code set 4000601 (ccl report service bindings). a default of 0.0 indicates the cpmscriptbatch service is used for this report object. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEWER_MODE_CD` | DOUBLE | NOT NULL |  | reference to code set 4002472 (da2 object types). A default of 0.0 indicates the standard da2 report viewer will be used to display reports. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_FOLDER_ID` | [DA_FOLDER](DA_FOLDER.md) | `DA_FOLDER_ID` |
| `DA_REPORT_ID` | [DA_REPORT](DA_REPORT.md) | `DA_REPORT_ID` |

