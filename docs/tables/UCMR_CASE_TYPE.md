# UCMR_CASE_TYPE

> This table stores high level case type information.

**Description:** Unified Case Management Reference Case Type  
**Table type:** REFERENCE  
**Primary key:** `UCMR_CASE_TYPE_ID`  
**Columns:** 14  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CASE_TYPE_CAT_CD` | DOUBLE | NOT NULL |  | Indicates the catalog item to which this case step information is related. This orderable will be used for tracking purposes and will be assigned to the case accession number. |
| 5 | `CASE_TYPE_DESC_TEXT` | VARCHAR(250) |  |  | This field contains a brief description of the case type. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `META_CASE_IND` | DOUBLE | NOT NULL |  | Indicates if this case type is a meta case, or a grouping of other cases. |
| 8 | `STATUS_CAT_CD` | DOUBLE | NOT NULL |  | Indicates the catalog item that this case type will use to help control the case status. |
| 9 | `UCMR_CASE_TYPE_ID` | DOUBLE | NOT NULL | PK | This field contains a unique identifier for the case type version. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [UCMR_CASE_CHARGE_ORDRBL_R](UCMR_CASE_CHARGE_ORDRBL_R.md) | `UCMR_CASE_TYPE_ID` |
| [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_TYPE_ID` |
| [UCMR_CASE_TRIGGER](UCMR_CASE_TRIGGER.md) | `UCMR_CASE_TYPE_ID` |
| [UCMR_CASE_WORKUP](UCMR_CASE_WORKUP.md) | `UCMR_CASE_TYPE_ID` |
| [UCM_CASE](UCM_CASE.md) | `UCMR_CASE_TYPE_ID` |

