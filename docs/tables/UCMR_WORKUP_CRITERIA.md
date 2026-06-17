# UCMR_WORKUP_CRITERIA

> This table stores criteria for the case workup used to determine which workups need to be performed with specimens on a case

**Description:** Unified Case Management Reference Workup Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field indicates a valid body site for this criteria. A '0' value will indicate (Any) body site. |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Indicates a valid catalog item for this criteria. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource code value which helps determine the qualifying workup. |
| 8 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates a valid specimen type for this criteria. Will only be a valid specimen type for the selected catalog item. A '0' value will indicate (Any) specimen type. |
| 9 | `UCMR_CASE_WORKUP_ID` | DOUBLE | NOT NULL | FK→ | This field indicates the case workup this workup criteria is part of. |
| 10 | `UCMR_WORKUP_CRITERIA_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the case workup version. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_WORKUP_ID` | [UCMR_CASE_WORKUP](UCMR_CASE_WORKUP.md) | `UCMR_CASE_WORKUP_ID` |

