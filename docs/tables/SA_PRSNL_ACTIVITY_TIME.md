# SA_PRSNL_ACTIVITY_TIME

> Child of PRSNL_ACTIVITY (which Contains records that document prsnl associated to an anesthesia record). Based on the # of prsnl involved in a case, and how they are tracked.

**Description:** SA Personel Activity Time  
**Table type:** ACTIVITY  
**Primary key:** `SA_PRSNL_ACTIVITY_TIME_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `END_DT_TM` | DATETIME |  |  | End Date and Time |
| 6 | `PREV_PRSNL_ACTIVITY_TIME_ID` | DOUBLE | NOT NULL | FK→ | Parent row ID if this is a child in a recursive relationship within the table. |
| 7 | `PULLED_TO_SURGERY_IND` | DOUBLE | NOT NULL |  | Indicates whether the data is pulled to surgery documentation |
| 8 | `SA_PRSNL_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | ID of row in Parent Table |
| 9 | `SA_PRSNL_ACTIVITY_TIME_ID` | DOUBLE | NOT NULL | PK | Primary Key field for this table. |
| 10 | `SIGN_DT_TM` | DATETIME |  |  | Stores the date time stamp of the signature |
| 11 | `START_DT_TM` | DATETIME | NOT NULL |  | The start date and time |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_PRSNL_ACTIVITY_TIME_ID` | [SA_PRSNL_ACTIVITY_TIME](SA_PRSNL_ACTIVITY_TIME.md) | `SA_PRSNL_ACTIVITY_TIME_ID` |
| `SA_PRSNL_ACTIVITY_ID` | [SA_PRSNL_ACTIVITY](SA_PRSNL_ACTIVITY.md) | `SA_PRSNL_ACTIVITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_PRSNL_ACTIVITY_TIME](SA_PRSNL_ACTIVITY_TIME.md) | `PREV_PRSNL_ACTIVITY_TIME_ID` |

