# PERSON_PRSNL_ACTIVITY

> This table records info about prsnl viewing results or similar activities. Both PowerChart and ProVide track activity between users and patients.

**Description:** This table records info about prsnl viewing results or similar activities.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPUTER_NAME` | VARCHAR(100) |  |  | This is an optional field that could be filled out when doing chart access or view access logging to track which computer was being used at the time. |
| 6 | `COMP_CAPTION` | VARCHAR(100) |  |  | This is an optional field that could be filled out to track component access via PowerChart/ProVide. It is not used at this time. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 8 | `PPA_CNT` | DOUBLE |  |  | Contains the number of times this row has been updated. |
| 9 | `PPA_COMMENT` | VARCHAR(256) |  |  | This is an option field that could be used with logging to store additional information about why the access had taken place. |
| 10 | `PPA_FIRST_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time that this row was originally stamped with. |
| 11 | `PPA_FIRST_TZ` | DOUBLE |  |  | Contains the time zone that this row was originally stamped with. |
| 12 | `PPA_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 13 | `PPA_LAST_DT_TM` | DATETIME |  |  | The last time that this row got 'stamped' for activity. |
| 14 | `PPA_LAST_TZ` | DOUBLE |  |  | Contains the time zone for the last time that this row got "stamped" for activity. |
| 15 | `PPA_TYPE_CD` | DOUBLE | NOT NULL |  | The code value representing the person prsnl activity type, i.e. RESULTS REVIEW |
| 16 | `PPR_CD` | DOUBLE |  |  | This is an optional field that will be filled out for chart access and view access logging with the ppr_cd that was active at the time of the access. |
| 17 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the person_id for the user or provider that the row is written for. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VIEW_CAPTION` | VARCHAR(100) |  |  | This is an optional field that will be used with view access logging to contain the caption of the view that was accessed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

