# BR_PREFS

> Reference data for preferences.

**Description:** BR_PREFS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_NAME` | VARCHAR(200) | NOT NULL |  | The name for a preference. |
| 2 | `BR_PREFS_ID` | DOUBLE | NOT NULL |  | The primary key for the BR_PREFS table. |
| 3 | `CODE_LEVEL` | VARCHAR(100) |  |  | The code level the preference became available. |
| 4 | `DEFAULT_VALUE` | VARCHAR(256) |  |  | Some preferences have default values to display. This column holds the default value. |
| 5 | `PARENT_PREFS_ID` | DOUBLE | NOT NULL |  | A group of preferences can be stored under a single preference. This column holds the parent's BR_PREFS_ID. |
| 6 | `PVC_NAME` | VARCHAR(100) | NOT NULL |  | The pvc_name for a preference. |
| 7 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of preference. Font size, DLL, row, column, etc. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIEW_NAME` | VARCHAR(100) |  |  | The view a preference is available for. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

