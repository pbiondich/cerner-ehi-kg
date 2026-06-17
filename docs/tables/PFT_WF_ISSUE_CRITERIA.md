# PFT_WF_ISSUE_CRITERIA

> Stores reference build data for ProFit workflow issues.

**Description:** ProFit Workflow Issue Criteria  
**Table type:** REFERENCE  
**Primary key:** `PFT_WF_ISSUE_CRITERIA_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CRITERIA_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of criteria. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the parent table. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies which entity is the related parent. |
| 5 | `PFT_WF_ISSUE_CRITERIA_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies build data for pft workflow issues. |
| 6 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related workflow issue. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_WF_ISSUE_ID` | [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_ISSUE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_WF_HIST_REMINDER_RELTN](PFT_WF_HIST_REMINDER_RELTN.md) | `PFT_WF_ISSUE_CRITERIA_ID` |

