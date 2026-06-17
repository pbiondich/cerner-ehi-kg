# TRANSACTION_ELIGIBILITY

> Table stores information to track eligibility transaction history for patients and encounters.

**Description:** Transaction Eligibility  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ELIGIBILITY_ID`  
**Columns:** 32  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CACHE_DT_TM` | DATETIME |  |  | The date and time the transaction was originally returned by the payer and cached within Transaction Services' system. |
| 2 | `CACHE_EXPIRE_DT_TM` | DATETIME |  |  | The date and time the cached transaction expires. After this point in time, the eligibility data from the response message is stale. |
| 3 | `COVERAGE_STATUS_CD` | DOUBLE | NOT NULL |  | The aggregate coverage status for all benefits within this eligibility transaction. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the encounter table. If populated, eligibility was checked during the given encounter. |
| 5 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the encounter plan relationship for which the eligibility transaction request was published. |
| 6 | `EXT_PAYER_IDENT` | VARCHAR(100) |  |  | The primary identifier of the organization providing the insurance plan (carrier) used by external systems to identify the organization and will only be populated when the organization does not exist in the Millennium build. |
| 7 | `HEALTH_PLAN_ID` | DOUBLE |  | FK→ | Uniquely identifies the related Health Plan record on the HEALTH_PLAN table. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the facility organization that shall provide services to the patient. Identifying information for the facility that was sent to the payer. |
| 9 | `ORIGINATING_TRANS_ELIG_ID` | DOUBLE |  | FK→ | The identifier of the transaction_eligibility table that identifies the eligibility transaction that initiated the publishing of this subsequent eligibility transaction. If this column is populated, this transaction was triggered from a secondary inquiry rule. |
| 10 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the organization table defining the payer from which eligibility was requested. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier to the person table for the patient whose eligibility was checked via this transaction. |
| 12 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person plan relationship for which the eligibility transaction request was published. |
| 13 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | A code to define the current state of the automated processing of the transaction data. |
| 14 | `REPLY_DT_TM` | DATETIME |  |  | The date and time the eligibility transaction response was received inbound. |
| 15 | `REQUESTED_BEG_COVERAGE_DT_TXT` | VARCHAR(10) |  |  | The beginning of the plan coverage date range for which eligibility was requested of the payer. If only one date was provided, plan coverage information was requested for that single date. Date format is YYYY-MM-DD. |
| 16 | `REQUESTED_END_COVERAGE_DT_TXT` | VARCHAR(10) |  |  | The end of the plan coverage date range for which eligibility was requested of the payer. Date format is YYYY-MM-DD. |
| 17 | `REVIEWER_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the long_text table row containing the reviewers comments. |
| 18 | `REVIEWER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that last modified the manual reviewer status. |
| 19 | `REVIEWER_STATUS_CD` | DOUBLE | NOT NULL |  | The current transaction's manual processing status as defined by the latest reviewing personnel. |
| 20 | `REVIEWER_UPDT_DT_TM` | DATETIME |  |  | Date and time of the last status update by a reviewing personnel. |
| 21 | `SENT_DT_TM` | DATETIME |  |  | The date and time the eligibility transaction was sent outbound. |
| 22 | `SUBMITTER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier of the personnel that initiated publishing of the transaction to request eligibility. |
| 23 | `TRANSACTION_BATCH_LOG_ID` | DOUBLE | NOT NULL | FK→ | The primary key from the TRANSACTION_BATCH_LOG table. The identifier of the transaction_batch_log row to which this transaction is related. |
| 24 | `TRANSACTION_ELIGIBILITY_ID` | DOUBLE | NOT NULL | PK | This is the primary identifier of the transaction_eligibility table. |
| 25 | `TRANSACTION_SOURCE_IDENT` | VARCHAR(50) | NOT NULL |  | The transaction identifier assigned by Transaction Services. Used to retrieve transaction details. |
| 26 | `TRANSACTION_STATUS_CD` | DOUBLE | NOT NULL |  | The high level status of the transaction. |
| 27 | `TRANSACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of the eligibility transaction. It indicates from where the patient¿s eligibility transaction is requested and retrieved. For example, MED_ELIG is processed through Transaction Services while FC_MED_ELIG is processed through Financial Clearance. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIGINATING_TRANS_ELIG_ID` | [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `TRANSACTION_ELIGIBILITY_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| `REVIEWER_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REVIEWER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUBMITTER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANSACTION_BATCH_LOG_ID` | [TRANSACTION_BATCH_LOG](TRANSACTION_BATCH_LOG.md) | `TRANSACTION_BATCH_LOG_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `ORIGINATING_TRANS_ELIG_ID` |
| [TRANSACTION_ELIG_ALERT](TRANSACTION_ELIG_ALERT.md) | `TRANSACTION_ELIGIBILITY_ID` |
| [TRANSACTION_ELIG_CLOB](TRANSACTION_ELIG_CLOB.md) | `TRANSACTION_ELIGIBILITY_ID` |
| [TRANSACTION_ELIG_ERROR](TRANSACTION_ELIG_ERROR.md) | `TRANSACTION_ELIGIBILITY_ID` |
| [TRANSACTION_ELIG_SERVICE](TRANSACTION_ELIG_SERVICE.md) | `TRANSACTION_ELIGIBILITY_ID` |
| [TRANS_ELIG_AUTO_PLAN](TRANS_ELIG_AUTO_PLAN.md) | `TRANSACTION_ELIGIBILITY_ID` |

