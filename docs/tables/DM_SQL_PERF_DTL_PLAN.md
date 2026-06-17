# DM_SQL_PERF_DTL_PLAN

> This tables stores SQL plan information for SQL statements from the Oracle V$SQL_PLAN view. All but the 3 id columns come straight from the V$SQL_PLAN view, with some slight renaming of columns to avoid Millennium naming standard violations.

**Description:** Data Management SQL Performance Detail Plan  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_PREDICATES` | VARCHAR(4000) |  |  | The access predicates from the V$SQL_PLAN table. |
| 2 | `BYTES` | DOUBLE |  |  | The bytes column information from the V$SQL_PLAN table. |
| 3 | `CARDINALITY` | DOUBLE |  |  | The cardinality column information from the V$SQL_PLAN table. |
| 4 | `COST` | DOUBLE |  |  | The cost column information from the V$SQL_PLAN table. |
| 5 | `CPU_COST` | DOUBLE |  |  | The CPU Cost column information from the V$SQL_PLAN table. |
| 6 | `DEPTH` | DOUBLE |  |  | The depth column information from the V$SQL_PLAN table. |
| 7 | `DISTRIBUTION` | VARCHAR(20) |  |  | The distribution column information from the V$SQL_PLAN table. |
| 8 | `DM_SQL_ID` | DOUBLE | NOT NULL | FK→ | This column relates this performance detail plan row to a specific Data Management SQL Performance row. |
| 9 | `DM_SQL_PERF_DTL_ID` | DOUBLE | NOT NULL | FK→ | This column relates this performance detail plan row to a specific performance detail record. |
| 10 | `DM_SQL_PERF_DTL_PLAN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a Performance Detail Plan SQL statement. |
| 11 | `FILTER_PREDICATES` | VARCHAR(4000) |  |  | The filter predicates column information from the V$SQL_PLAN table. |
| 12 | `IO_COST` | DOUBLE |  |  | The IO Cost column information from the V$SQL_PLAN table. |
| 13 | `OBJECT_IDENT` | DOUBLE |  |  | The object_id column information from the V$SQL_PLAN table. |
| 14 | `OBJECT_NAME` | VARCHAR(64) |  |  | The object_name column information from the V$SQL_PLAN table. |
| 15 | `OBJECT_NODE` | VARCHAR(10) |  |  | The Object_Node column information from the V$SQL_PLAN table. |
| 16 | `OBJECT_OWNER` | VARCHAR(30) |  |  | The Object_Owner column information from the V$SQL_PLAN table. |
| 17 | `OPERATION` | VARCHAR(30) |  |  | The operation column information from the V$SQL_PLAN table. |
| 18 | `OPTIMIZER` | VARCHAR(20) |  |  | The optimizer column information from the V$SQL_PLAN table. |
| 19 | `OPTIONS` | VARCHAR(30) |  |  | The options column information from the V$SQL_PLAN table. |
| 20 | `OTHER` | VARCHAR(4000) |  |  | The Other column information from the V$SQL_PLAN table. |
| 21 | `OTHER_TAG` | VARCHAR(35) |  |  | The Other Tag column information from the V$SQL_PLAN table. |
| 22 | `PARENT_IDENT` | DOUBLE |  |  | The Parent_ID column information from the V$SQL_PLAN table. |
| 23 | `POSITION` | DOUBLE |  |  | The position column information from the V$SQL_PLAN table. |
| 24 | `SEARCH_COLUMNS` | DOUBLE |  |  | The Search_Columns column information from the V$SQL_PLAN table. |
| 25 | `TEMP_SPACE` | DOUBLE |  |  | The Temp_Space column information from the V$SQL_PLAN table. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 31 | `VSQL_PLAN_IDENT` | DOUBLE | NOT NULL |  | The VSQL_PLAN_ID column information from the V$SQL_PLAN table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_SQL_ID` | [DM_SQL_PERFORMANCE](DM_SQL_PERFORMANCE.md) | `DM_SQL_ID` |
| `DM_SQL_PERF_DTL_ID` | [DM_SQL_PERF_DTL](DM_SQL_PERF_DTL.md) | `DM_SQL_PERF_DTL_ID` |

