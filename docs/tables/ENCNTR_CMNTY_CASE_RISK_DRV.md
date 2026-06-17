# ENCNTR_CMNTY_CASE_RISK_DRV

> The contribution that each condition (clinical category) contributes to the clinical portion of each individual's total risk score for the community case.

**Description:** Encounter Community Case Risk Driver  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CODING_SYSTEM_IDENT` | VARCHAR(255) |  |  | The external unique coding system identifier of the risk driver. |
| 6 | `ENCNTR_CMNTY_CASE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter community case. |
| 7 | `ENCNTR_CMNTY_CASE_RISK_DRV_ID` | DOUBLE | NOT NULL |  | The contribution that each condition (clinical category) contributes to the clinical portion of each individual's total risk score for the community case. |
| 8 | `RISK_DRIVER_DISPLAY_TXT` | VARCHAR(255) |  |  | The display of the clinical risk driver. |
| 9 | `RISK_DRIVER_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | The numeric or string representation of the clinical risk driver. |
| 10 | `SOURCE_IDENT` | VARCHAR(255) | NOT NULL |  | The external unique source identifier of the clinical risk driver. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_CMNTY_CASE_ID` | [ENCNTR_CMNTY_CASE](ENCNTR_CMNTY_CASE.md) | `ENCNTR_CMNTY_CASE_ID` |

