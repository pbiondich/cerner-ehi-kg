# SURG_REQ

> Contains information about a surgical request

**Description:** Surgical Request  
**Table type:** ACTIVITY  
**Primary key:** `SURG_REQ_ID`  
**Columns:** 25  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANESTHESIA_CD` | DOUBLE | NOT NULL |  | The type of anesthesia to use for this surgical request |
| 3 | `BLOCK_TIME_IND` | DOUBLE | NOT NULL |  | Whether or not the surgeon's time should be blocked during this surgical request |
| 4 | `CONCURRENT_PROC_IND` | DOUBLE | NOT NULL |  | Whether or not all procedures for this surgical request can be performed concurrently |
| 5 | `DATE_REQ_TYPE_FLAG` | DOUBLE | NOT NULL |  | Which date time field to use where 0 = timeframe_cd, 1=req_start_dt_tm and req_end_dt_tm, and 2 = req_date_free-text |
| 6 | `DEFER_ANESTHESIA_IND` | DOUBLE | NOT NULL |  | Whether or not the anesthesia type is deferred to the anesthesiologist |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID of the Surgery Request submitted |
| 8 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility for this surgical request |
| 9 | `IN_PROGRESS_IND` | DOUBLE | NOT NULL |  | Indicates if a row should considered as a surgical request that is being saved to be finished at a later time. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location for this surgical request |
| 11 | `PATIENT_TYPE_CD` | DOUBLE | NOT NULL |  | The patient's type (e.g. inpatient or outpatient) |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person ID for this surgical request |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the person who originally created the Surgery Request |
| 14 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the surgical request |
| 15 | `REQ_DATE_FREETEXT` | VARCHAR(255) |  |  | A free text field for requesting a timeframe for this surgical request |
| 16 | `REQ_END_DT_TM` | DATETIME |  |  | The requested end date time for this surgical request |
| 17 | `REQ_START_DT_TM` | DATETIME |  |  | The requested begin date time for this surgical request |
| 18 | `SUBMIT_DT_TM` | DATETIME |  |  | The time and date of this surgical request was submitted. |
| 19 | `SURG_REQ_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 20 | `TIMEFRAME_CD` | DOUBLE | NOT NULL |  | A granular timeframe for this surgical request |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SURG_REQ_FAVORITE](SURG_REQ_FAVORITE.md) | `SURG_REQ_ID` |
| [SURG_REQ_ORDER_R](SURG_REQ_ORDER_R.md) | `SURG_REQ_ID` |
| [SURG_REQ_PLAN_R](SURG_REQ_PLAN_R.md) | `SURG_REQ_ID` |
| [SURG_REQ_PROC_GROUP](SURG_REQ_PROC_GROUP.md) | `SURG_REQ_ID` |

