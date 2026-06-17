# BR_DTA_RRF

> legacy dta reference ranges

**Description:** BEDROCK DTA RRF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_FROM` | DOUBLE | NOT NULL |  | beginning age |
| 2 | `AGE_FROM_UNITS` | VARCHAR(25) |  |  | beginning age units (month/year) |
| 3 | `AGE_TO` | DOUBLE | NOT NULL |  | ending age |
| 4 | `AGE_TO_UNITS` | VARCHAR(25) |  |  | ending age units (month/year) |
| 5 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 6 | `CRITICAL_HIGH` | DOUBLE | NOT NULL |  | critical high |
| 7 | `CRITICAL_IND` | DOUBLE |  |  | Indicates if critical_high, critical_low, or both are valued. |
| 8 | `CRITICAL_LOW` | DOUBLE | NOT NULL |  | critical low |
| 9 | `DILUTE_IND` | DOUBLE | NOT NULL |  | Defined as 1 the dilute indicator is defined. |
| 10 | `DTA_ID` | DOUBLE | NOT NULL |  | Legacy assay id. |
| 11 | `FEASIBLE_HIGH` | DOUBLE | NOT NULL |  | feasible high |
| 12 | `FEASIBLE_IND` | DOUBLE |  |  | Indicates if feasible_high, feasible_low, or both are valued. |
| 13 | `FEASIBLE_LOW` | DOUBLE | NOT NULL |  | feasible low |
| 14 | `LINEAR_HIGH` | DOUBLE | NOT NULL |  | linear high |
| 15 | `LINEAR_IND` | DOUBLE |  |  | Indicates if linear_high, linear_low, or both are valued. |
| 16 | `LINEAR_LOW` | DOUBLE | NOT NULL |  | linear low |
| 17 | `NORMAL_HIGH` | DOUBLE | NOT NULL |  | normal high |
| 18 | `NORMAL_IND` | DOUBLE |  |  | Indicates if normal_high, normal_low, or both are valued. |
| 19 | `NORMAL_LOW` | DOUBLE | NOT NULL |  | normal low |
| 20 | `REVIEW_HIGH` | DOUBLE | NOT NULL |  | review high |
| 21 | `REVIEW_IND` | DOUBLE |  |  | Indicates if review_high, review_low, or both are valued. |
| 22 | `REVIEW_LOW` | DOUBLE | NOT NULL |  | review low |
| 23 | `RRF_ID` | DOUBLE | NOT NULL |  | Reference range ID. |
| 24 | `SERVICE_RESOURCE` | VARCHAR(40) |  |  | Service resource for the reference range |
| 25 | `SEX` | VARCHAR(12) |  |  | gender |
| 26 | `UNKNOWN_AGE_IND` | DOUBLE | NOT NULL |  | indicates unknown age |
| 27 | `UOM` | VARCHAR(40) |  |  | The unit of measure. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

