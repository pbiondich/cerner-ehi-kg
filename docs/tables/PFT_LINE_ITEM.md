# PFT_LINE_ITEM

> Stores Line Item data from a claim.

**Description:** ProFit Line Item  
**Table type:** ACTIVITY  
**Primary key:** `PFT_LINE_ITEM_ID`  
**Columns:** 25  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies type of bill |
| 2 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | Identifies the Version Number of the Claim |
| 3 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Internal number to identify claim |
| 4 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the revenue code for this line on the claim |
| 5 | `FROM_SERVICE_DT_TM` | DATETIME |  |  | From Service Date of the charges on this line of the claim |
| 6 | `LINE_ITEM_IDENT` | VARCHAR(20) |  |  | Contains the reference id for the line item on the claim. This column is in the format of nnnnn-rrr where the nnnnn represents the claim number and the sss is a randomly generated number. |
| 7 | `LINE_NBR` | DOUBLE |  |  | Line number of the given line on a claim |
| 8 | `MODIFIER_FLAG` | DOUBLE |  |  | Identifies if the modifier_value is a nomenclature_id or a code value |
| 9 | `MODIFIER_VALUE` | DOUBLE |  |  | Charge Modifier for this line or charge on the claim |
| 10 | `NONCOVERED_CHARGES` | DOUBLE |  |  | Total Non-Covered Charge Amount for this line on the claim |
| 11 | `PAGE_NBR` | DOUBLE |  |  | Page number of the give line on a claim |
| 12 | `PFT_LINE_ITEM_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a line item data from a claim. |
| 13 | `PROCEDURE_CODE` | DOUBLE |  |  | Procedure Code for this line on the claim |
| 14 | `REVENUE_CD` | DOUBLE | NOT NULL |  | Revenue code identified for this line on the claim |
| 15 | `TOTAL_ADJUSTMENTS` | DOUBLE | NOT NULL |  | Total adjustments that have been applied to this charge |
| 16 | `TOTAL_CHARGES` | DOUBLE |  |  | Total charge amount for this line on the claim |
| 17 | `TOTAL_PAYMENTS` | DOUBLE | NOT NULL |  | Total Payments that have been applied to this charge |
| 18 | `TOTAL_UNITS` | DOUBLE |  |  | Units or days of service for this line on the claim |
| 19 | `TO_SERVICE_DT_TM` | DATETIME |  |  | To service date of charges on this line of the claim |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `VARIANCE_AMT` | DOUBLE | NOT NULL |  | Differences between estimated and actual reimbursement. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `PFT_LINE_ITEM_ID` |
| [DENIAL](DENIAL.md) | `PFT_LINE_ITEM_ID` |
| [PFT_BR_LINE_STATUS_DETAIL](PFT_BR_LINE_STATUS_DETAIL.md) | `PFT_LINE_ITEM_ID` |
| [PFT_LINE_ITEM_CHRG_RELTN](PFT_LINE_ITEM_CHRG_RELTN.md) | `PFT_LINE_ITEM_ID` |
| [PFT_LINE_ITEM_DETAIL](PFT_LINE_ITEM_DETAIL.md) | `PFT_LINE_ITEM_ID` |

