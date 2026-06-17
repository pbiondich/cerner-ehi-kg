# WH_BR_GROUP_RELTN

> group relations

**Description:** WH_BR_GROUP_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_GROUP_ID` | DOUBLE | NOT NULL |  | The group that is related to the other object in this relationship. |
| 2 | `BR_GROUP_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_GROUP_RELTN table. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time in which an ETL extract was run |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that idenitifes health system |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that idenitifes health system source |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id for the item that belongs in the group. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table for the item being placed in the group. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_USER` | VARCHAR(40) |  |  | The ETL process that updated the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

