# BATCH_TRANS

> Contains information about a Batch Transaction

**Description:** Batch Transaction  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_TRANS_ID`  
**Columns:** 66  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJ_COMPUTED_TOTAL` | DOUBLE |  |  | Adjustment Computed Total. The total monetary amount of adjustments that have been added to the batch. |
| 6 | `ADJ_RESTATED_TOTAL` | DOUBLE |  |  | Populated in the event the user re-states the adjustment control total after stating it during batch creation. |
| 7 | `ADJ_STATED_TOTAL` | DOUBLE |  |  | The initial adjustment control total as stated by the user. |
| 8 | `BATCHJOB_IND` | DOUBLE |  |  | Obsolete. This column is no longer used. Batch Job Indicator |
| 9 | `BATCH_ALIAS` | VARCHAR(25) |  |  | An optional User-defined batch alias for each transaction entry batch |
| 10 | `BATCH_ALIAS_KEY` | VARCHAR(25) |  |  | Corresponding KEY field in UPPERCASE and with special characters and blanks removed. |
| 11 | `BATCH_ALIAS_KEY_A_NLS` | VARCHAR(100) |  |  | BATCH_ALIAS_KEY_A_NLS column |
| 12 | `BATCH_ALIAS_KEY_NLS` | VARCHAR(52) |  |  | Corresponding Global support field for the associated column KEY column. |
| 13 | `BATCH_CONTROL_NBR` | VARCHAR(20) |  |  | This will assist batch control handling when receiving transactions from an external file |
| 14 | `BATCH_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the watch, i.e., working posted, etc. Code Set 23372. |
| 15 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a batch transaction. |
| 16 | `BATCH_TYPE_FLAG` | DOUBLE |  |  | Indicates which tool created the batch. |
| 17 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 18 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the billing_entity table. |
| 19 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 20 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of person that created the record. |
| 21 | `DENIAL_AMT` | DOUBLE | NOT NULL |  | ** obsolete ** The amount of the denial. |
| 22 | `DENIAL_CD` | DOUBLE | NOT NULL |  | ** obsolete ** The Code representing the denial reason. |
| 23 | `DEPOSIT_DT_TM` | DATETIME |  |  | This indicates on which date the amount got deposited to the bank, for the user to see at the time of batch reconciliation |
| 24 | `DEPOSIT_RECORD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the deposit record related to this batch transaction. |
| 25 | `DR_CR_ADJ_COMPUTED_FLAG` | DOUBLE |  |  | Debit Credit Flag for the Adjustment Computed.0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 26 | `DR_CR_ADJ_RESTATED_FLAG` | DOUBLE |  |  | Debit Credit Flag for the Adjustment Restated 0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 27 | `DR_CR_ADJ_STATED_FLAG` | DOUBLE |  |  | Debit Credit Flag for the Adjustment Stated 0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 28 | `DR_CR_FC_COMPUTED_FLAG` | DOUBLE |  |  | Obsolete. No longer used. Debit Credit Flag for the Finance Charge Computed 0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 29 | `DR_CR_FC_RESTATED_FLAG` | DOUBLE |  |  | Obsolete. No longer used. Debit Credit Flag for Finance Charge Restated |
| 30 | `DR_CR_FC_STATED_FLAG` | DOUBLE |  |  | Obsolete. No longer used. Debit Credit Flag for the Finance Charge Stated |
| 31 | `DR_CR_PAY_COMPUTED_FLAG` | DOUBLE |  |  | Debit Credit Flag for Payment Computed 0 - No Balance; 1- Debit Balance; 2 - Credit Balance |
| 32 | `DR_CR_PAY_RESTATED_FLAG` | DOUBLE |  |  | Debit Credit Flag for the Payment Restated 0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 33 | `DR_CR_PAY_STATED_FLAG` | DOUBLE |  |  | Debit Credit Flag for the Payment Stated 0 - No Balance; 1 - Debit Balance; 2 - Credit Balance |
| 34 | `ELECTRONIC_FILE_NAME` | VARCHAR(500) |  |  | Stores the 835 file name in the system. |
| 35 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 36 | `EXT_BATCH_ID_TXT` | VARCHAR(100) |  |  | External Batch ID Text. User created Batch Identifier. |
| 37 | `EXT_BATCH_ID_TXT_KEY` | VARCHAR(100) |  |  | External Batch ID Text_key. This field is used for indexing and searching by External Batch ID Text. |
| 38 | `EXT_BATCH_ID_TXT_KEY_A_NLS` | VARCHAR(400) |  |  | EXT_BATCH_ID_TXT_KEY_A_NLS column |
| 39 | `EXT_BATCH_ID_TXT_KEY_NLS` | VARCHAR(100) |  |  | EXT_BATCH_ID_TXT Key field converted to NLS format for internationalization requirements. |
| 40 | `FC_COMPUTED_TOTAL` | DOUBLE |  |  | Obsolete. No longer used. Finance Charge Computed Total |
| 41 | `FC_RESTATED_TOTAL` | DOUBLE |  |  | Obsolete. No longer used. Finance Charge Restated Total |
| 42 | `FC_STATED_TOTAL` | DOUBLE |  |  | Obsolete. Column no longer used. Finance Charge Stated Total |
| 43 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 44 | `ONEPAYMENT_IND` | DOUBLE | NOT NULL |  | One Payment Indicator. If the indicator is 1, then the batch has one form of payment for all payments within the batch. |
| 45 | `PAYEE_NPI_ORG_ALIAS` | VARCHAR(100) | NOT NULL |  | National provider identifier alias for the payee organization. |
| 46 | `PAYEE_ORG_ID` | DOUBLE | NOT NULL | FK→ | National provider identifier for the payee organization. |
| 47 | `PAYER_BATCH_IDENT` | VARCHAR(25) | NOT NULL |  | ** obsolete ** External reference number specified by payer for batch of the claim forms |
| 48 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | The mode of payment sent by the payer. |
| 49 | `PAYMENT_NUM_DESC` | VARCHAR(500) | NOT NULL |  | The check number associated with the remittance check. |
| 50 | `PAYOR_ORG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the payor of the remittance batch. |
| 51 | `PAY_COMPUTED_TOTAL` | DOUBLE |  |  | Payment Computed Total. The total monetary amount of payments that have been added to the batch. |
| 52 | `PAY_RESTATED_TOTAL` | DOUBLE |  |  | Payment Restated Total. Populated in the event the user re-states the payment control total after stating it during batch creation. |
| 53 | `PAY_STATED_TOTAL` | DOUBLE |  |  | Payment Stated Total. The initial payment control total as stated by the user. |
| 54 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL |  | Obsolete. No longer used. ProFit Event Occurrence Log |
| 55 | `POSTED_BY_USER_ID` | DOUBLE | NOT NULL | FK→ | The column will help to identify who posted the batch. |
| 56 | `POST_DT_TM` | DATETIME |  |  | Post date for this batch. |
| 57 | `PURGED_IND` | DOUBLE |  |  | Obsolete. No longer used. Purged Indicator |
| 58 | `RAW_BATCH_TRANS_ID` | DOUBLE |  | FK→ | Uniquely identifies the Raw Batch Transaction record related to this row. |
| 59 | `SESSION_ID` | DOUBLE | NOT NULL |  | Session ID - No longer used |
| 60 | `SUBMITTED_DT_TM` | DATETIME |  |  | If submitted, the date and time of submittal |
| 61 | `SUBMITTED_IND` | DOUBLE |  |  | Indicates whether or not submitted |
| 62 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PAYEE_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PAYOR_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `POSTED_BY_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAW_BATCH_TRANS_ID` | [RAW_BATCH_TRANS](RAW_BATCH_TRANS.md) | `RAW_BATCH_TRANS_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_EXT](BATCH_TRANS_EXT.md) | `BATCH_TRANS_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `BATCH_TRANS_ID` |
| [BATCH_TRANS_RELTN](BATCH_TRANS_RELTN.md) | `BATCH_TRANS_ID` |
| [CLAIM_TRANS_INFO](CLAIM_TRANS_INFO.md) | `BATCH_TRANS_ID` |
| [DEP_REC_BATCH_TRANS_RELTN](DEP_REC_BATCH_TRANS_RELTN.md) | `BATCH_TRANS_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `BATCH_TRANS_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `BATCH_TRANS_ID` |

