# PFT_QUEUE_ITEM_HIST

> The purpose of this table is to store history for the pft_queue_item table.

**Description:** Contains the profit workflow queue items.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

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
| 9 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel the workqueue item has been assigned to. |
| 10 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL | FK→ | Batch Transaction ID value |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity to which the work item is associated.. |
| 13 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | The version number identifying which bill |
| 14 | `BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique id from blob_reference table used to relate workflow exceptions to images that enter a queue. |
| 15 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Used to track the history each Benefit Order/Health Plan Relations throughout Workflow. Foreign Key link to the BO_HP_RELTN table |
| 16 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 17 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Correspondence Activity ID value |
| 18 | `CREATED_DT_TM` | DATETIME |  |  | Used for aging pft_queue_item_hist rows. |
| 19 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies to which encounter this history relates. |
| 20 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 21 | `ITEM_STATUS_CD` | DOUBLE | NOT NULL |  | This field represents the status or work item for the workflow item. |
| 22 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person ID associated to this work flow. |
| 24 | `PFT_BALANCE_ID` | DOUBLE | NOT NULL |  | This column relates a queue item history to a pft_balance record. |
| 25 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | FK to the pft_encntr table. Represenents a financial Encounter |
| 26 | `PFT_ENTITY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the information contained in a workflow queue. |
| 27 | `PFT_ENTITY_STATUS_GROUP_CD` | DOUBLE | NOT NULL |  | The status of the information contained in a workflow queue. |
| 28 | `PFT_ENTITY_SUB_STATUS_TXT` | VARCHAR(200) |  |  | Used to Describe the corresponding substate for the item in Work Flow. |
| 29 | `PFT_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of information contained in a workflow queue. |
| 30 | `PFT_QUEUE_EVENT_CD` | DOUBLE | NOT NULL |  | Specifies what the event associated to the queue. |
| 31 | `PFT_QUEUE_EVENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to store the type of queue event. ENQUEUE = 1, DEQUEUE = 2 |
| 32 | `PFT_QUEUE_ITEM_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the pft_queue_item table. |
| 33 | `PFT_REPORT_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | References PFT_REPORT_INSTANCE |
| 34 | `PREV_ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL |  | Previous assigned personnel person identifier. |
| 35 | `REFERRAL_EXT_IDENT` | DOUBLE | NOT NULL |  | Uniquely identifies the related referral for this item. |
| 36 | `SCH_ENTRY_ID` | DOUBLE |  | FK→ | Uniquely identifies the related scheduling entry for this item. |
| 37 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related scheduling evento for this item. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `BATCH_TRANS_ID` | [BATCH_TRANS](BATCH_TRANS.md) | `BATCH_TRANS_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `BLOB_REF_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PFT_REPORT_INSTANCE_ID` | [PFT_REPORT_INSTANCE](PFT_REPORT_INSTANCE.md) | `PFT_REPORT_INSTANCE_ID` |
| `SCH_ENTRY_ID` | [SCH_ENTRY](SCH_ENTRY.md) | `SCH_ENTRY_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

