# DM_TEXT_FIND_QUERY

> This table will store meta-data about the queries to run in the new Text Search tool owned by DM

**Description:** Datbase Management Text Find Query  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to DM_TEXT_FIND_CAT table |
| 3 | `DM_TEXT_FIND_QUERY_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `DRIVER_COL_NAME` | VARCHAR(30) |  |  | The driver column necessary to construct the query joins |
| 5 | `JOIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | **OBSOLETE - THIS COLUMN MOVED TO TABLE DM_TEXT_FIND_DTL_QUERY_R** The flag to indicate how join is performed to get data |
| 6 | `QUERY_COL_DEFAULT_WEIGHT` | DOUBLE | NOT NULL |  | The default weight to assign to this QUERY_GROUP_NAME and QUERY_COLUMN combination. |
| 7 | `QUERY_COL_NAME` | VARCHAR(30) |  |  | The column name to query on in the TEXT |
| 8 | `QUERY_GROUP_NAME` | VARCHAR(40) |  |  | A group name used to associated similar queries to each other. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALUE_DEFAULT_WEIGHT` | DOUBLE | NOT NULL |  | The default weight to assign to this QUERY_GROUP_NAME and QUERY_VALUE combination. |
| 15 | `WHERE_COL_TEXT` | VARCHAR(1000) |  |  | The where clause used to find data values to query upon |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_CAT_ID` | [DM_TEXT_FIND_CAT](DM_TEXT_FIND_CAT.md) | `DM_TEXT_FIND_CAT_ID` |

