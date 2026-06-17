# AOAV_EVENT

> Events such as clinical events pertaining to AOAV persons

**Description:** AOAV_EVENT  
**Table type:** ACTIVITY  
**Primary key:** `AOAV_EVENT_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value number that identifies the component for this event |
| 6 | `AOAV_EVENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `CALCULATED_FLAG` | DOUBLE | NOT NULL |  | The calculated flag giving the state of the event. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier of the encounter |
| 9 | `ERROR_STATUS_FLAG` | DOUBLE | NOT NULL |  | Error status flag (0 = no error, 1 = in error) |
| 10 | `EVENT_DT_TM` | DATETIME |  |  | The date/time the event was documented. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique ID of the parent entity. For e.g. clinical_event_id if parent is a clinical event |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Type of parent entity, e.g. CLINICAL_EVENT |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This field is no longer used - DBARCHDTL-23349 |
| 14 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | Code value number of the unit of measure of the event. |
| 15 | `RESULT_VALUE` | DOUBLE |  |  | The event result value. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AOAV_EVENT_CHILD](AOAV_EVENT_CHILD.md) | `AOAV_EVENT_ID` |
| [AOAV_OUTCOME_COMP_EVENT_R](AOAV_OUTCOME_COMP_EVENT_R.md) | `AOAV_EVENT_ID` |

