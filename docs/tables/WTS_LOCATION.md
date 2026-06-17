# WTS_LOCATION

> This table is a reference table for WTS Location program configuration settings. It will hold all solution configuration settings.

**Description:** WTS Location configuration settings  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIGURATION_NAME` | VARCHAR(100) | NOT NULL |  | The configuration option name |
| 2 | `CONFIGURATION_VALUE_TXT` | VARCHAR(512) | NOT NULL |  | The configuration option value |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WTS_LOCATION_ID` | DOUBLE | NOT NULL |  | Primary Key; Unique number identifying the WTS Location configuration options |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

