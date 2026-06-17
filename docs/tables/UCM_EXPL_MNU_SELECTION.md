# UCM_EXPL_MNU_SELECTION

> This table holds the names given to the set of selections the user wants to save.

**Description:** Unified Case Manager - Explorer Menu Selection  
**Table type:** ACTIVITY  
**Primary key:** `UCM_EXPL_MNU_SELECTION_ID`  
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
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `SELECTION_NAME` | VARCHAR(100) | NOT NULL |  | The name given by the user for the selection tobe saved. |
| 7 | `UCMR_EXPL_MNU_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related report. |
| 8 | `UCM_EXPL_MNU_SELECTION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a selection the user wants to save. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `UCMR_EXPL_MNU_REPORT_ID` | [UCMR_EXPL_MNU_REPORT](UCMR_EXPL_MNU_REPORT.md) | `UCMR_EXPL_MNU_REPORT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_EXPL_MNU_PROMPT_VALUE](UCM_EXPL_MNU_PROMPT_VALUE.md) | `UCM_EXPL_MNU_SELECTION_ID` |

