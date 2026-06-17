# HEALTH_PLAN_INFO

> Table used to store generic Health Plan Information.

**Description:** Health Plan Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARTABLE_IND` | DOUBLE |  |  | Determines whether this information can be charted. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 10 | `HEALTH_PLAN_INFO_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the health plan information table. It is an internal system assigned number. |
| 11 | `HP_INFO_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Health Plan Information Sub Type Code identifies the category if additional information contained in the row. (For Example: Number of Children, Clerical Contact, etc.) |
| 12 | `HP_INFO_TYPE_CD` | DOUBLE | NOT NULL |  | Health Plan Information Type Code identifies the type of the information. (For Example: Comment, General Announcement, etc.) |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from LONG_TEXT table. Ties free text comments to a health plan information row. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALUE_DT_TM` | DATETIME |  |  | A Date and Time value representing the information in the health plan information row. |
| 20 | `VALUE_NUMERIC` | DOUBLE |  |  | A numeric value representing the information in the health plan information row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

