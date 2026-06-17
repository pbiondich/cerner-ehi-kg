# UCMR_CASE_WORKUP

> This table stores specific information for each workup of a case type.

**Description:** Unified Case Management  
**Table type:** REFERENCE  
**Primary key:** `UCMR_CASE_WORKUP_ID`  
**Columns:** 13  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `UCMR_CASE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This field indicates the case type of this workup. |
| 6 | `UCMR_CASE_WORKUP_ID` | DOUBLE | NOT NULL | PK | This field is a unique identifier for the case workup version. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORKUP_NAME` | VARCHAR(40) |  |  | This field indicates the client defined name of this workup. |
| 13 | `WORKUP_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The sequence number of the case workup in context of other workups in same case type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_TYPE_ID` | [UCMR_CASE_TYPE](UCMR_CASE_TYPE.md) | `UCMR_CASE_TYPE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [UCMR_CASE_STEP](UCMR_CASE_STEP.md) | `UCMR_CASE_WORKUP_ID` |
| [UCMR_WORKUP_CRITERIA](UCMR_WORKUP_CRITERIA.md) | `UCMR_CASE_WORKUP_ID` |
| [UCMR_WS_STMT_ASSAY_R](UCMR_WS_STMT_ASSAY_R.md) | `UCMR_CASE_WORKUP_ID` |

