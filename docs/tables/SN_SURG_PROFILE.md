# SN_SURG_PROFILE

> Surgeon Profile for storing surgeon specific data used in surgical cases (pref cards, picklist, comments, etc.)

**Description:** SurgiNet Surgeon Profile  
**Table type:** REFERENCE  
**Primary key:** `SN_SURG_PROFILE_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The Date and Time the profile was marked active or inactive; |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_PRSNL_ID` | DOUBLE |  | FK→ | The personnel who marked the profile as active or inactive; |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Date and Time the Surgeon Profile was created; |
| 5 | `CREATE_PRSNL_ID` | DOUBLE |  | FK→ | Personnel who created the surgeon profile; |
| 6 | `PRSNL_ID` | DOUBLE |  | FK→ | Personnel Id for the Surgeon ; |
| 7 | `SN_SURG_PROFILE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SN_SURG_PROFILE_COMMENT](SN_SURG_PROFILE_COMMENT.md) | `SN_SURG_PROFILE_ID` |
| [SN_SURG_PROFILE_LOCK](SN_SURG_PROFILE_LOCK.md) | `SN_SURG_PROFILE_ID` |
| [SN_SURG_PROFILE_MOD_HIST](SN_SURG_PROFILE_MOD_HIST.md) | `SN_SURG_PROFILE_ID` |

