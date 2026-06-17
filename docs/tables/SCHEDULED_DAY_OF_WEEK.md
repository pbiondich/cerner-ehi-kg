# SCHEDULED_DAY_OF_WEEK

> Scheduled day of week

**Description:** Days of weeks for frequencies  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Used for flexing frequencies by department/activity. Default is activity_type_cd of 0, A given frequency will have 1 or more associated activity type codes it is valid for, each schedule will be specific to 1 activity_type |
| 2 | `DAY_OF_WEEK` | DOUBLE | NOT NULL |  | The day of the week that is attached to the frequency schedule. (1 = Sunday) |
| 3 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Each instance for an ad hoc frequency will have an effective date for that instance. |
| 4 | `FACILITY_CD` | DOUBLE | NOT NULL |  | This column is used for flexing schedules by facility. |
| 5 | `FREQUENCY_CD` | DOUBLE | NOT NULL |  | Primary key. |
| 6 | `FREQ_QUALIFIER` | DOUBLE | NOT NULL |  | Primary KeyDefines the domain of ordering attributes which define the schedule for a specific order. |
| 7 | `INSTANCE` | DOUBLE | NOT NULL |  | Each time an ad hoc frequency is modified a new instance is generated and stored as an order deta |
| 8 | `PARENT_ENTITY` | CHAR(32) |  |  | Parent Entity name |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity ID for merge |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

