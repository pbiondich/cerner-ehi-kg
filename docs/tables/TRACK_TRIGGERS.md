# TRACK_TRIGGERS

> This table has all the trigger information

**Description:** TRACK TRIGGERS  
**Table type:** REFERENCE  
**Primary key:** `TRACK_TRIGGER_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE` | VARCHAR(50) | NOT NULL |  | This column stores what action needs to be performedColumn |
| 2 | `ACTION_VALUE` | VARCHAR(50) | NOT NULL |  | This stores what action valuesColumn |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | This stores the pm conversation identifier with the firstnet taskColumn |
| 5 | `FREQUENCY` | VARCHAR(5) |  |  | This stores whether the trigger should happen once or alwaysColumn |
| 6 | `PRIORITY_SEQUENCE` | DOUBLE |  |  | priority sequence |
| 7 | `REGISTRATION_KEY_TXT` | VARCHAR(255) | NOT NULL |  | this stores the registration key |
| 8 | `STATUS` | VARCHAR(50) |  |  | This is used for event statuses.Column |
| 9 | `TRACK_GROUP` | DOUBLE | NOT NULL |  | This stores the tracking_groupColumn |
| 10 | `TRACK_TRIGGER_ID` | DOUBLE | NOT NULL | PK | auto generated key for the tableColumn |
| 11 | `TRIGGER_KEY` | VARCHAR(200) | NOT NULL |  | this stores the trigger key from the conversationColumn |
| 12 | `TRIGGER_VALUE` | VARCHAR(50) | NOT NULL |  | this stores the trigger value.Column |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_TRIGGER_ACTIVITY](TRACK_TRIGGER_ACTIVITY.md) | `TRACK_TRIGGER_ID` |

