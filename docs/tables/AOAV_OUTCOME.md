# AOAV_OUTCOME

> This table stores the outcomes generated such as PI score, etc.

**Description:** AOAV_OUTCOME  
**Table type:** ACTIVITY  
**Primary key:** `AOAV_OUTCOME_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_OUTCOME_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `CALCULATED_DT_TM` | DATETIME |  |  | The date time the outcome is calculated |
| 7 | `COMP_SCORE_VALUE` | DOUBLE |  |  | Score value of the outcome |
| 8 | `DAY_NUM` | DOUBLE |  |  | The day of the patient's encounter stay after they entered the first level of care for which the outcome is generated |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Encounter |
| 10 | `EQUATION_CD` | DOUBLE | NOT NULL |  | The AOAV equation code value |
| 11 | `OUTCOME_STS_FLAG` | DOUBLE | NOT NULL |  | The outcome status flag IN-PROGRESS = 0, COMPLETED = 1, SUMMARIZED = 2, MODIFIED = 3 |
| 12 | `OUTCOME_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for the type of outcome generated |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This field is no longer used - DBARCHDTL-23349 |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AOAV_OUTCOME_COMP](AOAV_OUTCOME_COMP.md) | `AOAV_OUTCOME_ID` |

