# LH_TABLE_RELTN

> This table is used to store the table relationships used in rules for measures of Lighthouse topics.

**Description:** LH_TABLE_RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 2 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 3 | `JOIN_TXT` | VARCHAR(255) |  |  | Details the join between lh_table_id and related_lh_table_id. This text will be placed in the WHERE clause of the query. |
| 4 | `LH_TABLE_ID` | DOUBLE | NOT NULL | FK→ | A table involved in a query for a Measure's rule Foreign Key to LH_TABLE |
| 5 | `LH_TABLE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table relationship |
| 6 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was loaded into the table. |
| 7 | `RELATED_LH_TABLE_ID` | DOUBLE | NOT NULL | FK→ | A table being joined to lh_table_id Foreign Key to LH_TABLE |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 11 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_TABLE](LH_TABLE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_TABLE](LH_TABLE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_TABLE_ID` | [LH_TABLE](LH_TABLE.md) | `LH_TABLE_ID` |
| `RELATED_LH_TABLE_ID` | [LH_TABLE](LH_TABLE.md) | `LH_TABLE_ID` |

