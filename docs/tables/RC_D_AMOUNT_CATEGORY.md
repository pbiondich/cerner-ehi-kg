# RC_D_AMOUNT_CATEGORY

> Contains pre-defined currency range categories.

**Description:** Revenue Cycle Dimension Amount Category  
**Table type:** REFERENCE  
**Primary key:** `RC_D_AMOUNT_CATEGORY_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_AMOUNT` | DOUBLE | NOT NULL |  | The beginning amount for this category. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CATEGORY_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | The textual description of the given amount category. |
| 5 | `END_AMOUNT` | DOUBLE | NOT NULL |  | The ending amount for this category. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 10 | `RC_D_AMOUNT_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a given amount category. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_BAL_AMT_CATEGORY_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_UNBILLED_BAL_AMT_CAT_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_BAL_AMT_CATEGORY_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_UNBILLED_BAL_AMT_CAT_ID` |

