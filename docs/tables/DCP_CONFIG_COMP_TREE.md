# DCP_CONFIG_COMP_TREE

> This table contains data to form a tree structure using configuration components from the dcp_config_comp table

**Description:** Configuration Component Tree Structure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_SEQUENCE` | DOUBLE |  |  | describes the order in which the sibling domain/sub-domain/component/sub-component are grouped under the parent |
| 2 | `DCP_CONFIG_COMP_ID` | DOUBLE | NOT NULL | FK→ | Identifier for a Component in config_components table |
| 3 | `DCP_CONFIG_COMP_TREE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PARENT_COMP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the parent of each domain/sub-domain/component(points to another row in the same table) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_CONFIG_COMP_ID` | [DCP_CONFIG_COMP](DCP_CONFIG_COMP.md) | `DCP_CONFIG_COMP_ID` |
| `PARENT_COMP_ID` | [DCP_CONFIG_COMP](DCP_CONFIG_COMP.md) | `DCP_CONFIG_COMP_ID` |

