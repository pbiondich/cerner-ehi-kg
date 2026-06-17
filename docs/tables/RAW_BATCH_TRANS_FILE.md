# RAW_BATCH_TRANS_FILE

> Contins pre-translated X12 835 Transaction Level data..

**Description:** Raw Batch Transaction File  
**Table type:** ACTIVITY  
**Primary key:** `RAW_BATCH_TRANS_FILE_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_NUMBER_IDENT` | VARCHAR(38) | NOT NULL |  | CLP01- Bill Number sent in for CLP, CAS, SVC and SVC-CAS transactions. |
| 2 | `CLAIM_STATUS_CD_TXT` | VARCHAR(4) | NOT NULL |  | CLP02 - Code identifying the status of an entire claim as assigned by the payor, claim review organization, or repricing organization. i.e. - Processed as Primary, Secondary, Tertiary, etc. |
| 3 | `PAYER_BILL_CODE` | VARCHAR(20) | NOT NULL |  | Code used by payer to adjudicate the bill. |
| 4 | `PAYER_BILL_TYPE_CODE` | VARCHAR(10) | NOT NULL |  | Code type used by payer to adjudicate the bill. |
| 5 | `PAYER_COVERED_CHARGE_AMT` | DOUBLE |  |  | The charge amount covered by payer. |
| 6 | `PAYER_COVERED_DAYS` | DOUBLE |  |  | The number of days covered by payer. |
| 7 | `PROCEDURE_CD_TXT` | VARCHAR(48) | NOT NULL |  | SVC01-2. Identifying number for a product or service. |
| 8 | `PROCEDURE_MODIFIER_CD_TXT` | VARCHAR(15) | NOT NULL |  | Will hold any modifiers that were sent. Identifies special circumstances related to the performance of the service. Combination of SVC01-3 to SVC01-6. Will be separated with "\|". |
| 9 | `PROD_SRVC_QUAL_CD_TXT` | VARCHAR(2) | NOT NULL |  | SVC01-1. Code identifying the type/source of the descriptive number used in Product/Service ID. i.e. - HC for HCPCS codes or NU for UB92 codes. |
| 10 | `RAW_BATCH_TRANS_FILE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a pre-translated X12 835 transaction level data row. |
| 11 | `RAW_BATCH_TRANS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the raw batch trans record related to this row. |
| 12 | `REF_IDENT_CD_TXT` | VARCHAR(50) | NOT NULL |  | REF02. Reference information as defined for a particular Transaction Set or as specified by the Reference Identification Qualifier. |
| 13 | `REF_IDENT_QUAL_CD_TXT` | VARCHAR(3) | NOT NULL |  | REF01. Code that qualifies the reference identification. I.e. - Provider control number or Authorization Number. |
| 14 | `SRVC_DT_TM` | DATETIME |  |  | DTM02. Date and time service was performed. |
| 15 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | CLP03, SVC02. Total Charge Amount. |
| 16 | `TRANS_AMT` | DOUBLE | NOT NULL |  | CLP04, CAS03, SVC03, SVC-CAS03. Amount of transaction. |
| 17 | `TRANS_GROUP_CD_TXT` | VARCHAR(2) | NOT NULL |  | CAS01 - Identifies category of claim adjustment. Translates to codeset 26379.CO - Contractual ObligationCR - Correction and ReversalsOA - Other AdjustmentsPI - Payor initiated reductionsPR - Patient Responsibility |
| 18 | `TRANS_REASON_CD_TXT` | VARCHAR(5) | NOT NULL |  | CAS02, SVC-CAS02. Identifies reason the adjustment was made. Translates to codeset 26398. |
| 19 | `TRANS_SEGMENT_IDENT` | VARCHAR(10) | NOT NULL |  | CLP, CAS, SVC, SVC-CAS, SVC-REF. Identifies the segment from which the transaction came. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RAW_BATCH_TRANS_ID` | [RAW_BATCH_TRANS](RAW_BATCH_TRANS.md) | `RAW_BATCH_TRANS_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `RAW_BATCH_TRANS_FILE_ID` |

