# SHX_COMMENT

> Each row on the table represents relationship between the Patient's social history assessment record and the comment. This is to track comment History on a patient's history assessment.

**Description:** SHX_COMMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMMENT_DT_TM` | DATETIME | NOT NULL |  | COMMENT DATE AND TIME |
| 4 | `COMMENT_DT_TM_TZ` | DOUBLE | NOT NULL |  | COMMENT DATE TIME TIME ZONE |
| 5 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Comment personnel id. This is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | LONG TEXT ID FROM LONG_TEXT table |
| 8 | `SHX_ACTIVITY_GROUP_ID` | DOUBLE | NOT NULL |  | Activity group. This is the shx_activity_group_id value from the shx_activity table |
| 9 | `SHX_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: PROBLEM_SEQ unique identifier for the SHX_ ACTIVITY table. |
| 10 | `SHX_COMMENT_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME: PROBLEM_SEQ This is the table's primary key. the unique identifier for a shx_long_text_r table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SHX_ACTIVITY_ID` | [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_ACTIVITY_ID` |

