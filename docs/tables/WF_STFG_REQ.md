# WF_STFG_REQ

> This table stores the header information of the result of the predictive calculation after the calculation is executed against a specified date and time in workforce solution.

**Description:** Workforce Staffing Requirements  
**Table type:** REFERENCE  
**Primary key:** `WF_STFG_REQ_ID`  
**Columns:** 24  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_CD` | DOUBLE | NOT NULL |  | Active code for the staffing template. |
| 2 | `ACTIVE_DT_TM` | DATETIME |  |  | The date time the template was activated. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACUITY_IND` | DOUBLE |  |  | Indicates the type of staffing calculator. 1 = acuity model, 0 = census model. |
| 6 | `ADJ_CENSUS_IND` | DOUBLE |  |  | Indicates if the staffing calculator will consider pending admits & discharges to calculate a total census. 1 = Accounts for pending admits / discharges 0 = No accout for pending admits / discharges |
| 7 | `ALLOW_MOD_IND` | DOUBLE |  |  | Indicates if the staffing recommendation can be manually updated. 1 = User allowed to modify staffing recommendations 0 = User not allowed to modify the recommended staffing |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BUDGETED_CENSUS` | DOUBLE |  |  | The budgeted census for a location |
| 10 | `DESCRIPTION` | VARCHAR(200) |  |  | Description of the staffing template. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EXCLUDE_PREADMIT_IND` | DOUBLE | NOT NULL |  | This indicator will determine whether pre-admit encounter will be excluded in the calculation of patient census. |
| 13 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location of the staffing recommendation |
| 14 | `MANUAL_A_D_IND` | DOUBLE |  |  | Indicates if pending admits and discharges can be manually captured when determining staffing requirements. 1 = User allowed to enter pending admits / discharges 0 = User not allowed to enter pending admits / discharges |
| 15 | `NAME` | VARCHAR(60) |  |  | Name of the staffing template |
| 16 | `PREV_WF_STFG_REQ_ID` | DOUBLE | NOT NULL | FK→ | Associates the staffing requirements calculator data to the previous staffing requirements calculator data; used for versioning. |
| 17 | `STATUS_CD` | DOUBLE | NOT NULL |  | Determines the status of the staffing template |
| 18 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the associated discrete element (task or assay) |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `WF_STFG_REQ_ID` | DOUBLE | NOT NULL | PK | Identifies the staffing requirements calculator data |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PREV_WF_STFG_REQ_ID` | [WF_STFG_REQ](WF_STFG_REQ.md) | `WF_STFG_REQ_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [WF_ACUITY](WF_ACUITY.md) | `WF_STFG_REQ_ID` |
| [WF_SHIFT_DISTRIBUTION](WF_SHIFT_DISTRIBUTION.md) | `WF_STFG_REQ_ID` |
| [WF_STFG_HDR](WF_STFG_HDR.md) | `WF_STFG_REQ_ID` |
| [WF_STFG_REQ](WF_STFG_REQ.md) | `PREV_WF_STFG_REQ_ID` |
| [WF_STFG_REQ_LINE](WF_STFG_REQ_LINE.md) | `WF_STFG_REQ_ID` |
| [WF_STFG_SHIFT_RELTN](WF_STFG_SHIFT_RELTN.md) | `WF_STFG_REQ_ID` |
| [WF_STFG_TIME](WF_STFG_TIME.md) | `WF_STFG_REQ_ID` |

