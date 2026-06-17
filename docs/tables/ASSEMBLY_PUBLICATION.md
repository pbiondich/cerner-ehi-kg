# ASSEMBLY_PUBLICATION

> Provides a list of publications of assemblies to which t the lab system provides or subscribes..

**Description:** Assembly Publication  
**Table type:** ACTIVITY  
**Primary key:** `ASSEMBLY_PUBLICATION_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSEMBLY_PUBLICATION_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a list of publications of assemblies to which the lab system provides or subscribes. |
| 3 | `EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date from which the publication is effective. |
| 4 | `LAST_LOCK_ELAPSED_SECS` | DOUBLE | NOT NULL |  | The time duration over which the last lock of the publication lasted. |
| 5 | `LAST_PUBLISHED_DT_TM` | DATETIME |  |  | The data and time of the most recent publishing. |
| 6 | `PUBLICATION_NAME` | VARCHAR(60) | NOT NULL |  | The name of the publication |
| 7 | `PUBLISHER_NAME` | VARCHAR(60) | NOT NULL |  | Name of the Publisher |
| 8 | `PUBLISH_ANCHOR_DT_TM` | DATETIME |  |  | The anchor date and time of the publishing attempt. |
| 9 | `PUBLISH_EXPIRATION_DT_TM` | DATETIME |  |  | The expiration date and time of the publishing attempt. |
| 10 | `PUBLISH_FREQUENCY_SECS` | DOUBLE | NOT NULL |  | The frequency in seconds for the publishing interval. |
| 11 | `PUBLISH_STATUS_FLAG` | DOUBLE | NOT NULL |  | The publishing status flag. 0 - Inactive; 1 - Ready; 2 - Started; 3 - Completed |
| 12 | `SOURCE_LAB_SYSTEM_NAME` | VARCHAR(40) | NOT NULL |  | The lab system that is the source of the publication. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ASSEMBLY_PART](ASSEMBLY_PART.md) | `ASSEMBLY_PUBLICATION_ID` |
| [ASSEMBLY_PUBLICATION_VIEW](ASSEMBLY_PUBLICATION_VIEW.md) | `ASSEMBLY_PUBLICATION_ID` |
| [ASSEMBLY_SUBSCRIPTION](ASSEMBLY_SUBSCRIPTION.md) | `ASSEMBLY_PUBLICATION_ID` |

