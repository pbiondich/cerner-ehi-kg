# PCA_SOURCE

> Defines who provided the content for a Quality Topic.

**Description:** Power Chart Analytics Source  
**Table type:** REFERENCE  
**Primary key:** `PCA_SOURCE_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFINED_BY_FLAG` | DOUBLE | NOT NULL |  | Identifies the group that provided this Quality Source. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Comment which provides additional meaning or context to the Source. |
| 3 | `DISPLAY_TXT` | VARCHAR(60) | NOT NULL |  | The textual display for this Source. |
| 4 | `PCA_SOURCE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_SOURCE table. |
| 5 | `SOURCE_CD` | DOUBLE | NOT NULL |  | The CODE VALUE record which identifies the source. This field will only be used for base Sources shipped. Will contain zeros for client added rows. |
| 6 | `SOURCE_URL_TXT` | VARCHAR(255) |  |  | A URL address associated with the Source. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PCA_OUTCOME](PCA_OUTCOME.md) | `PCA_SOURCE_ID` |
| [PCA_QUALITY_MEASURE](PCA_QUALITY_MEASURE.md) | `PCA_SOURCE_ID` |
| [PCA_QUALITY_TOPIC](PCA_QUALITY_TOPIC.md) | `PCA_SOURCE_ID` |

