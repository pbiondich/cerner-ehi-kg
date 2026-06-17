# SCH_LIST_RES

> Scheduling List Resource

**Description:** Scheduling List Resource  
**Table type:** REFERENCE  
**Primary key:** `LIST_ROLE_ID`, `RESOURCE_CD`  
**Columns:** 23  
**Referenced by:** 4 columns

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
| 7 | `DISPLAY_SEQ` | DOUBLE |  |  | The display order of the object within the collection. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | PK FK→ | The unique identifier for the scheduling role. |
| 10 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 11 | `PREF_IND` | DOUBLE |  |  | Determines if the resource had a preferred resource list. |
| 12 | `RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The identifier for the resource. A resource is an item of limited availability. |
| 13 | `RES_SCH_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the schedulable status of the resource (schedulable, overflow). |
| 14 | `RES_SCH_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the resource schedulable code. |
| 15 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 16 | `SEARCH_SEQ` | DOUBLE |  |  | Determines the manual search order for the resources. |
| 17 | `SELECTED_IND` | DOUBLE |  |  | Determines if the object is (by default) selected or not. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RES_SCH_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [SCH_LIST_LOC](SCH_LIST_LOC.md) | `LIST_ROLE_ID` |
| [SCH_LIST_LOC](SCH_LIST_LOC.md) | `RESOURCE_CD` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `LIST_ROLE_ID` |
| [SCH_LIST_SLOT](SCH_LIST_SLOT.md) | `RESOURCE_CD` |

