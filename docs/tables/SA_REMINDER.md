# SA_REMINDER

> Contains information about adhoc and pre-built reminders in the anesthesia record.

**Description:** SA REMINDER  
**Table type:** ACTIVITY  
**Primary key:** `SA_REMINDER_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | The date and time the reminder was completed |
| 6 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indication that the reminder has been completed |
| 7 | `COMPLETE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The clinical person who completed the reminder |
| 8 | `PARENT_ENTITY_ID` | DOUBLE |  |  | the row PK value from the table identified in field PARENT ENTITY NAME which contains the item this sequence is defining |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | the parent table that contains the item this sequence is defining. the PK value of the parent table row id in PARENT_ENTITY_ID ; |
| 10 | `PREV_REMINDER_ID` | DOUBLE | NOT NULL | FK→ | The previous reminder in a set of reminders |
| 11 | `REMINDER_ALERT_DT_TM` | DATETIME |  |  | The date and time the reminder alert triggered |
| 12 | `REMINDER_DUE_DT_TM` | DATETIME |  |  | The date and time the reminder is due |
| 13 | `REMINDER_TEXT` | VARCHAR(250) | NOT NULL |  | Text presented when the reminder triggers |
| 14 | `REPEAT_ALERT_MINUTES_VAL` | DOUBLE |  |  | The default alert time to use for repeat reminders. null value means subsequent repeat reminders will not have an alert. |
| 15 | `REPEAT_MINUTES_VAL` | DOUBLE | NOT NULL |  | The interval in minutes which represents the offset for the new due date/time when this reminder is completed. |
| 16 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | Anesthesia record the reminder is associated with. |
| 17 | `SA_REMINDER_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPLETE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PREV_REMINDER_ID` | [SA_REMINDER](SA_REMINDER.md) | `SA_REMINDER_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_REMINDER](SA_REMINDER.md) | `PREV_REMINDER_ID` |

