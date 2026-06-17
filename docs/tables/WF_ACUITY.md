# WF_ACUITY

> This table contains the (patient) acuity included in the predictive calculation of the number of staff requuired in the shift.

**Description:** Workforce staffing time table  
**Table type:** REFERENCE  
**Primary key:** `WF_ACUITY_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACUITY_LEVEL` | DOUBLE |  |  | The associated acuity level to a workforce staffing |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CENSUS_CUTOFF_NBR` | DOUBLE | NOT NULL |  | Minimum number of patients that must be present before a category (refers to unit secretary, charge nurse) is needed. |
| 5 | `DESCRIPTION` | VARCHAR(400) |  |  | Description of the acuity level of workforce staffing |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PREV_WF_ACUITY_ID` | DOUBLE | NOT NULL | FK→ | Associates the processing acuity level (times) of workforce staffing to the previous processing acuity level (times) of workforce staffing |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WF_ACUITY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the processing acuity level (times) of workforce staffing |
| 14 | `WF_STFG_REQ_ID` | DOUBLE | NOT NULL | FK→ | Associates staffing requirements calculator data |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_WF_ACUITY_ID` | [WF_ACUITY](WF_ACUITY.md) | `WF_ACUITY_ID` |
| `WF_STFG_REQ_ID` | [WF_STFG_REQ](WF_STFG_REQ.md) | `WF_STFG_REQ_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WF_ACUITY](WF_ACUITY.md) | `PREV_WF_ACUITY_ID` |
| [WF_STFG_REQ_LINE](WF_STFG_REQ_LINE.md) | `WF_ACUITY_ID` |

