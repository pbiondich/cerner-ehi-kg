# EKS_DLG

> Reference data for the installed Insights with versions and active dates.

**Description:** EKS DLG  
**Table type:** REFERENCE  
**Primary key:** `DLG_NAME`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DLG_NAME` | VARCHAR(255) | NOT NULL | PK | Unique identifier for an Insight. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PROGRAM_NAME` | CHAR(30) |  |  | File name for the ActiveX control which executes the client portion of and Insight. |
| 6 | `TITLE` | VARCHAR(255) |  |  | Full title of an Insight. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_MAJOR` | DOUBLE |  |  | Major version identifier for an Insight |
| 13 | `VERSION_MINOR` | DOUBLE |  |  | Minor version identifier for an Insight |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EKS_DLG_EVENT](EKS_DLG_EVENT.md) | `DLG_NAME` |

