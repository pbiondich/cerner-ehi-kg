# SCH_APPT_LOC

> Defines the valid location for an appointment type.

**Description:** Appointment Type Location  
**Table type:** REFERENCE  
**Primary key:** `APPT_TYPE_CD`, `LOCATION_CD`  
**Columns:** 19  
**Referenced by:** 4 columns

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
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `GRP_RES_LIST_ID` | DOUBLE | NOT NULL | FK→ | Resource List to be used when creating a group session |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | PK FK→ | The field identifies the current permanent location of the patient. |
| 11 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 12 | `RES_LIST_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the scheduling resource list. |
| 13 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The ID of the row from the SCH_FLEX_STRING table taht is associated to the scheduling appointment type location. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `GRP_RES_LIST_ID` | [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `RES_LIST_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RES_LIST_ID` | [SCH_RESOURCE_LIST](SCH_RESOURCE_LIST.md) | `RES_LIST_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SCH_APPT_COMP](SCH_APPT_COMP.md) | `APPT_TYPE_CD` |
| [SCH_APPT_COMP](SCH_APPT_COMP.md) | `LOCATION_CD` |
| [SCH_APPT_INTER](SCH_APPT_INTER.md) | `APPT_TYPE_CD` |
| [SCH_APPT_INTER](SCH_APPT_INTER.md) | `LOCATION_CD` |

