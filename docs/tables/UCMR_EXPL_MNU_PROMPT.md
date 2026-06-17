# UCMR_EXPL_MNU_PROMPT

> This table contains all the prompt names used in Helix related reports in the Explorer menu.

**Description:** Unified Case Manager Reference - Explorer Menu Prompt  
**Table type:** REFERENCE  
**Primary key:** `UCMR_EXPL_MNU_PROMPT_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PARAM_TYPE_TEXT` | VARCHAR(10) | NOT NULL |  | The data type of the parameter. For example: String, Integer |
| 6 | `PARAM_WRAP_TEXT` | VARCHAR(10) | NOT NULL |  | Indicates if the parameters to this prompt will be wrapped by some format. For example "VALUE( )" |
| 7 | `PROMPT_NAME` | VARCHAR(50) | NOT NULL |  | This will save the report names available in the explorer menu. |
| 8 | `UCMR_EXPL_MNU_PROMPT_ID` | DOUBLE | NOT NULL | PK | Uniquely Identifies a prompt used in Helix related reports in the Explorer Menu. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_EXPL_MNU_PROMPT_VALUE](UCM_EXPL_MNU_PROMPT_VALUE.md) | `UCMR_EXPL_MNU_PROMPT_ID` |

