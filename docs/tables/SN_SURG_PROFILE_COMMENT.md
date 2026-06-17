# SN_SURG_PROFILE_COMMENT

> Stores surgeon specific comments used during surgical cases (room setup preferences, sizes, handedness, etc.)

**Description:** SurgiNet Surgeon Profile Comment  
**Table type:** REFERENCE  
**Primary key:** `SN_SURG_PROFILE_COMMENT_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The Date and Time the profile comment version was marked active or inactive; |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_PRSNL_ID` | DOUBLE |  | FK→ | The personnel who marked the profile comment as active or inactive; |
| 4 | `COMMENT_VALUE` | LONGTEXT |  |  | Comment for Surgeon Profile stored in HTML format; |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | Date and Time the Surgeon Profile comment version was created; |
| 6 | `CREATE_PRSNL_ID` | DOUBLE |  | FK→ | Personnel who created the surgeon profile comment version; |
| 7 | `PREV_SURG_PROFILE_COMMENT_ID` | DOUBLE |  | FK→ | Identifies the previous version of the surgeon profile comment ; |
| 8 | `SN_SURG_PROFILE_COMMENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `SN_SURG_PROFILE_ID` | DOUBLE |  | FK→ | Identifies the surgeon profile that this comment belongs to; |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PREV_SURG_PROFILE_COMMENT_ID` | [SN_SURG_PROFILE_COMMENT](SN_SURG_PROFILE_COMMENT.md) | `SN_SURG_PROFILE_COMMENT_ID` |
| `SN_SURG_PROFILE_ID` | [SN_SURG_PROFILE](SN_SURG_PROFILE.md) | `SN_SURG_PROFILE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_SURG_PROFILE_COMMENT](SN_SURG_PROFILE_COMMENT.md) | `PREV_SURG_PROFILE_COMMENT_ID` |

