# PFT_TRANS_RELTN

> Contains all ProFit transactions, including charges, payments and adjustments.

**Description:** ProFit Transaction Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | FK to the activity_log table |
| 6 | `AMOUNT` | DOUBLE | NOT NULL |  | Amount value |
| 7 | `BATCH_TRANS_FILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the batch_trans_file table. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | FK to the bo_hp_reltn table. Identifies to which balance this transaction is associated. |
| 10 | `BILL_VRSN_NBR` | DOUBLE |  |  | The version number identifying which bill |
| 11 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Date and time this record was created. |
| 12 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | FK to the person table |
| 13 | `DR_CR_FLAG` | DOUBLE | NOT NULL |  | Flag identifying whether the balance is debit or credit. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `FINANCE_CHRG_ID` | DOUBLE | NOT NULL | FK→ | FK to the finance_chrg_cat |
| 16 | `GL_TRANS_LOG_ID` | DOUBLE | NOT NULL | FK→ | FK to the gl_trans_log table |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | FK to account, pft_encntr or bill_rec tables. |
| 18 | `PARENT_ENTITY_NAME` | CHAR(32) | NOT NULL |  | Name of the parent entity |
| 19 | `PFT_TRANS_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies all ProFit transactions, including charges, payments and adjustments. |
| 20 | `POST_CLAIM_DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that the transaction was posted to claim because the charge could not be identified |
| 21 | `REASSOC_DT_TM` | DATETIME |  |  | Date that the transaction was reassociated from one entity to another. |
| 22 | `REVENUE_SUMMARY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the corresponding revenue summary, which this transaction participated. |
| 23 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction type code value |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `BATCH_TRANS_FILE_ID` | [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `BATCH_TRANS_FILE_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FINANCE_CHRG_ID` | [FINANCE_CHRG_CAT](FINANCE_CHRG_CAT.md) | `FINANCE_CHRG_ID` |
| `GL_TRANS_LOG_ID` | [GL_TRANS_LOG](GL_TRANS_LOG.md) | `GL_TRANS_LOG_ID` |
| `REVENUE_SUMMARY_ID` | [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `PFT_REVENUE_SUMMARY_ID` |

