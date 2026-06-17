# UCM_EXPL_MNU_PROMPT_VALUE

> This table holds the values of each prompt item selected by the user to be saved.

**Description:** Unified Case Manager Explorer Menu Prompt Value  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PROMPT_VALUE_TEXT` | VARCHAR(500) | NOT NULL |  | The value of the individualselected items of prompt. |
| 6 | `UCMR_EXPL_MNU_PROMPT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related prompt. |
| 7 | `UCM_EXPL_MNU_PROMPT_VALUE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the values of a prompt item selected by the user to be saved. |
| 8 | `UCM_EXPL_MNU_SELECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related menu selection. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_EXPL_MNU_PROMPT_ID` | [UCMR_EXPL_MNU_PROMPT](UCMR_EXPL_MNU_PROMPT.md) | `UCMR_EXPL_MNU_PROMPT_ID` |
| `UCM_EXPL_MNU_SELECTION_ID` | [UCM_EXPL_MNU_SELECTION](UCM_EXPL_MNU_SELECTION.md) | `UCM_EXPL_MNU_SELECTION_ID` |

