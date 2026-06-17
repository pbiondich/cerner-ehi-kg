# RCR_TRANS_DIST

> Rows represent current a log of automatic distributions of posted payment amounts across one or more posted charges. Purpose of table is to render scattered financial information into a form that can be used for business accounting reports.

**Description:** Revenue Cycle Reporting - Transaction Distribution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date and Time the transaction was posted. |
| 3 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related transaction |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity |
| 6 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | The total chare amount for the specific charge or group of charges. |
| 7 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related charge item |
| 8 | `DETAIL_SUMMARY_FLG` | DOUBLE | NOT NULL |  | Indicates whether this row represents the distribution of a portion of the transaction to a specific charge, or to a group of charges. |
| 9 | `DISTRIBUTED_AMT` | DOUBLE | NOT NULL |  | The amount of the transaction that was distributed to the charge. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the facility where the patient was located when the charge was incurred. |
| 12 | `FIN_NUMBER_ALIAS` | VARCHAR(200) |  |  | Secondary identifier for the financial encounter. |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the nomenclature associated with the proceure alias. |
| 14 | `ORDERING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the physician responsible for ordering material or service. |
| 15 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related financial encounter. |
| 16 | `POSTED_BY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel responsible for posting the charge. |
| 17 | `PROCEDURE_ALIAS` | VARCHAR(200) |  |  | Identifies the procedure associated with the charge. |
| 18 | `RCR_TRANS_DIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row that represents a current log of automatic distributions of posted payment amounts across one or more posted charges. |
| 19 | `RENDERING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the physician responsible for rendering service. |
| 20 | `SERVICE_DT_TM` | DATETIME |  |  | Date and Time the service was rendered. |
| 21 | `TRANS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | An optional identifier that further defines the type of transaction. |
| 22 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of transaction (payment or adjustment) |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDERING_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `POSTED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RENDERING_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

