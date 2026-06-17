# HIM_TASK_DETAIL

> Options associated with HIM tasks are stored in this table.

**Description:** HIM Task Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `HIM_TASK_DETAIL_ID` | DOUBLE | NOT NULL |  | This is the unique primary identifier of the him_task_detail table. SEQUENCE NAME: PROFILE_SEQ |
| 5 | `PRIMARY_COLOR_VALUE` | DOUBLE | NOT NULL |  | The primary background color that will be shown based on the PRIMARY_TASK_AGE_DAYS value. |
| 6 | `PRIMARY_TASK_AGE_DAYS` | DOUBLE | NOT NULL |  | The low limit number of days that the primary coloring should be used. |
| 7 | `SECONDARY_COLOR_VALUE` | DOUBLE | NOT NULL |  | The secondary background color that will be shown based on the SECONDARY_TASK_AGE_DAYS value. |
| 8 | `SECONDARY_TASK_AGE_DAYS` | DOUBLE | NOT NULL |  | The low limit number of days that the secondary coloring should be used. |
| 9 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the HIM Task Type. CODE SET: 6026 |
| 10 | `TERTIARY_COLOR_VALUE` | DOUBLE | NOT NULL |  | The tertiary background color that will be shown based on the TERTIARY_TASK_AGE_DAYS value. |
| 11 | `TERTIARY_TASK_AGE_DAYS` | DOUBLE | NOT NULL |  | The low limit number of days that the tertiary coloring should be used. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `USE_TASK_AGE_COLOR_IND` | DOUBLE | NOT NULL |  | Indicates whether or not Task Age Coloring is being used for the task type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

