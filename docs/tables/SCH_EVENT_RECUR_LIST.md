# SCH_EVENT_RECUR_LIST

> Table to store the information about how a future instance of a recurring appointment should be booked.

**Description:** Scheduling Event Recurring List  
**Table type:** ACTIVITY  
**Primary key:** `SCH_EVENT_RECUR_LIST_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_MINUTE_NBR` | DOUBLE | NOT NULL |  | Additional minutes to be added to the recurring instances. |
| 2 | `APPT_REASON_FREE` | VARCHAR(255) |  |  | The free text reason the appointment was requested. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. it is an internal system assigned number. |
| 4 | `EVENT_RECUR_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the associated sch_event_recur table. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. |
| 6 | `OVERRIDE_DURATION_MINUTE_NBR` | DOUBLE | NOT NULL |  | The duration (in minutes) of the patient override. |
| 7 | `PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of health insurance profile for the person plan profile row (i.e., professional, institutional, workmen's comp). |
| 8 | `RES_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the associated scheduling resource. |
| 9 | `SCH_EVENT_RECUR_LIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_LIST table. |
| 10 | `SEQ_NBR` | DOUBLE | NOT NULL |  | The instance sequence for recurring series within one date. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EVENT_RECUR_ID` | [SCH_EVENT_RECUR](SCH_EVENT_RECUR.md) | `EVENT_RECUR_ID` |
| `RES_LIST_ID` | [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `RES_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCH_EVENT_RECUR_ROLE](SCH_EVENT_RECUR_ROLE.md) | `SCH_EVENT_RECUR_LIST_ID` |
| [SCH_FREQ_DATE](SCH_FREQ_DATE.md) | `SCH_EVENT_RECUR_LIST_ID` |

