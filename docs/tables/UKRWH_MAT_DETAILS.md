# UKRWH_MAT_DETAILS

> Contains maternity pregnanacy and birth activity details

**Description:** UKRWH_MAT_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | First date/time row was inserted into table. |
| 3 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | Last date/time row was updated. |
| 6 | `MAT_DETAIL_TYPE_DESC` | VARCHAR(40) |  |  | Maternity activity name |
| 7 | `MAT_DETAIL_TYPE_FLG` | DOUBLE |  |  | Maternity activity type flag |
| 8 | `PARENT_ENTITY_KEY` | DOUBLE |  |  | PIEDW system generated unique identifier for a pregnancy or birth |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Parent type of entity - Pregnancy or Birth |
| 10 | `PARENT_ENTITY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy or birth |
| 11 | `SEQUENCE` | DOUBLE |  |  | Sequence of occurrence |
| 12 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 13 | `UKRWH_MAT_DETAILS_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MAT_DETAILS table. |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `UPDT_USER` | VARCHAR(100) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `VALUE` | VARCHAR(100) |  |  | Reference value for activity |
| 19 | `VALUE_TYPE_DESC` | VARCHAR(40) |  |  | Reference value type Snowmed - Nomenclature or code value |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

