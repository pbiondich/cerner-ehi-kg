# SCH_EVENT_RECUR_ROLE

> Table to store the information about how a future instance of a recurring appointment should be booked in role level.

**Description:** Scheduling Event Recur Role  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_DT_TM` | DATETIME | NOT NULL |  | The begin Date and time value of the resource or the person for the resource list role or order role. |
| 2 | `CLEANUP_DURATION` | DOUBLE |  |  | The duration for patient recovery or resource (such as room) clean up. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the row of the encounter associated with this table. |
| 4 | `END_DT_TM` | DATETIME | NOT NULL |  | The end date and time value of the resource or the person for the resource list role or order role. |
| 5 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the associated list role. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. If the role is a patient role, the person_id is patient's person_id. If the role is not a patient role, it will be a scheduling resource. There are different type of resources. If the resource is a personnel resource, the person_id will be provider's person_id. If the resource is not a personnel resource, then the person_id will be 0. |
| 7 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the associated resource. A resource is an item of limited availability. |
| 8 | `ROLE_SEQ` | DOUBLE | NOT NULL |  | The order of the role on the resource list. |
| 9 | `SCH_EVENT_RECUR_LIST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of associated row from the sch_event_recur_list table. |
| 10 | `SCH_EVENT_RECUR_ROLE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_ROLE table. |
| 11 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The generic term used to denote a physical place in the Health Care Organization. |
| 12 | `SETUP_DURATION` | DOUBLE |  |  | The duration for patient arrival or resource (such as room) set up. |
| 13 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the slot type that is associated to the appointment. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |
| `SCH_EVENT_RECUR_LIST_ID` | [SCH_EVENT_RECUR_LIST](SCH_EVENT_RECUR_LIST.md) | `SCH_EVENT_RECUR_LIST_ID` |
| `SERVICE_RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |

