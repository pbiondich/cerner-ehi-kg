# REV_CODE_EXCEPTION

> Revenue Code Exception

**Description:** REV CODE EXCEPTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | This is the bill type such as HCFA 1450, Patient Stmt, or Client Invoice |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Health Plan ID |
| 9 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Nomenclature ID |
| 10 | `REVENUE_CD` | DOUBLE | NOT NULL |  | Revenue CD |
| 11 | `REV_CODE_EXCEPTION_ID` | DOUBLE | NOT NULL |  | Revenue Code Exception ID |
| 12 | `REV_CODE_FLAG` | DOUBLE | NOT NULL |  | Provides functionality for Claim Rollup functionality - Flag will determine Degree of Claim Rollup on a Revenue code by Revenue code basis. Flag Values - Default is 0 (Normal rollup processing), 1 (Skip Rollup Processing). |
| 13 | `SOURCE_VOCAB_CD` | DOUBLE | NOT NULL |  | Source Vocabulary Cd |
| 14 | `UB_BILL_CLASS_CD` | DOUBLE | NOT NULL |  | UB Bill Class Code |
| 15 | `UB_BILL_FREQ_CD` | DOUBLE | NOT NULL |  | UB Bill Frequency CD |
| 16 | `UB_FACILITY_TYPE_CD` | DOUBLE | NOT NULL |  | UB Facility Type CD |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

