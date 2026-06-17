# CNFG_MGR_TOOL

> Provides information about a tool and its parent group in Configuration Manager

**Description:** Configuration Manager tool  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNFG_MGR_GRP_ID` | DOUBLE | NOT NULL | FK→ | ID of parent group |
| 3 | `CNFG_MGR_TOOL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Defines the order of the tools for a tool |
| 5 | `HELP_TXT` | VARCHAR(500) | NOT NULL |  | Help Text - Describes what tool does. |
| 6 | `REPORT_NAME` | VARCHAR(100) | NOT NULL |  | Name of the script to call when opening the tool. |
| 7 | `REPORT_PARAM` | VARCHAR(255) | NOT NULL |  | Describes what parameters to pass into the script when opening a tool. |
| 8 | `TITLE_TXT` | VARCHAR(100) | NOT NULL |  | Unique value which is the NAME of the Tool |
| 9 | `TOOL_KEY_TXT` | VARCHAR(100) | NOT NULL |  | Unique string key to identify each tool. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNFG_MGR_GRP_ID` | [CNFG_MGR_GRP](CNFG_MGR_GRP.md) | `CNFG_MGR_GRP_ID` |

