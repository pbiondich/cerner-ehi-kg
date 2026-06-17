# ENCNTR_CMNTY_CASE

> Stores information about community case management.

**Description:** Encounter Community Case  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_CMNTY_CASE_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CASE_STATUS_CD` | DOUBLE | NOT NULL |  | The case status identifies the state of a particular case from the time it is initiated until it is closed (i.3., new, pending enrollment, enrolled, active, pending closure, closed). |
| 6 | `CLOSURE_REASON_CD` | DOUBLE | NOT NULL |  | The reason the case was closed. |
| 7 | `ENCNTR_CMNTY_CASE_ID` | DOUBLE | NOT NULL | PK | Stores information about community case management. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Encounter. |
| 9 | `ENROLLMENT_DT_TM` | DATETIME |  |  | The date and time of the patient's enrollment on the case encounter. |
| 10 | `INITIAL_IDENT_DT_TM` | DATETIME |  |  | The date and time the case was initially identified. |
| 11 | `REFERRAL_REASON_CD` | DOUBLE | NOT NULL |  | The reason the case was referred. |
| 12 | `RISK_FACTOR_SCORE_NBR` | DOUBLE | NOT NULL |  | The decimal number value representing the risk factor score of the patient. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ENCNTR_CMNTY_CASE_ID_PGM](ENCNTR_CMNTY_CASE_ID_PGM.md) | `ENCNTR_CMNTY_CASE_ID` |
| [ENCNTR_CMNTY_CASE_RISK_DRV](ENCNTR_CMNTY_CASE_RISK_DRV.md) | `ENCNTR_CMNTY_CASE_ID` |

