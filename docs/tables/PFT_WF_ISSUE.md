# PFT_WF_ISSUE

> Contains workflow issue definitions.

**Description:** ProFit Workflow Issue  
**Table type:** REFERENCE  
**Primary key:** `PFT_WF_ISSUE_ID`  
**Columns:** 30  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(100) | NOT NULL |  | Alias used to find issues. |
| 6 | `ALIAS_KEY` | VARCHAR(100) | NOT NULL |  | Searcheable key value of the alias column. Contains all caps and no special characters. |
| 7 | `APPROVE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the approval action. |
| 8 | `AUTO_RESOLVE_ACTION_ID` | DOUBLE | NOT NULL |  | *** obsolete - no longer being used ***Identifier of the action stored on the long_blob_reference table that symbolizes the action to be taken when an issue is assigned to the resolution state. |
| 9 | `BILLING_HOLD_CD` | DOUBLE | NOT NULL |  | Billing Hold to be applied when an issue is logged. |
| 10 | `COMPLETE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the completion |
| 11 | `DENY_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the denial action. |
| 12 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | Display value depicting what the issue represents. |
| 13 | `DISPLAY_KEY` | VARCHAR(100) | NOT NULL |  | Searchable key value of the display column. This column will contain all caps and no special characters. |
| 14 | `EVENT_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a reference to the JSON definition for the system event associated to this issue. |
| 15 | `INCOMPLETE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the incompletion action |
| 16 | `ISSUE_CD` | DOUBLE | NOT NULL |  | Codified issue from various data sources. |
| 17 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 18 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related issue description. |
| 19 | `MODEL_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the workflow model to which the issue belongs. |
| 20 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization for which the issue is defined. If it is zero, it implies it is a system default issue definition. |
| 21 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a workflow issue. |
| 22 | `PFT_WF_PROCESS_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the related workflow process model. |
| 23 | `PRODUCTIVITY_IND` | DOUBLE | NOT NULL |  | Indicates if Productivity Weight is set |
| 24 | `PRODUCTIVITY_WEIGHT_NBR` | DOUBLE | NOT NULL |  | Productivity Weight for the Work Item |
| 25 | `RESOLVE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the resolution action. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_DEFINITION_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PFT_WF_PROCESS_MODEL_ID` | [PFT_WF_PROCESS_MODEL](PFT_WF_PROCESS_MODEL.md) | `PFT_WF_PROCESS_MODEL_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `PFT_WF_ISSUE_ID` |
| [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `PFT_WF_ISSUE_ID` |
| [PFT_WF_ISSUE_CRITERIA](PFT_WF_ISSUE_CRITERIA.md) | `PFT_WF_ISSUE_ID` |
| [PFT_WF_ISSUE_EVENT](PFT_WF_ISSUE_EVENT.md) | `PFT_WF_ISSUE_ID` |
| [PFT_WF_ISSUE_PRIORITY](PFT_WF_ISSUE_PRIORITY.md) | `PFT_WF_ISSUE_ID` |
| [WORK_ITEM_RELTN](WORK_ITEM_RELTN.md) | `CHILD_PFT_WF_ISSUE_ID` |
| [WORK_ITEM_RELTN](WORK_ITEM_RELTN.md) | `PARENT_PFT_WF_ISSUE_ID` |

