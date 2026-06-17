# UCMR_REQUIRED_STEP

> This table stores case steps that are dependent on other case steps.

**Description:** Unified Case Management Reference Required Step  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_WORKUPS_IND` | DOUBLE | NOT NULL |  | Indicates if the required step must be completed across all instances of this workup, Not just the same instance of the workup. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `REQUIRED_UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | This field is a unique identifier for the required case step version. |
| 7 | `UCMR_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | This field indicates the case step that has other steps that are required before it can be accessed. |
| 8 | `UCMR_REQUIRED_STEP_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the required case step version. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REQUIRED_UCMR_CASE_STEP_ID` | [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_STEP_ID` |
| `UCMR_CASE_STEP_ID` | [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_STEP_ID` |

