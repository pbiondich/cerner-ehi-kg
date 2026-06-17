# UCMR_CASE_GROUP

> Contains case group type data.

**Description:** Unified Case Manger Reference - Case Group  
**Table type:** REFERENCE  
**Primary key:** `UCMR_CASE_GROUP_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CASE_GROUP_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Contains the description of the case group type. |
| 5 | `CASE_GROUP_NAME_CD` | DOUBLE | NOT NULL |  | Contains the code value of the Case Group Name |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LOOKBACK_MINUTES_MAX_NBR` | DOUBLE | NOT NULL |  | Contains the maximum number of minutes to look back for cases to qualify. |
| 8 | `LOOKBACK_MINUTES_MIN_NBR` | DOUBLE | NOT NULL |  | Contains the minimum number of minutes to look back for cases to qualify. |
| 9 | `MAX_DATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The preferred date type display of maximum lookback minutes. For example: days, weeks, months, and years.1 - Days2 - Weeks3 - Months4 - Years |
| 10 | `MIN_DATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The preferred date type display of minimum lookback minutes. For example: days, weeks, months, and years.1 - Days2 - Weeks3 - Months4 - Years |
| 11 | `PREV_UCMR_CASE_GROUP_ID` | DOUBLE | NOT NULL |  | Used to track versions of the case group information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 12 | `PROMPT_REPEAT_ORDERS_IND` | DOUBLE | NOT NULL |  | Prompt to add repeat orders to the worklist when True. Otherwise automatically add repeat orders. |
| 13 | `UCMR_CASE_GROUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a case group. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [UCMR_CASE_GRP_STEP_R](UCMR_CASE_GRP_STEP_R.md) | `UCMR_CASE_GROUP_ID` |
| [UCMR_CASE_TYP_GRP_R](UCMR_CASE_TYP_GRP_R.md) | `UCMR_CASE_GROUP_ID` |
| [UCM_CASE_GROUP_PREQUAL](UCM_CASE_GROUP_PREQUAL.md) | `UCMR_CASE_GROUP_ID` |

