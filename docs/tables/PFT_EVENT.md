# PFT_EVENT

> ProFit's events

**Description:** Holds user defined events  
**Table type:** REFERENCE  
**Primary key:** `PFT_EVENT_ID`  
**Columns:** 25  
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
| 6 | `CURRENT_OCCURRANCE` | DOUBLE |  |  | Obsolete, No longer used. - Current Occurrance |
| 7 | `END_DT_TM` | DATETIME |  |  | End Date and Time value |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LAST_OPS_PING_DT_TM` | DATETIME |  |  | Obsolete, no longer being used. Last operations ping date time |
| 10 | `LAST_PING_STATUS_CD` | DOUBLE | NOT NULL |  | - last ping stats code |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `PFT_EVENT_DESC` | VARCHAR(250) |  |  | Description of what event will occur |
| 13 | `PFT_EVENT_DESC_KEY` | VARCHAR(250) |  |  | Description of what event will occur, formatted to aid in performance when searching. |
| 14 | `PFT_EVENT_ID` | DOUBLE | NOT NULL | PK | Unique Key |
| 15 | `PFT_EVENT_NAME` | VARCHAR(50) |  |  | Name of the event |
| 16 | `PFT_EVENT_NAME_KEY` | VARCHAR(50) |  |  | Event Name Key |
| 17 | `PFT_EVENT_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Event sub type - Claim generation, Claim Print, etc. |
| 18 | `PFT_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Event Type - automated process, business process, etc. |
| 19 | `RECURRING_IND` | DOUBLE |  |  | Flag whether this is a recurring event or not. |
| 20 | `START_DT_TM` | DATETIME |  |  | Start date / time of the event |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PFT_DATE](PFT_DATE.md) | `PFT_EVENT_ID` |
| [PFT_EVENT_PARAMS](PFT_EVENT_PARAMS.md) | `PFT_EVENT_ID` |
| [PFT_EVENT_PATTERN](PFT_EVENT_PATTERN.md) | `PFT_EVENT_ID` |
| [PFT_REPORT_INSTANCE](PFT_REPORT_INSTANCE.md) | `PFT_EVENT_ID` |

