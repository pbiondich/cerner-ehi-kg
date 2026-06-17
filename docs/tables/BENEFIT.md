# BENEFIT

> A benefit related to a base health plan or to an employer-tailored plan

**Description:** BENEFIT  
**Table type:** REFERENCE  
**Primary key:** `BENEFIT_ID`  
**Columns:** 23  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BENEFIT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a benefit category |
| 7 | `BENEFIT_MOD_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the benefit record adds to an existing benefit, nullifies an existing benefit, or changes an existing benefit |
| 8 | `BNFT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value representing a benefit category (type of benefit) |
| 9 | `DX_CODE_MAX` | VARCHAR(50) |  |  | The highest diagnosis code of a range of codes for which this benefit applies |
| 10 | `DX_CODE_MIN` | VARCHAR(50) |  |  | The minimum diagnosis code of a range for which this benefit applies. |
| 11 | `DX_DESCRIPTION` | VARCHAR(100) |  |  | Description of the diagnosis for which this benefit applies. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `ORG_PLAN_RELTN_ID` | DOUBLE | NOT NULL |  | Foreign key to the org_plan_reltn table. Identifies the relationship to which this benefit is tied. |
| 14 | `PARENT_BNFT_ID` | DOUBLE |  |  | The ID of the benefit to which this benefit is related |
| 15 | `SOFT_BENEFIT_TEXT` | VARCHAR(200) |  |  | Text description of a benefit |
| 16 | `SPECIALTY_CD` | DOUBLE |  |  | The code value for the specialty for which this benefit applies if it is a specialty related benefit. |
| 17 | `SUB_TYPE_DISPLAY` | VARCHAR(100) |  |  | User-definable display value for the benefits subtype |
| 18 | `TYPE_DISPLAY` | VARCHAR(100) |  |  | User-definable display for the benefit type |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BENEFIT_DETAIL](BENEFIT_DETAIL.md) | `BENEFIT_ID` |

