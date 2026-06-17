# PFT_WF_PROCESS_MODEL

> Reference table to hold ProFit workflow process models.

**Description:** ProFit Workflow Process Model  
**Table type:** REFERENCE  
**Primary key:** `PFT_WF_PROCESS_MODEL_ID`  
**Columns:** 34  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPROVE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the approval action. |
| 3 | `ASSESSMENT_STATE_CD` | DOUBLE | NOT NULL |  | Code that defines the workflow state for the assessment. |
| 4 | `ASSESSOR_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related assessor. |
| 5 | `ASSESSOR_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies from which table the assessment comes, personnel or department, etc. |
| 6 | `ASSESSOR_TYPE_CD` | DOUBLE | NOT NULL |  | Type of assessment owner either personnel or department, etc. |
| 7 | `BILLING_HOLD_CD` | DOUBLE | NOT NULL |  | Code defining the billing hold. |
| 8 | `CATEGORY_CD` | DOUBLE | NOT NULL |  | Used to classify workflow model created by the user using category. |
| 9 | `COMPLETE_ACTION_CD` | DOUBLE | NOT NULL |  | Code defining the completion action |
| 10 | `DENY_ACTION_CD` | DOUBLE | NOT NULL |  | Code defining the denial action. |
| 11 | `DESCRIPTION_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row in the long_text_reference table that will store the model description. |
| 12 | `DYNAMIC_DELAY_CD` | DOUBLE | NOT NULL |  | The column stores the code of the dynamic delay defined in the codeset. the code value will map CCL script to calculate the dynamic delay. |
| 13 | `ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the entity type to which the model belongs. |
| 14 | `INCOMPLETE_ACTION_CD` | DOUBLE | NOT NULL |  | Action code defining the incompletion action. |
| 15 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 16 | `PFT_WF_PROCESS_MODEL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a given workflow process model. |
| 17 | `PROCESS_MODEL_NAME` | VARCHAR(255) | NOT NULL |  | Name of the workflow process model. |
| 18 | `REQ_MAN_ASSIGN_IND` | DOUBLE | NOT NULL |  | Determines if this process model requires manual assignment of a resolution owner. |
| 19 | `RESOLUTION_STATE_CD` | DOUBLE | NOT NULL |  | Defines the workflow state for the resolution. |
| 20 | `RESOLVER_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the owner ID of the resolution state. |
| 21 | `RESOLVER_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the Name of the table for the resolver, based on the type of resolution. For example: personnel, department, etc. |
| 22 | `RESOLVER_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the type of resolution owner, either personnel, department, etc. |
| 23 | `RESOLVE_ACTION_CD` | DOUBLE | NOT NULL |  | Action Cdoe defining the resolution action. |
| 24 | `REVIEWER_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the owner id of the review state. |
| 25 | `REVIEWER_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the Name of the table for the reviewer, based on the type of review. For example: personnel, department, etc. |
| 26 | `REVIEWER_TYPE_CD` | DOUBLE | NOT NULL |  | Type of reviewer owner either personnel or department, etc. |
| 27 | `REVIEW_STATE_CD` | DOUBLE | NOT NULL |  | Contains the workflow state for the review. |
| 28 | `SUBCATEGORY_CD` | DOUBLE | NOT NULL |  | Used to further classify workflow model inside a category. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `WI_ASSIGNMENT_TYPE_CD` | DOUBLE |  |  | This column stores the workitem assignment type information. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DESCRIPTION_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_PROCESS_MODEL_ID` |
| [PFT_WF_NOTIFICATION](PFT_WF_NOTIFICATION.md) | `PFT_WF_PROCESS_MODEL_ID` |
| [PFT_WF_STATE_ACTION_RELTN](PFT_WF_STATE_ACTION_RELTN.md) | `PFT_WF_PROCESS_MODEL_ID` |

