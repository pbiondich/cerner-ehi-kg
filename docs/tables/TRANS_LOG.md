# TRANS_LOG

> Is used to identify what type of transaction we are dealing with along with high level information about the transaction before it is broken down to the account or charge level.

**Description:** Transaction Log  
**Table type:** ACTIVITY  
**Primary key:** `ACTIVITY_ID`  
**Columns:** 34  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | PK FK→ | Primary Key and Foreign Key to the Activity Log Table. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILL_IND` | DOUBLE |  |  | Indicates that the bill has been sent out for the transaction. |
| 8 | `BUNDLE_ID` | DOUBLE | NOT NULL |  | Will be removed |
| 9 | `BUNDLE_IND` | DOUBLE |  |  | Bundle Indicator - no longer being used. |
| 10 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 11 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 12 | `CREDIT_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Balance this transaction impacted (credit) |
| 13 | `DEBIT_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Balance this transaction impacted (debit). |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `FIN_TRANS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the FIN_TRANS_GROUP table. |
| 16 | `GL_POSTED_IND` | DOUBLE |  |  | General Ledger Indicator |
| 17 | `PAYMENT_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related payment detail record. |
| 18 | `PFT_PAYMENT_LOCATION_ID` | DOUBLE |  | FK→ | Uniquely identifies the payment location for this record. |
| 19 | `POST_DT_TM` | DATETIME |  |  | The date and time the transaction was posted. |
| 20 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | ** Obsolete - No longer used ** SOURCE FLAG - 1 = Automatically calculated - 0 = Manually calculated ** Obsolete** |
| 21 | `SUPPRESS_FLAG` | DOUBLE |  |  | Suppression flag to indicate levels of suppression - Needs to be a long. |
| 22 | `TOTAL_TRANS_AMOUNT` | DOUBLE |  |  | The total amount of the transaction. (In the case of a payment, the full amount before being applied to multiple accounts). |
| 23 | `TPM_ID` | DOUBLE | NOT NULL |  | Transaction Posting Matrix |
| 24 | `TRANS_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_trans_alias table. |
| 25 | `TRANS_REASON_CD` | DOUBLE | NOT NULL |  | Stores information about why a transaction (adjustment, write off) took place. |
| 26 | `TRANS_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the transaction. (hold, review) |
| 27 | `TRANS_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Contains the reason code for this transaction log entry. |
| 28 | `TRANS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction Sub Type |
| 29 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies whether we are dealing with a charge, payment, adjustment... |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREDIT_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |
| `DEBIT_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |
| `FIN_TRANS_GROUP_ID` | [FIN_TRANS_GROUP](FIN_TRANS_GROUP.md) | `FIN_TRANS_GROUP_ID` |
| `PAYMENT_DETAIL_ID` | [PAYMENT_DETAIL](PAYMENT_DETAIL.md) | `PAYMENT_DETAIL_ID` |
| `PFT_PAYMENT_LOCATION_ID` | [PFT_PAYMENT_LOCATION](PFT_PAYMENT_LOCATION.md) | `PFT_PAYMENT_LOCATION_ID` |
| `TRANS_ALIAS_ID` | [PFT_TRANS_ALIAS](PFT_TRANS_ALIAS.md) | `PFT_TRANS_ALIAS_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `CHRG_ACTIVITY_ID` |
| [BATCH_TRANS_RELTN](BATCH_TRANS_RELTN.md) | `ACTIVITY_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `ACTIVITY_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `ACTIVITY_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `ACTIVITY_ID` |
| [RCR_TRANS_DIST](RCR_TRANS_DIST.md) | `ACTIVITY_ID` |
| [TRANS_TRANS_RELTN](TRANS_TRANS_RELTN.md) | `CHILD_ACTIVITY_ID` |
| [TRANS_TRANS_RELTN](TRANS_TRANS_RELTN.md) | `PARENT_ACTIVITY_ID` |

