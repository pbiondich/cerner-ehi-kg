# PERSON_PAYMENT_PROPENSITY

> Table stores payment propensity scores and accompanying data for a person.

**Description:** Person Payment Propensity  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PAYMENT_PROPENSITY_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL |  | The information describing the source of the person's payment propensity information. Examples may include various third party transactions or manual entry (name of the hospital). |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `ESTIMATED_HOUSEHOLD_INCOME_AMT` | DOUBLE |  |  | The estimated total income of those living within the person's household. |
| 9 | `ESTIMATED_HOUSEHOLD_SIZE_CNT` | DOUBLE |  |  | The estimated number of people in the person's household. A household usually includes the tax filer, their spouse if they have one, and their tax dependents. |
| 10 | `HEALTHCARE_CREDIT_SCORE_VALUE` | DOUBLE |  |  | The FICO propensity score for healthcare that is used to evaluate the probability that a person will pay off their healthcare debt. |
| 11 | `NUMBER_OF_BANKRUPTCIES_CNT` | DOUBLE |  |  | A person's number of open bankruptcies. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to store the identifier for the parent. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Used to store the identifier for the parent. |
| 14 | `PERSON_PAYMENT_PROPENSITY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PERSON_PAYMENT_PROPENSITY table. |
| 15 | `SCORE_DESC` | VARCHAR(100) |  |  | The description of the payment propensity score value. |
| 16 | `SCORE_VALUE_TXT` | VARCHAR(20) |  |  | The score is a value, often a number, assigned to a person that indicates their propensity to make payment on bills for healthcare services rendered. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PAY_PROPENSITY_HIST](PERSON_PAY_PROPENSITY_HIST.md) | `PERSON_PAYMENT_PROPENSITY_ID` |

