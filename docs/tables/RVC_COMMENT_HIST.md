# RVC_COMMENT_HIST

> Stores history for free text comments for various solution domains.

**Description:** Revenue Cycle Comment History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 6 | `COMMENT_TEXT` | LONGTEXT |  |  | The Free Text Comment. |
| 7 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The comment type is the code set value which identifies the specific type of comment for the comment row (i.e., general, delay reason, etc.) |
| 8 | `COMMENT_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Comment type class is used to categorize comments into general entity groups (i.e., person, encounter, encounterauthorization, etc.) |
| 9 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time that the comment was created. |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user responsible for creating the comment. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the comment row is related. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this comment row is related (i.e., person, encounter, authorization, etc.) |
| 13 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 14 | `RVC_COMMENT_HIST_ID` | DOUBLE | NOT NULL |  | Stores the history of free text comments for various solution domains. |
| 15 | `RVC_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a revenue cycle comment. |
| 16 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 17 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `RVC_COMMENT_ID` | [RVC_COMMENT](RVC_COMMENT.md) | `RVC_COMMENT_ID` |

