# STAFF_ACTIVITY

> Used by SNStaffAssign

**Description:** Staff Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and TimeColumn |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Create Personnel IdColumn |
| 3 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 4 | `CREAT_APPLCTX` | DOUBLE |  |  | Create Application ContextColumn |
| 5 | `FREE_TEXT_NAME` | VARCHAR(100) | NOT NULL |  | Free text nameColumn |
| 6 | `METHOD_FLAG` | DOUBLE |  |  | Method Flag. Possible values are: null = Assign by case; 1 = Assign by case; 2 = Assign by OR; 3 = Assign by Team |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_ID of the staff assigned |
| 8 | `ROLE_CD` | DOUBLE | NOT NULL |  | Role of the assigned staff |
| 9 | `SHIFT_CD` | DOUBLE | NOT NULL |  | Shift Code the staff is assigned to |
| 10 | `STAFF_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Staff Activity IdColumn |
| 11 | `START_DT_TM` | DATETIME | NOT NULL |  | The activity Start Date and Time |
| 12 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 13 | `STOP_DT_TM` | DATETIME | NOT NULL |  | The activity Stop Date and Time |
| 14 | `STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Surgical Area Cd for the associated staff activity |
| 16 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case ID the staff is assigned to |
| 17 | `SURG_OP_LOC_CD` | DOUBLE | NOT NULL |  | OR the staff is assigned to |
| 18 | `TEAM_CD` | DOUBLE | NOT NULL |  | Team the staff is associated to |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

