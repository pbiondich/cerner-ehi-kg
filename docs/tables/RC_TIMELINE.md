# RC_TIMELINE

> Stores the information about the activities applied on a person

**Description:** Revenue cycle Timeline  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_CREATED_DT_TM` | DATETIME |  |  | The date and time the activity was added. |
| 6 | `ACTIVITY_CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person who has applied the activity. |
| 7 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This will be used to identify the type of activity. For example, statement cycle change, balance status changed, move charges, workflow, etc. |
| 8 | `APPLIED_TO_CD` | DOUBLE | NOT NULL |  | This will carry the type of entity to which this activity is associated . Example : ENCOUNTER, PERSON etc . |
| 9 | `APPLIED_TO_TXT` | VARCHAR(200) |  |  | This will contain a concatenated string with the entity details. |
| 10 | `CHILD_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The entity of the comment/activity undergone in a financial combine/uncombine |
| 11 | `CHILD_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The entity of the comment/activity undergone in a financial combine/uncombine. |
| 12 | `COMMENT_CLOB` | LONGTEXT |  |  | User entered comments which need to be displayed in the comment section. |
| 13 | `DESCRIPTION_TXT` | VARCHAR(1500) |  |  | Textual description of the activity applied. |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The idnentifier fo the entity to which the activity is applied. |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the entity of the comment/activity |
| 16 | `PRIORITY_NBR` | DOUBLE |  |  | This will be the importance level of the comment. |
| 17 | `RC_TIMELINE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_TIMELINE table. |
| 18 | `SOLUTION_CD` | DOUBLE | NOT NULL |  | This will carry solution names like Registtration, Scheduling, HIM, Care Management, CPA |
| 19 | `SOURCE_REFERENCE_IDENT` | VARCHAR(64) |  |  | The identifier for the source system from which the activity is applied. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `WORKFLOW_CATEGORY_CD` | DOUBLE |  |  | Contains the value of the workflow model type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

