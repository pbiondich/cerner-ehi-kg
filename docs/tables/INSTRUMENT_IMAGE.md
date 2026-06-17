# INSTRUMENT_IMAGE

> Contains scattergram image activity data associated to results.

**Description:** Instrument Image  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `INSTRUMENT_IMAGE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies scattergram image activity data associated to results. |
| 6 | `PERFORM_DT_TM` | DATETIME | NOT NULL |  | Performed data and time of the result associated to the image. |
| 7 | `REPEAT_NBR` | DOUBLE | NOT NULL |  | Keeps track of the number of times a dta has been resulted. |
| 8 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | Relates this image activity data to a specific result. |
| 9 | `RESULT_IMAGE_NAME` | VARCHAR(64) |  |  | Handle to scattergram image stored in MMF. |
| 10 | `RESULT_IMAGE_VRSN_NBR` | DOUBLE | NOT NULL |  | Version number needed for retrieving result image from the MMF data archive. |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource code for instrument. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |

