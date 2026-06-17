# SCH_EVENT_ROLE

> Store the resource list modification for an event.

**Description:** Scheduling Event Role  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EVENT_MOD_ID` | DOUBLE | NOT NULL |  | The unique identifier for the event's resource list modification. |
| 9 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the list role. |
| 10 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 11 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the resource. A resource is an item of limited availability. |
| 12 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. |
| 13 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 14 | `SELECTED_IND` | DOUBLE | NOT NULL |  | Determines if the object is (by default) selected or not. |
| 15 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the slot type. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |

