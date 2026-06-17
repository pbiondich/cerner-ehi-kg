# SCH_ORDER_APPT

> Scheduling Order Appointment

**Description:** Scheduling Order Appointment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling appointment type. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the order catalog entry. |
| 9 | `CHILD_APPT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the child appointment type. |
| 10 | `DEL_APPT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the delete appointment action. |
| 11 | `DEL_APPT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the delete appointment action. |
| 12 | `DISPLAY_SEQ_NBR` | DOUBLE | NOT NULL |  | The display order of the valid appointment types within the order tool. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EVENT_CONCURRENT_IND` | DOUBLE | NOT NULL |  | Determintes if the order is concurrent to the entire event. |
| 15 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 16 | `PROC_SPEC_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the procedure specific status. This field is used to determine if the order is required for the appointment type. |
| 17 | `PROC_SPEC_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the procedure specific status. |
| 18 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 19 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CATALOG_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CHILD_APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DEL_APPT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PROC_SPEC_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

