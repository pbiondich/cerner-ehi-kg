# SN_SURG_PROFILE_MOD_HIST

> Contains history of who and when changes were made to a surgeons profile

**Description:** SurgiNet Surgeon Profile Modify History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODIFY_DT_TM` | DATETIME |  |  | Date and Time a modification was made to the surgeons profile; |
| 2 | `MODIFY_LOCK_ID` | DOUBLE |  | FK→ | The surgeon profile lock that was used to make the modification; |
| 3 | `MODIFY_PRSNL_ID` | DOUBLE |  | FK→ | User who made a modification to a surgeons profile; |
| 4 | `MODIFY_TYPE_FLAG` | DOUBLE |  |  | The type of data that was modified on the surgeons profile; |
| 5 | `SN_SURG_PROFILE_ID` | DOUBLE |  | FK→ | Surgeon Profile associated to the modification history; |
| 6 | `SN_SURG_PROFILE_MOD_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_LOCK_ID` | [SN_SURG_PROFILE_LOCK](SN_SURG_PROFILE_LOCK.md) | `SN_SURG_PROFILE_LOCK_ID` |
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_SURG_PROFILE_ID` | [SN_SURG_PROFILE](SN_SURG_PROFILE.md) | `SN_SURG_PROFILE_ID` |

