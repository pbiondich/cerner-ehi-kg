# LH_TABLE

> This table is used to store the tables and aliases that are used in rules for measures of Lighthouse topics.

**Description:** LH_TABLE  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_TABLE_ID`  
**Columns:** 10  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS` | VARCHAR(50) |  |  | An alias for the table |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 4 | `LH_TABLE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the table |
| 5 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was loaded into the table. |
| 6 | `TABLE_NAME` | VARCHAR(50) |  |  | Name of the table |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 10 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [LH_TABLE_RELTN](LH_TABLE_RELTN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_TABLE_RELTN](LH_TABLE_RELTN.md) | `LH_TABLE_ID` |
| [LH_TABLE_RELTN](LH_TABLE_RELTN.md) | `RELATED_LH_TABLE_ID` |

