# SCH_AT_ENCNTR_TYPE_R

> Links an appointment type to a list of related encounter types.

**Description:** Scheduling Appointment Type Encounter Type Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Parent appointment type code. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type related to the appointment type. |
| 8 | `SCH_ACTION_CD` | DOUBLE | NOT NULL |  | The scheduling where the relationship is effective. The default is SCHEDULE. Another example would be CHECKIN which would mean that when the appointment is checked in, its encounter type should be one of the related encounter types built for the action of Check In. |
| 9 | `SCH_AT_ENCNTR_TYPE_R_ID` | DOUBLE | NOT NULL |  | The unique primary key of the SCH_AT_ENCNTR_TYPE_R table. |
| 10 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [SCH_APPT_TYPE](SCH_APPT_TYPE.md) | `APPT_TYPE_CD` |

