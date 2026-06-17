# RC_F_INVOICE_AR_BALANCE

> This table contains data related to client invoices.

**Description:** Revenue Cycle Fact Invoice AR Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the admit date. |
| 3 | `BALANCE_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** This column is no longer being used. Contains the invoice balance. ** Obsolete ** |
| 4 | `BILL_AGE` | DOUBLE | NOT NULL |  | ** Obsolete ** This column is no longer being used. Contains the number of days that result from the difference between the current activity data and the transmission date of the bill. ** Obsolete ** |
| 5 | `BILL_NUMBER_IDENT` | VARCHAR(40) | NOT NULL |  | Contains the display value associated to a bill number. |
| 6 | `DAILY_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** - No longer used. Contains the adjustment amount per day. ** Obsolete ** |
| 7 | `DAILY_CHARGE_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** - No longer used. Contains the daily charge amount per day. ** Obsolete **. |
| 8 | `DAILY_PAYMENT_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** - No longer used. Contains the payment amount per day. ** Obsolete ** |
| 9 | `DISCHARGE_DT_NBR` | DOUBLE |  | FK→ | The Discharge Date of the Patient |
| 10 | `FIN_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | Financial Number of the patient |
| 11 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 12 | `INVOICE_AGE` | DOUBLE | NOT NULL |  | Contains the number of days that result from the difference between the current activity date and the submission date of the bill. |
| 13 | `INVOICE_BALANCE_AMT` | DOUBLE |  |  | Contains the invoice balance due. |
| 14 | `INVOICE_GENERATION_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date the invoice was generated. |
| 15 | `INVOICE_LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a adjusment was made to the financial encounter. |
| 16 | `INVOICE_LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made against the invoice. |
| 17 | `INVOICE_ORIG_BALANCE_AMT` | DOUBLE | NOT NULL |  | Contains the original invoice balance. |
| 18 | `INVOICE_SUBMISSION_DT_NBR` | DOUBLE |  | FK→ | The date the invoice was submited |
| 19 | `INVOICE_TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments at invoice level |
| 20 | `INVOICE_TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Contains the total of the charges at invoice level |
| 21 | `INVOICE_TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the payments at invoice level |
| 22 | `INVOICE_TRANSMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date the invoice was transmitted |
| 23 | `LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | ** Obsolete ** - No longer used. Date of the last time a adjusment was made to the financial encounter. ** Obsolete ** |
| 24 | `LAST_CHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | ** Obsolete ** No longer being used. Date of the last time a charge was posted to the financial encounter. ** Obsolete ** |
| 25 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | ** Obsolete ** - No longer being used. Date of the last time a payment was made to the financial encounter. ** Obsolete ** |
| 26 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 27 | `MILL_CORSP_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related BILL_REC row on Millennium. |
| 28 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 29 | `MILL_PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium Profit Encounter record that relates to this fact row. |
| 30 | `MRN_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | Identifier of a medical record number. |
| 31 | `ORIGINAL_BILL_DT_NBR` | DOUBLE | NOT NULL |  | ** Obsolete ** This column is no longer being used. A number representing the original bill date. References the key in the OMF_DATE table. ** Obsolete ** |
| 32 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact. |
| 33 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 34 | `RC_D_AGE_BY_BILL_ID` | DOUBLE | NOT NULL | FK→ | ** Obsolete ** This column is no longer being used. Relates this fact row to a specific age category. ** Obsolete ** |
| 35 | `RC_D_AGE_BY_INVOICE_ID` | DOUBLE | NOT NULL | FK→ | Relates this fact row to a specific age category. |
| 36 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 37 | `RC_D_BILL_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies bill property information related to this fact row |
| 38 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies encounter type class information related to this fact row |
| 39 | `RC_F_INVOICE_AR_BALANCE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data related to client invoices. |
| 40 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies location information related to this fact row. |
| 41 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies person information related to this fact row. |
| 42 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted |
| 43 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** No longer being used. The total of the adjustments. ** Obsolete ** |
| 44 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** - No longer used. The total of the charges. ** Obsolete ** |
| 45 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | ** Obsolete ** No longer used. The total of the payments. ** Obsolete ** |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INVOICE_GENERATION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INVOICE_LAST_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INVOICE_LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INVOICE_SUBMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INVOICE_TRANSMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_CHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_AGE_BY_BILL_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_AGE_BY_INVOICE_ID` | [RC_D_AGE_CATEGORY](RC_D_AGE_CATEGORY.md) | `RC_D_AGE_CATEGORY_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |
| `RC_D_BILL_PROPERTY_ID` | [RC_D_BILL_PROPERTY](RC_D_BILL_PROPERTY.md) | `RC_D_BILL_PROPERTY_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

