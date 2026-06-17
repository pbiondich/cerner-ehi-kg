# MARS_NODE

> Hierarchically defines a node of an XML Schema Document.

**Description:** MARS_NODE  
**Table type:** REFERENCE  
**Primary key:** `MARS_NODE_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MARS_NODE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `MARS_REPORT_ID` | DOUBLE |  | FK→ | Report to which this node belongs. |
| 3 | `NODE_NAME` | VARCHAR(255) |  |  | Name of the schema node - ELEMENT - ATTRIBUTE - ENUMERATION etc. |
| 4 | `NODE_TEXT` | VARCHAR(255) |  |  | Text within the node. |
| 5 | `NODE_TYPE_NBR` | DOUBLE |  |  | Type of the schema node |
| 6 | `PARENT_NODE_ID` | DOUBLE |  | FK→ | Parent MARS_NODE_ID. Zero where Node is root. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_REPORT_ID` | [MARS_REPORT](MARS_REPORT.md) | `MARS_REPORT_ID` |
| `PARENT_NODE_ID` | [MARS_NODE](MARS_NODE.md) | `MARS_NODE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MARS_ATTRIBUTE](MARS_ATTRIBUTE.md) | `MARS_NODE_ID` |
| [MARS_NODE](MARS_NODE.md) | `PARENT_NODE_ID` |

