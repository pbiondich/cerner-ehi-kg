# OCS_FACILITY_R_HIST

> History- Used to define which synonyms are available for which facility

**Description:** Stores the orderable information for a facility - hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 2 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 3 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 4 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the facility (zero means all facilities) |
| 5 | `OCS_FACILITY_R_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | Identifies the synonym. Foreign Key from ORDER_CATALOG_SYNONYM table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

