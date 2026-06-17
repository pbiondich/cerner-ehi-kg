# OPS2_DEPENDENCY_RELTN

> The operations dependency table stores the information about a dependency that exists between:- Jobs and other jobs not in the same Job Group- Job Groups and other Job Groups- Job Groups and Jobs that are not in the same Job Group- Job Groups and Steps that are not in the same Job Group- Jobs and Steps that are not in the same Job- Steps and other Steps that are not in the same Job

**Description:** Operations Dependency Relation  
**Table type:** REFERENCE  
**Primary key:** `OPS2_DEPENDENCY_RELTN_ID`  
**Columns:** 27  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATE_RECUR_INTERVAL_NBR` | DOUBLE | NOT NULL |  | The interval between each occurrence of the dependency. The unit of measurement for how this value is interpreted, flexes based on the schedule type. For example, this value will be an interval of days for daily dependencies. |
| 4 | `DEP_CRITERIA_FLAG` | DOUBLE | NOT NULL |  | The criteria that must be satisfied by the 'trigger item' of the dependency, in order for the 'dependent item' to be automatically executed. The dependency may be configured to execute on errors only (DEP_CRITERIA_FLAG = 0), on success only (DEP_CRITERIA_FLAG = 1), or both (DEP_CRITERIA_FLAG = 2). |
| 5 | `DEP_JOB_GROUP_START_DT_TM` | DATETIME |  |  | The start time for the specific occurrence of the job group representing the 'dependent item' for which this dependency applies. |
| 6 | `DEP_JOB_START_DT_TM` | DATETIME |  |  | The start time for the specific occurrence of the job or job within a job group representing the 'dependent item' for which this dependency applies. |
| 7 | `DEP_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the dependent object for the triggering object on this row. |
| 8 | `DEP_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the dependent table that contains the object that is the dependent object. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXTERNAL_USERNAME` | VARCHAR(100) |  |  | The name of the non-Millennium (e.g. Olympus) user that modified the record. |
| 11 | `OPS2_DAY_OF_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_DAY_OF_MONTH. Indicates which days of the month this dependency applies. |
| 12 | `OPS2_DAY_OF_WEEK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_DAY_OF_WEEK. Indicates which days of the week this dependency applies. |
| 13 | `OPS2_DEPENDENCY_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the OPS2_DEPENDENCY_RELTN table. |
| 14 | `OPS2_MONTH_OF_YEAR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_MONTH_OF_YEAR. Indicates which months of the year this dependency applies. |
| 15 | `OPS2_WEEK_OF_MONTH_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS2_WEEK_OF_MONTH. Indicates which weeks of the month this dependency applies. |
| 16 | `ORIG_OPS2_DEPENDENCY_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the Dependency relationships. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 17 | `SAME_DAY_IND` | DOUBLE | NOT NULL |  | Indicates if the 'dependent item' of the dependency will execute on the same day as the 'trigger item' (SAME_DAY_IND = 1) or the next day (SAME_DAY_IND = 0). |
| 18 | `SKIP_IF_FAILED_IND` | DOUBLE | NOT NULL |  | Indicates if the 'dependent item' of the dependency should be automatically skipped if the dependency criteria (i.e. DEP_CRITERIA_FLAG) is not satisfied (SKIP_IF_FAILED_IND = 1), or wait for a user to resolve the situation (SKIP_IF_FAILED_IND = 0). |
| 19 | `TRIGGER_JOB_GROUP_START_DT_TM` | DATETIME |  |  | The start time for the specific occurrence of the job group representing the 'trigger item' for which this dependency applies. |
| 20 | `TRIGGER_JOB_START_DT_TM` | DATETIME |  |  | The start time for the specific occurrence of the job or job within a job group representing the 'trigger item' for which this dependency applies. |
| 21 | `TRIGGER_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the trigger item for the dependent object on this row. |
| 22 | `TRIGGER_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that contains the object that is the trigger item. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS2_DAY_OF_MONTH_ID` | [OPS2_DAY_OF_MONTH](OPS2_DAY_OF_MONTH.md) | `OPS2_DAY_OF_MONTH_ID` |
| `OPS2_DAY_OF_WEEK_ID` | [OPS2_DAY_OF_WEEK](OPS2_DAY_OF_WEEK.md) | `OPS2_DAY_OF_WEEK_ID` |
| `OPS2_MONTH_OF_YEAR_ID` | [OPS2_MONTH_OF_YEAR](OPS2_MONTH_OF_YEAR.md) | `OPS2_MONTH_OF_YEAR_ID` |
| `OPS2_WEEK_OF_MONTH_ID` | [OPS2_WEEK_OF_MONTH](OPS2_WEEK_OF_MONTH.md) | `OPS2_WEEK_OF_MONTH_ID` |
| `ORIG_OPS2_DEPENDENCY_RELTN_ID` | [OPS2_DEPENDENCY_RELTN](OPS2_DEPENDENCY_RELTN.md) | `OPS2_DEPENDENCY_RELTN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS2_DEPENDENCY_RELTN](OPS2_DEPENDENCY_RELTN.md) | `ORIG_OPS2_DEPENDENCY_RELTN_ID` |
| [OPS2_SCHED_DEPENDENCY_R](OPS2_SCHED_DEPENDENCY_R.md) | `OPS2_DEPENDENCY_RELTN_ID` |

