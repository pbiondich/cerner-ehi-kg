# CNFG_MGR_GRP

> Defines the list of groups containing a set of sub groups.

**Description:** Configuration Manager groups  
**Table type:** REFERENCE  
**Primary key:** `CNFG_MGR_GRP_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNFG_MGR_GRP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Defines the order sequence of the group. |
| 3 | `GRP_KEY_TXT` | VARCHAR(100) |  |  | Unique string key to identify each group. |
| 4 | `PARENT_GRP_ID` | DOUBLE | NOT NULL | FK→ | Parent group ID of the group. |
| 5 | `TITLE_TXT` | VARCHAR(100) | NOT NULL |  | Name of the group. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_GRP_ID` | [CNFG_MGR_GRP](CNFG_MGR_GRP.md) | `CNFG_MGR_GRP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNFG_MGR_GRP](CNFG_MGR_GRP.md) | `PARENT_GRP_ID` |
| [CNFG_MGR_TOOL](CNFG_MGR_TOOL.md) | `CNFG_MGR_GRP_ID` |

