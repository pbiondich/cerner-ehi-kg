# RC_F_INVOICE_AR_BAL_INV

> This table contains summarized client AR balance data at the account level.

**Description:** Revenue Cycle Fact Invoice AR Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 6 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | The invoice balance amount that is due. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 10 | `GENERATION_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date the invoice was generated. |
| 11 | `INVOICE_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity date and the submission date of the bill. |
| 12 | `INVOICE_IDENT` | VARCHAR(40) | NOT NULL |  | Contains the display value assoicated to an invoice. |
| 13 | `LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the most recent adjustment date of this balance fact row. References the key in the OMF_DATE table. |
| 14 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made against the invoice. Related to the OMF_DATE table. |
| 15 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 16 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related row on the Millennium BILL_REC table |
| 17 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 18 | `ORIG_BALANCE_AMT` | DOUBLE |  |  | Contains the original invoice balance. |
| 19 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact row. |
| 20 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account type information related to this fact row. |
| 21 | `RC_D_AGE_BY_INVOICE_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category. |
| 22 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifiies the billing entity related to this fact row. |
| 23 | `RC_F_INVOICE_AR_BAL_INV_ID` | DOUBLE | NOT NULL |  | Contains accounts receivable balance invoice summary information. |
| 24 | `SUBMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date the invoice was submitted. Relates to the OMF Date table. |
| 25 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 26 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE |  |  | The total adjustment made against the invoice. |
| 27 | `TOTAL_CHARGE_AMT` | DOUBLE |  |  | The total charge made against the invoice. |
| 28 | `TOTAL_PAYMENT_AMT` | DOUBLE |  |  | The total payment made against the invoice. |
| 29 | `TRANSMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date the invoice was transmitted. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `GENERATION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_AGE_BY_INVOICE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `SUBMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `TRANSMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |

