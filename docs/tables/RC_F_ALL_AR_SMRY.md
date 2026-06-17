# RC_F_ALL_AR_SMRY

> This table contains data related to All AR account summary - Client AR, General AR, Patient AR, Non AR

**Description:** Revenue Cycle Fact All Accounts Receivable Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | Represents the activity date. References the key on the OMF_DATE table.. |
| 2 | `ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the adjustment amount for each AR account. |
| 3 | `BEGIN_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the Begin Balance for each AR account. |
| 4 | `CHARGE_AMT` | DOUBLE | NOT NULL |  | This will store the Total Charge Amount for Patient AR, Balance AR and Client AR |
| 5 | `END_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the End Balance for each AR account. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 9 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the payment amount for each AR account. |
| 10 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the account type information related to this fact row. |
| 11 | `RC_D_BALANCE_TYPE_ID` | DOUBLE |  | FK→ | Uniquely identifies the related fow on the RC_D_BALANCE_TYPE table. |
| 12 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies billing entity information related to this fact row. |
| 13 | `RC_F_ALL_AR_SMRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_ALL_AR_SMRY. |
| 14 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone in which the GSR job is running. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_BALANCE_TYPE_ID` | [RC_D_BALANCE_TYPE](RC_D_BALANCE_TYPE.md) | `RC_D_BALANCE_TYPE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |

