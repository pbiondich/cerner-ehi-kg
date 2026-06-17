# WH_BR_GROUP

> This table Used to group a generic set of items.

**Description:** WH_BR_GROUP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_GROUP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_GROUP table. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date and time for which first ETL extract was run |
| 4 | `GROUP_NAME` | VARCHAR(100) |  |  | The name that identifies the group. |
| 5 | `GROUP_TYPE_FLAG` | DOUBLE |  |  | The type of group. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date and time for which the record was last processed on the clearing house side |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performs the insert or update to the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

