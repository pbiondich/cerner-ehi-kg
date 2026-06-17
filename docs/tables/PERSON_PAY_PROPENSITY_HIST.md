# PERSON_PAY_PROPENSITY_HIST

> Table stores historical information about payment propensity scores and accompanying data for a person.

**Description:** Person Payment Propensity History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL |  | The information describing the source of the person's payment propensity information. Examples may include various third party transactions or manual entry (name of the hospital). |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `ESTIMATED_HOUSEHOLD_INCOME_AMT` | DOUBLE |  |  | The estimated total income of those living within the person's household. |
| 10 | `ESTIMATED_HOUSEHOLD_SIZE_CNT` | DOUBLE |  |  | The estimated number of people in the person's household. A household usually includes the tax filer, their spouse if they have one, and their tax dependents. |
| 11 | `HEALTHCARE_CREDIT_SCORE_VALUE` | DOUBLE |  |  | The FICO propensity score for healthcare that is used to evaluate the probability that a person will pay off their healthcare debt. |
| 12 | `NUMBER_OF_BANKRUPTCIES_CNT` | DOUBLE |  |  | A person's number of open bankruptcies. |
| 13 | `PERSON_PAYMENT_PROPENSITY_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the PERSON_PAYMENT_PROPENSITY table. |
| 14 | `PERSON_PAY_PROPENSITY_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON_PAY_PROPESNITY_HIST table. |
| 15 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 16 | `SCORE_DESC` | VARCHAR(100) |  |  | The description of the payment propensity score value. |
| 17 | `SCORE_VALUE_TXT` | VARCHAR(20) |  |  | The score is a value, often a number, assigned to a person that indicates their propensity to make payment on bills for healthcare services rendered. |
| 18 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 19 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_PAYMENT_PROPENSITY_ID` | [PERSON_PAYMENT_PROPENSITY](PERSON_PAYMENT_PROPENSITY.md) | `PERSON_PAYMENT_PROPENSITY_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

