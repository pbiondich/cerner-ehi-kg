# CLAIM_TRANS_INFO

> The claim_trans_info table holds claim transaction information for a given batch.

**Description:** Claims Transaction Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_TRANS_ID` | DOUBLE |  | FK→ | Uniquely identifies the related remittance batch_id on the BATCH_TRANS table. |
| 2 | `BILL_VRSN_NBR` | DOUBLE |  | FK→ | Contains the related bill_vrsn_nbr from the BILL_REC table. |
| 3 | `CAPITAL_EXCEPTION_AMT` | DOUBLE |  |  | MIA24 is the capital exception amount. |
| 4 | `CAPITAL_OUTLIER_AMT` | DOUBLE |  |  | MIA17 is the Prospective Payment System (PPS) Capital Outlier amount |
| 5 | `CLAIM_PAY_REMARK_CD_MIA05_TXT` | VARCHAR(250) |  |  | MIA05 is the Claim Payment Remark Code |
| 6 | `CLAIM_PAY_REMARK_CD_MIA20_TXT` | VARCHAR(250) |  |  | MIA20 is the Claim Payment Remark Code |
| 7 | `CLAIM_PAY_REMARK_CD_MIA21_TXT` | VARCHAR(250) |  |  | MIA21 is the Claim Payment Remark Code |
| 8 | `CLAIM_PAY_REMARK_CD_MIA22_TXT` | VARCHAR(250) |  |  | MIA22 is the Claim Payment Remark Code |
| 9 | `CLAIM_PAY_REMARK_CD_MIA23_TXT` | VARCHAR(250) |  |  | MIA23 is the Claim Payment Remark Code |
| 10 | `CLAIM_PAY_REMARK_CD_MOA03_TXT` | VARCHAR(250) |  |  | MOA03 is the Claim Payment Remark Code |
| 11 | `CLAIM_PAY_REMARK_CD_MOA04_TXT` | VARCHAR(250) |  |  | MOA04 is the Claim Payment Remark Code |
| 12 | `CLAIM_PAY_REMARK_CD_MOA05_TXT` | VARCHAR(250) |  |  | MOA05 is the Claim Payment Remark Code |
| 13 | `CLAIM_PAY_REMARK_CD_MOA06_TXT` | VARCHAR(250) |  |  | MOA06 is the Claim Payment Remark Code |
| 14 | `CLAIM_PAY_REMARK_CD_MOA07_TXT` | VARCHAR(250) |  |  | MOA07 is the Claim Payment Remark Code |
| 15 | `CLAIM_TRANS_INFO_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies a row on the CLAIM_TRANS_INFO table. |
| 16 | `CORSP_ACTIVITY_ID` | DOUBLE |  | FK→ | In conjunction with the bill_vrsn_nbr, uniquely identifies the related claim row on the BILL_REC table. |
| 17 | `COST_REPORT_DAYS_CNT` | DOUBLE |  |  | MIA15 is the cost report days |
| 18 | `COVERED_DAYS_CNT` | DOUBLE |  |  | MIA01 is the covered days |
| 19 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 20 | `DISPROPORTION_AMT` | DOUBLE |  |  | MIA06 is the disproportionate share amount |
| 21 | `DRG_AMT` | DOUBLE |  |  | MIA04 is the Diagnosis Related Group (DRG) amount |
| 22 | `DSH_CAPITAL_AMT` | DOUBLE |  |  | MIA11 is the Prospective Payment System (PPS) capital, disproportionate share, hospital Diagnosis Related Group (DRG) amount |
| 23 | `ESRD_PAY_AMT` | DOUBLE |  |  | MOA08 is the End Stage Renal Disease (ESRD) payment amount |
| 24 | `FEDERAL_DRG_AMT` | DOUBLE |  |  | MIA16 is the federal specific Diagnosis Related Group (DRG) amount |
| 25 | `FSP_CAPITAL_AMT` | DOUBLE |  |  | MIA09 is the Prospective Payment System (PPS) capital, federal specific portion, Diagnosis Related Group (DRG) amount |
| 26 | `HOSPITAL_DRG_AMT` | DOUBLE |  |  | MIA14 is hospital specific Diagnosis Related Group (DRG) Amount |
| 27 | `HSP_CAPITAL_AMT` | DOUBLE |  |  | MIA10 is the Prospective Payment System (PPS) capital, hospital specific portion, Diagnosis Related Group (DRG), amount |
| 28 | `IME_CAPITAL_AMT` | DOUBLE |  |  | MIA13 is the Prospective Payment System (PPS) capital indirect medical education claim amount |
| 29 | `MIA_NON_PAYABLE_AMT` | DOUBLE |  |  | MIA19 is the professional component amount billed but not payable |
| 30 | `MOA_NON_PAYABLE_AMT` | DOUBLE |  |  | MOA09 is the professional component amount billed but not payable |
| 31 | `OLD_CAPITAL_AMT` | DOUBLE |  |  | MIA12 is the old capital amount |
| 32 | `OPERATING_OUTLIER_AMT` | DOUBLE |  |  | MIA02 is the Prospective Payment System (PPS) Operating Outlier amount |
| 33 | `PASS_THROUGH_AMT` | DOUBLE |  |  | MIA07 is the Medicare Secondary Payer (MSP) pass-through amount |
| 34 | `PAYABLE_AMT` | DOUBLE |  |  | MOA02 is the claim HCPCS payable amount |
| 35 | `PPS_CAPITAL_AMT` | DOUBLE |  |  | MIA08 is the total Prospective Payment System (PPS) capital amount |
| 36 | `PSYCH_DAYS_CNT` | DOUBLE |  |  | MIA03 is the lifetime psychiatric days |
| 37 | `REIMBURSEMENT_RATE_PCT` | DOUBLE |  |  | MOA01 is the reimbursement rate. Percentage expressed as a decimal 0.0 thru 1.0 |
| 38 | `TEACHING_AMT` | DOUBLE |  |  | MIA18 is the indirect teaching amount |
| 39 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_TRANS_ID` | [BATCH_TRANS](BATCH_TRANS.md) | `BATCH_TRANS_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |

