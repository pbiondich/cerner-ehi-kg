# PFT_QUEUE_ITEM_WF_HIST

> This table keeps history of workflow item cycle process.

**Description:** ProFit Queue Item Workflow History  
**Table type:** ACTIVITY  
**Primary key:** `PFT_QUEUE_ITEM_WF_HIST_ID`  
**Columns:** 49  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNTABLE_ENTITY_CD` | DOUBLE | NOT NULL |  | The code value from code set 4002623 representing the supported accountable entities. For example, personnek, department, guarantor, etc. |
| 2 | `ACCOUNTABLE_ENTITY_ID` | DOUBLE | NOT NULL |  | Indicates the accountable party for this work item. |
| 3 | `ACCOUNTABLE_PERSON_ID` | DOUBLE | NOT NULL |  | Indicates the accountable person for this work item. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `BALANCE` | DOUBLE |  |  | The balance amount of the entity at the time of perfroming the action. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity to which the work item is associated. |
| 8 | `BILLING_HOLD_CD` | DOUBLE | NOT NULL |  | The billing hold which is applied on the entity when work the work item is identified. |
| 9 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Creation time of the entry in the pft_queue_item table. |
| 10 | `CURRENT_RESPONSIBILITY_FLAG` | DOUBLE | NOT NULL |  | Indicates where responsibility currently lies. Options: 1- Assessment, 2 - Resolution, 3 - Review |
| 11 | `DEPARTMENT_ID` | DOUBLE |  | FK→ | Stores the department id (prsnl_group_id) that the workitem has been assigned to. |
| 12 | `DEPARTMENT_TYPE_CD` | DOUBLE |  |  | The type of department assigned to this work item.For Just In Time alone value is filled from pft_wf_process_model table. For other department types value is filled from pft_wf_department_reltn table. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_CD` | DOUBLE | NOT NULL |  | Store event code of the event identifying the work item. |
| 15 | `IDENTIFER_PERSON_ID` | DOUBLE | NOT NULL |  | Indicates the person who identified the work item |
| 16 | `IDENTIFIER_ENTITY_CD` | DOUBLE | NOT NULL |  | Code value from code set 4002623 representing the supported identifier entities. For example, personnel, department, guarantor, etc. |
| 17 | `IDENTIFIER_ENTITY_ID` | DOUBLE | NOT NULL |  | Indicates the identifier party of this work. |
| 18 | `IMPACT_CATEGORY_FLAG` | DOUBLE |  |  | The impact category. 1-High, 2-Medium, 3-Low |
| 19 | `ITEM_STATUS_CD` | DOUBLE | NOT NULL |  | Code value from code set 4002267 representing the state of the work item |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 21 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This contains a reference to the long_text table. The corresponding long_text column contains the work item's critical attribute values like billing hold. |
| 22 | `OWNER_ID` | DOUBLE | NOT NULL |  | the workflow item owner. the table from which this id comes is indicated by the owner_table_name column. the type of owner (personnel, guarantor, etc.) is indicated by the owner_type_cd column. |
| 23 | `OWNER_TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Identifies which table the owner_id is related. (PERSON or HEALTH_PLAN.) |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies a record related to the parent_entity_name. |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table name associated with the entity id. For example, PFT_ENCNTR, BO_HP_RELTN |
| 26 | `PERCENTILE_RANK_NBR` | DOUBLE | NOT NULL |  | The percentile rank of the work item. |
| 27 | `PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the current state for the work item. |
| 28 | `PFT_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of informaiton contained in a workflow queue. |
| 29 | `PFT_QUEUE_ITEM_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related queue item. |
| 30 | `PFT_QUEUE_ITEM_WF_HIST_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row of history from the PFT_QUEUE_ITEM table. |
| 31 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related workflow issue. |
| 32 | `PRIORITY_ASSESSMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The priority assessment type flag. 0-System, 1-External, 2-Manual |
| 33 | `PRIORITY_FLAG` | DOUBLE | NOT NULL |  | The work item priority. 1-Critical, 2-High, 3-Medium, 4-Low, 5-Minor |
| 34 | `PRIORITY_RETRY_CNT` | DOUBLE | NOT NULL |  | The priority assignment retry count. |
| 35 | `PRIORITY_STATUS_FLAG` | DOUBLE |  |  | The priority status. 1 - In-process, 2 - Complete, 3 - In-error |
| 36 | `QUEUE_ITEM_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time the status of the queue item was last updated. |
| 37 | `REASON_CD` | DOUBLE | NOT NULL |  | Applied action code on work item or reason code (CS 4003103) in case system applied action code. |
| 38 | `RESPONSIBLE_ENTITY_CD` | DOUBLE | NOT NULL |  | Code value from code set 4002623 representing the supported responsible entities. For example, personnel, department, guarantor, etc. |
| 39 | `RESPONSIBLE_ENTITY_ID` | DOUBLE | NOT NULL |  | Indicates the responsible party for this work. |
| 40 | `RESPONSIBLE_PERSON_ID` | DOUBLE | NOT NULL |  | Indicates the responsible person for this work item |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `URGENCY_CATEGORY_FLAG` | DOUBLE |  |  | The urgency category. 1-High, 2-Medium, 3-Low |
| 47 | `WORKITEM_ORIGIN_CD` | DOUBLE | NOT NULL |  | Stores the origin for the Orok Item created. |
| 48 | `WORK_ITEM_ACTION_FLAG` | DOUBLE | NOT NULL |  | Flag indication for supported performed actions on this queue item.1 - identified.2 - Approved3 - Denied4 - Resolved5 - Completed6 - Incompleted7 - Cancelled8 - Reassigned9 - No Action |
| 49 | `WORK_ITEM_AMT` | DOUBLE | NOT NULL |  | Contains the work item dollar amount. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `DEPARTMENT_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PFT_WF_ISSUE_ID` | [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_ISSUE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PFT_QUEUE_ITEM_WF_RELTN](PFT_QUEUE_ITEM_WF_RELTN.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |
| [PFT_WF_HIST_REMINDER_RELTN](PFT_WF_HIST_REMINDER_RELTN.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |

