# SCH_BASE_SCHEDULE_ACTIVITY

> Contains data pertaining to a base schedule. The schedule will be built out using activities

**Description:** Schedule Base Schedules With Activities  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | The activity code (Code Set: 4014000) associated with the schedule. |
| 6 | `ACTIVITY_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the activities display scheme. |
| 7 | `BEG_OFFSET` | DOUBLE | NOT NULL |  | defines the beginning offset for the activity from the begin time of the unit schedule. |
| 8 | `BORDER_COLOR` | DOUBLE | NOT NULL |  | the numeric equilivant of the border color. |
| 9 | `BORDER_SIZE` | DOUBLE | NOT NULL |  | the numeric equilivant of the border size. |
| 10 | `BORDER_STYLE` | DOUBLE | NOT NULL |  | the numeric equilivant of the border style. |
| 11 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | a sequence-generated number to uniquely identify the specific row in the database. |
| 12 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | a long description used for documentation. |
| 13 | `DURATION` | DOUBLE | NOT NULL |  | The duration of the unit's activity slot |
| 14 | `END_OFFSET` | DOUBLE | NOT NULL |  | defines the ending offset for the activity from the begin time of the unit schedule. |
| 15 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | a 100-character string used for identification and selection. |
| 16 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-dec-2100 00:00:00.00. this field is used to maintain foreign keys to tables that contain a version_dt_tm in the primary key. |
| 17 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to other tables as defined by the parent_entity_name. Used to link a scheduled activity item to a base schedule. |
| 18 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Designates the location (table) of the parent_entity_id. |
| 19 | `PEN_SHAPE` | DOUBLE | NOT NULL |  | a ""0"" in this column will indicate a ""square"" border pen. a ""1"" in this column will represent a ""round"" border pen. |
| 20 | `SCH_BASE_SCHEDULE_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_BASE_SCHEDULE_ACTIVITY table. |
| 21 | `SEQ_NBR` | DOUBLE | NOT NULL |  | determines the order among the children of a group. |
| 22 | `SERIES_UUID` | VARCHAR(36) | NOT NULL |  | Contains the series identifier that this activity and base schedule pertain to. This will determine what rows need to be updated on a change of the base schedule. Generated from the Java UUID llibraries. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | the version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |

