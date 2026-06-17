# PFT_BILL_ACTIVITY

> Relates bill activity to a benefit order health plan for pre-billing and charge balance evaluation.

**Description:** ProFit Bill Activity  
**Table type:** ACTIVITY  
**Primary key:** `PFT_BILL_ACTIVITY_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_AMT` | DOUBLE |  |  | Specifies the amount of a bill activity (Payment, Adjustment, Charge, co-pay, co-insurance, etc.). |
| 2 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date and time the bill activity occurred. |
| 3 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated transaction from TRANS_LOG |
| 4 | `AMT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of amount (Payment, Adjustment, Charge, co-pay, co-insurance, etc.). |
| 5 | `BILLED_DT_TM` | DATETIME |  |  | Date and time the bill activity occurred. |
| 6 | `BILL_ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Subtype of activity (Co-Pay, Transfer, etc.) |
| 7 | `BILL_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of activity (Payment, Adjustment, Balance Forward, etc.) |
| 8 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | Identifies the version of the bill record. |
| 9 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The benefit order health plan the charge or bill is related to. |
| 10 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | The related bill record. |
| 11 | `PFT_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the balance to which this activity is associated. |
| 12 | `PFT_BILL_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Identifies the activity for a bill record |
| 13 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated charge to the bill record activity. |
| 14 | `TRANSFER_AMT` | DOUBLE |  |  | Amount of transfer (balance transfer), if applicable. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `PFT_BALANCE_ID` | [PFT_BALANCE](PFT_BALANCE.md) | `PFT_BALANCE_ID` |
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_LINE_ITEM_ACTIVITY](PFT_LINE_ITEM_ACTIVITY.md) | `PFT_BILL_ACTIVITY_ID` |

