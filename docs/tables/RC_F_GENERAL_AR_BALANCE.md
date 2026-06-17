# RC_F_GENERAL_AR_BALANCE

> This table contains data related to General AR account balances.

**Description:** Revenue Cycle Fact General AR Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | **obsolete** This column is no longer being used. It has been replaced by the begin_dt_nbr and end_dt_nbr. A number representing the activity date. References the key in the OMF_DATE table. ** obsolete** |
| 2 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** No longer used. Contains the Balance of the General AR account. *** Obsolete *** |
| 3 | `BEGIN_BALANCE_AMT` | DOUBLE |  |  | The opening balance for the given activity date. |
| 4 | `BEGIN_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the begin date of this balance fact row. References the related row in the OMF_DATE table. |
| 5 | `DAILY_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the adjustment amount per day. |
| 6 | `DAILY_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the payment amount per day. |
| 7 | `END_BALANCE_AMT` | DOUBLE |  |  | The ending balance for the given activity date. |
| 8 | `END_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the end date of this balance fact row. References the related row in the OMF_DATE table. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 10 | `LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the most recent adjustment date of this fact row. References the related row on the OMF_DATE table. |
| 11 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the most recent adjustment date of this fact row. References the related row on the OMF_Date table. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 13 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 14 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact. |
| 15 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL |  | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 16 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies billing entity information related to this fact row. |
| 17 | `RC_F_GENERAL_AR_BALANCE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies General AR Balance information. |
| 18 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 19 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | ** obsolete ** this column is no longer being used. Contains the total of the adjustments. ** obsolete ** |
| 20 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | ** obsolete ** This column is no longer being used. Contains the total of the payments. ** obsolete ** |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `BEGIN_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `END_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |

