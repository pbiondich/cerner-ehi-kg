# SCH_APPT_COMP

> Define the children of a Protocol

**Description:** Appointment Type Components  
**Table type:** REFERENCE  
**Primary key:** `APPT_TYPE_CD`, `LOCATION_CD`, `SEQ_NBR`  
**Columns:** 30  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | PK FK→ | The identifier for an appointment type. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `COMP_APPT_SYNONYM_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the component appointment synonym. |
| 9 | `COMP_APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the component appointment type. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The field identifies the current permanent location of the patient. |
| 12 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 13 | `OFFSET_BEG_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset Beg Units |
| 14 | `OFFSET_BEG_UNITS_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Offset Beg Units Code |
| 15 | `OFFSET_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset Beg Units Meaning |
| 16 | `OFFSET_END_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset End Units |
| 17 | `OFFSET_END_UNITS_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Offset End Units Code |
| 18 | `OFFSET_END_UNITS_MEANING` | VARCHAR(12) |  |  | Scheduling Offset End Units Meaning |
| 19 | `OFFSET_FROM_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Offset From Type Code |
| 20 | `OFFSET_FROM_MEANING` | VARCHAR(12) |  |  | Scheduling Offset From Type Meaning |
| 21 | `OFFSET_SEQ_NBR` | DOUBLE | NOT NULL |  | Offset Sequence Number |
| 22 | `OFFSET_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Offset Type Code |
| 23 | `OFFSET_TYPE_MEANING` | VARCHAR(12) |  |  | Scheduling Offset Type Meaning |
| 24 | `SEQ_NBR` | DOUBLE | NOT NULL | PK | Determines the order among the children of a group. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [SCH_APPT_LOC](SCH_APPT_LOC.md) | `APPT_TYPE_CD` |
| `COMP_APPT_SYNONYM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `COMP_APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATION_CD` | [SCH_APPT_LOC](SCH_APPT_LOC.md) | `LOCATION_CD` |
| `OFFSET_BEG_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_END_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_FROM_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SCH_COMP_LOC](SCH_COMP_LOC.md) | `APPT_TYPE_CD` |
| [SCH_COMP_LOC](SCH_COMP_LOC.md) | `LOCATION_CD` |
| [SCH_COMP_LOC](SCH_COMP_LOC.md) | `SEQ_NBR` |

