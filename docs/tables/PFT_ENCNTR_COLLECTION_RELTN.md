# PFT_ENCNTR_COLLECTION_RELTN

> Relation table of Collection activity for a pft encounter

**Description:** PFT ENCNTR COLLECTION RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_ORDER_ID` | DOUBLE |  | FK→ | ** OBSOLETE ** NO LONGER USED. Uniquely identifies the related row on the benefit_order table. ** OBSOLETE ** |
| 7 | `COLLECTION_STATE_CD` | DOUBLE | NOT NULL |  | Identifies the collection state (example: ready to send, at agency, returned) |
| 8 | `COLL_PERCENTAGE` | DOUBLE |  |  | The percentage of retrieved money that is owed to the agency. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `CURRENT_BALANCE` | DOUBLE | NOT NULL |  | The current balance of the financial encounter. |
| 11 | `CURR_BAL_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit balance indicator |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `ORIG_BAL_SENT_AMT` | DOUBLE | NOT NULL |  | Contains the amount of the original balance sent to collections. |
| 14 | `ORIG_WRITE_OFF_BAL` | DOUBLE | NOT NULL |  | The original amount written off to bad debt for a financial encounter. |
| 15 | `ORIG_WRITE_OFF_DT_TM` | DATETIME |  |  | The date and time a financial encounter was written off to bad debt. |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to the table for which this entry points (Collectionagency, prsnl) |
| 17 | `PARENT_ENTITY_NAME` | CHAR(32) | NOT NULL |  | Name of parent entity |
| 18 | `PFT_CA_CRITERIA_VALUE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_ca_criteria_value table |
| 19 | `PFT_ENCNTR_COLLECTION_R_ID` | DOUBLE | NOT NULL |  | Unique identifier |
| 20 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to pft encounter table |
| 21 | `RETURN_BALANCE` | DOUBLE | NOT NULL |  | To capture the financial encounter balance returned from a Collection or Precollection Agency |
| 22 | `RETURN_DT_TM` | DATETIME |  |  | Date that the encounter was returned from the collection agency |
| 23 | `SEND_BACK_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason it was sent back from the collection agency (example: bankruptcy, patient deceased, client request return of encntr) |
| 24 | `SEND_DT_TM` | DATETIME |  |  | Date that the encntr was sent to a collection agency |
| 25 | `TOTAL_ADJ_AMT` | DOUBLE | NOT NULL |  | Amount of total adjustment |
| 26 | `TOTAL_ADJ_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for total adjustment |
| 27 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Amount of total payment |
| 28 | `TOTAL_PAY_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for total payment |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_ORDER_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `PFT_CA_CRITERIA_VALUE_ID` | [PFT_CA_CRITERIA_VALUE](PFT_CA_CRITERIA_VALUE.md) | `PFT_CA_CRITERIA_VALUE_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

