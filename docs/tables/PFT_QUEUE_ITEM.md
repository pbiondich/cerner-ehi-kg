# PFT_QUEUE_ITEM

> This table stores data representing items within the system that require processing in workflow..

**Description:** ProFit Queue Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 71

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | Used to track Accounts throughout Workflow. Foreign Key link to the ACCOUNT table. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from the Trans_log table. This defines a charge, or payment in a batch job. |
| 7 | `AR_BALANCE` | DOUBLE |  |  | Used for State Based Work Flow queue items when tracking their balances. The current balance of the pft_queue_item. |
| 8 | `AR_BALANCE_DR_CR_FLAG` | DOUBLE |  |  | Debit/Credit Flag for the AR Balance Column |
| 9 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel currently assigned to the PFT_QUEUE_ITEM. |
| 10 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL | FK→ | Batch Transaction ID value |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity that the work item is associated to. |
| 13 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL |  | The version number identifying which bill |
| 14 | `BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique id from blob_reference table used to relate workflow exceptions to images that enter a queue. |
| 15 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Used to track the history each Benefit Order/Health Plan Relations throughout Workflow. Foreign Key link to the BO_HP_RELTN table |
| 16 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 17 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Correspondence Activity ID value |
| 18 | `CREATED_DT_TM` | DATETIME |  |  | Used for aging pft_queue_item_hist rows. |
| 19 | `DEPARTMENT_ID` | DOUBLE |  | FK→ | Stores the department id (prsnl_group_id) that the workitem has been assigned to. |
| 20 | `DEPARTMENT_TYPE_CD` | DOUBLE |  |  | The type of department assigned to this work item.For Just In Time alone value is filled from pft_wf_process_model table. For other department types value is filled from pft_wf_department_reltn table. |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related clinical encounter for this item. |
| 22 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 23 | `EVENT_CD` | DOUBLE | NOT NULL |  | Store event code of the event identifying the work item. |
| 24 | `EVENT_PARAMETER` | VARCHAR(200) |  |  | String that will hold parameters for action batch jobs setup in Workflow. |
| 25 | `IMPACT_CATEGORY_FLAG` | DOUBLE |  |  | The impact category. 1-High, 2-Medium, 3-Low |
| 26 | `ITEM_STATUS_CD` | DOUBLE | NOT NULL |  | Current state of the entity. Pulls item status code from both code sets (4002267 for work items & continuous workflow and 29823 for state & exception queues) |
| 27 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 28 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related description of an issue. |
| 29 | `OWNER_ID` | DOUBLE | NOT NULL |  | The workflow item owner. The table from which this ID comes is indicated by the owner_table_name column. The type of owner (Personnel, Guarantor, etc.) is indicated by the owner_type_cd column. |
| 30 | `OWNER_TABLE_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table from which the owner_id originates. |
| 31 | `OWNER_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the owner type (Personnel, Guarantor, etc.) |
| 32 | `PENDING_EVENT_CD` | DOUBLE | NOT NULL |  | Event codes that are only defined for queue items that are waiting for a batch job to execute. |
| 33 | `PERCENTILE_RANK_NBR` | DOUBLE | NOT NULL |  | The percentile rank of the work item. |
| 34 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person ID associated to this workflow. |
| 35 | `PFT_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | This column stores the relationship between the queue item and it's affected balance. |
| 36 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to a ProFit encounter. |
| 37 | `PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the information contained in a workflow queue. |
| 38 | `PFT_ENTITY_STATUS_GROUP_CD` | DOUBLE | NOT NULL |  | The group to which the PFT_QUEUE_ITEM status is related. |
| 39 | `PFT_ENTITY_SUB_STATUS_TXT` | VARCHAR(200) |  |  | Used to Describe the corresponding substate for the item in Work Flow. |
| 40 | `PFT_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of information contained in a workflow queue. |
| 41 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL | FK→ | The event occur log ID repsonisble for creating this queue Item. |
| 42 | `PFT_QUEUE_ITEM_ID` | DOUBLE | NOT NULL |  | Unique identifier for the pft_queue_item table. |
| 43 | `PFT_REPORT_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | References PFT_REPORT_INSTANCE |
| 44 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | FK→ | The workflow issue id related to this queue item. |
| 45 | `PREV_ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel previously assigned to the PFT_QUEUE_ITEM. |
| 46 | `PRIORITY_ASSESSMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The priority assessment type flag. 0-System, 1-External, 2-Manual |
| 47 | `PRIORITY_FLAG` | DOUBLE | NOT NULL |  | The work item priority. 1-Critical, 2-High, 3-Medium, 4-Low, 5-Minor |
| 48 | `PRIORITY_RETRY_CNT` | DOUBLE | NOT NULL |  | The priority assignment retry count. |
| 49 | `PRIORITY_STATUS_FLAG` | DOUBLE |  |  | The priority status. 1 - In-process, 2 - Complete, 3 - In-error |
| 50 | `PRIORITY_UPDT_DT_TM` | DATETIME |  |  | This column indicates when the priority is last updated on this work item. |
| 51 | `PROCESS_MSG_TXT` | VARCHAR(110) | NOT NULL |  | Additional message data associated with any processing job. |
| 52 | `QUEUE_ITEM_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time the status of the queue item was last updated. |
| 53 | `REASON_CD` | DOUBLE | NOT NULL |  | Applied action code on work item or reason code (CS 4003103) in case system applied action code. |
| 54 | `REFERRAL_EXT_IDENT` | DOUBLE | NOT NULL |  | Uniquely identifies the related referral for this item. |
| 55 | `RESPONSIBLE_ID` | DOUBLE | NOT NULL |  | The resolver for this workflow item. The table from which this ID comes is indicated by the responsible_table_name column. The type of owner (Personnel, Guarantor, etc.) is indicated by the owner_type_cd column. |
| 56 | `RESPONSIBLE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related responsible personnel or department associated to an issue. |
| 57 | `RESPONSIBLE_TABLE_NAME` | VARCHAR(32) | NOT NULL |  | The table from which the resolver(responsible_id) originates. |
| 58 | `RESPONSIBLE_TYPE_CD` | DOUBLE | NOT NULL |  | The resolver type (personnel, guarantor, etc.) |
| 59 | `REVIEWING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the reviewer associated to an issue. |
| 60 | `SCH_ENTRY_ID` | DOUBLE |  | FK→ | Uniquely identifies the related scheduling entry for this item. |
| 61 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related scheduling evento for this item. |
| 62 | `SECONDARY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains the ID of the Secondary Owner of the work item when primary owner is Out of Office. |
| 63 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 67 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `URGENCY_CATEGORY_FLAG` | DOUBLE |  |  | The urgency category. 1-High, 2-Medium, 3-Low |
| 69 | `WI_ASSIGNED_DT_TM` | DATETIME |  |  | The date and time this work item was triggered. |
| 70 | `WORKITEM_ORIGIN_CD` | DOUBLE | NOT NULL |  | Stores the origin for the Orok Item created. |
| 71 | `WORK_ITEM_AMT` | DOUBLE | NOT NULL |  | Contains the work item dollar amount. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `BATCH_TRANS_ID` | [BATCH_TRANS](BATCH_TRANS.md) | `BATCH_TRANS_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BLOB_REF_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `DEPARTMENT_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PFT_EVENT_OCCUR_LOG_ID` | [PFT_EVENT_OCCUR_LOG](PFT_EVENT_OCCUR_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |
| `PFT_REPORT_INSTANCE_ID` | [PFT_REPORT_INSTANCE](PFT_REPORT_INSTANCE.md) | `PFT_REPORT_INSTANCE_ID` |
| `PFT_WF_ISSUE_ID` | [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_ISSUE_ID` |
| `RESPONSIBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEWING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_ENTRY_ID` | [SCH_ENTRY](SCH_ENTRY.md) | `SCH_ENTRY_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SECONDARY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

