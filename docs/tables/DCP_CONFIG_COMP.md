# DCP_CONFIG_COMP

> Contains information about the domains,sub-domains,components ,sub-components and this information is used to build a tree structure

**Description:** Configuration Component  
**Table type:** REFERENCE  
**Primary key:** `DCP_CONFIG_COMP_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_DESC` | VARCHAR(256) |  |  | description for domain/sub - domain/component |
| 2 | `COMP_DISPLAY` | VARCHAR(100) | NOT NULL |  | Name of domain/sub-domain/component that is displayed to the user |
| 3 | `COMP_IND` | DOUBLE | NOT NULL |  | Indicates whether ccnfig_setting has a standard value or not (1 - for component 0- for others) |
| 4 | `COMP_NAME` | VARCHAR(32) | NOT NULL |  | Unique Name for the domain,sub-domain or component |
| 5 | `DCP_CONFIG_COMP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DCP_CONFIG_COMP_RELTN](DCP_CONFIG_COMP_RELTN.md) | `DCP_CONFIG_COMP_ID` |
| [DCP_CONFIG_COMP_TREE](DCP_CONFIG_COMP_TREE.md) | `DCP_CONFIG_COMP_ID` |
| [DCP_CONFIG_COMP_TREE](DCP_CONFIG_COMP_TREE.md) | `PARENT_COMP_ID` |

