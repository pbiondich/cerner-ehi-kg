# PFT_CM_ERROR_DETAIL

> Stores a list of Cerner Contract Management Error Details for a Bill Record

**Description:** Patient Accounting Cerner Contract Management Error Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CCM_ERROR_CAT_CD` | DOUBLE | NOT NULL |  | Code value for the Error Category |
| 4 | `CCM_ERROR_CODE` | VARCHAR(20) |  |  | Code provided for the error from Cerner Contract Management. |
| 5 | `CCM_ERROR_DESC` | VARCHAR(1000) |  |  | Error description received from Cerner Contract Management |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PFT_CM_ERROR_DETAIL_ID` | DOUBLE | NOT NULL |  | Uniquely generated number that identifies a single row on the PFT_CM_ERROR_DETAIL table. |
| 8 | `PFT_CM_ERROR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the PFT_CM_ERROR table. |
| 9 | `RESOLUTION_ACTION_DT_TM` | DATETIME |  |  | Date and Time of a resolution action being applied. |
| 10 | `RESOLUTION_ACTION_FLAG` | DOUBLE |  |  | Flag denoting the resolution action applied. |
| 11 | `RESOLUTION_ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifier for the personnel applying the resolution action. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_CM_ERROR_ID` | [PFT_CM_ERROR](PFT_CM_ERROR.md) | `PFT_CM_ERROR_ID` |

