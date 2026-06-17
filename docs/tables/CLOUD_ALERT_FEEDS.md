# CLOUD_ALERT_FEEDS

> Tracks the feeds that Millennium is reading for the cloud.

**Description:** Cloud Alert Feeds  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLOUD_ALERT_FEEDS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CLOUD_ALERT_FEEDS table. |
| 2 | `LAST_READ_ENTRY_IDENT` | VARCHAR(255) |  |  | The identifier associated with the last read entry from this feed. A null indicates that no entry has ever ben read from this feed. |
| 3 | `LAST_READ_SYSTEM_DT_TM` | DATETIME |  |  | The current time of the system when this feed was last read. |
| 4 | `LAST_UPDATED_DT_TM_MS_NBR` | DOUBLE |  |  | The last time this feed was updated. Represented as epoch time. Null indicates that it has never been successfully read. NOTE: this time is pulled from the feed and is not intended to be current time relative to the local box. |
| 5 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 6 | `SERVER_DT_TM_MS_NBR` | DOUBLE |  |  | The current time reported by the server the last time the feed was read. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

