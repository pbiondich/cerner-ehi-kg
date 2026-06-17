# FN_EV_SURVEY_ACT

> Stores all survey activity data for each encounter used by Emergent Event

**Description:** FN_EV_SURVEY_ACT  
**Table type:** ACTIVITY  
**Primary key:** `FN_EV_SURVEY_ACT_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was created |
| 3 | `ENCNTR_ID` | DOUBLE |  | FK→ | encounter which the survey is associated with |
| 4 | `FN_EV_SURVEY_ACT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `PERFORMED_DT_TM` | DATETIME |  |  | The date and time the survey was performed |
| 6 | `PERFORMED_PRSNL_ID` | DOUBLE |  | FK→ | personnel id of provider who performed this survey |
| 7 | `SURVEY_GRP_ID` | DOUBLE |  |  | Unique identifier for a survey activity, there may be more than one row with same survey_grp_id, but only one of those rows will be current as indicated by the active_ind field.; The group ID value will be same as PK value of first survey in the group.; |
| 8 | `SURVEY_NAME` | VARCHAR(255) |  |  | Survey name that is displayed to the user. |
| 9 | `SURVEY_TYPE_FLAG` | DOUBLE |  |  | Determines survey is Pre-Hospital, Primary, Secondary, Other |
| 10 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FN_EV_SURVEY_ELEMENT_ACT](FN_EV_SURVEY_ELEMENT_ACT.md) | `FN_EV_SURVEY_ACT_ID` |

