# RC_D_BILL_TYPE

> This table contains bill type information such as the bill type.

**Description:** Revenue Cycle Dimension Bill Type  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BILL_TYPE_ID`  
**Columns:** 13  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILL_TYPE` | VARCHAR(40) | NOT NULL |  | Identifies the type of bill (i.e. Client Invoice, Patient Invoice, HCFA 1500, etc. ) |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `MILL_BILL_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the Bill Type code on the Millennium table from which this row was derived. |
| 8 | `RC_D_BILL_TYPE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies bill type information. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (11)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_DAILY_CLAIM_EVENT_SMRY](RC_F_DAILY_CLAIM_EVENT_SMRY.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_MONTHLY_CLAIM_EVENT_SMRY](RC_F_MONTHLY_CLAIM_EVENT_SMRY.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_BILL_TYPE_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_BILL_TYPE_ID` |

