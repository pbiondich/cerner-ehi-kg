# DRC_ROUTE_GROUP_VER

> version table for DRC_ROUTE_GROUP table.

**Description:** DRC_ROUTE_GROUP_VER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHILD_ROUTE_CD` | DOUBLE |  | FK→ | code_value to identify the child route. |
| 3 | `DRC_ROUTE_GROUP_ID` | DOUBLE |  |  | ***Obsolete Column***. Made obsolete since not needed to refer back to parent row and can not maintain a foreign key on it during deletes of the parent row in table DRC_ROUTE_GROUP. |
| 4 | `DRC_ROUTE_GROUP_VER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `PARENT_ROUTE_CD` | DOUBLE |  | FK→ | code_value to identify the parent route. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `VER_SEQ` | DOUBLE |  |  | The sequence of the version |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ROUTE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PARENT_ROUTE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

