# DCP_PL_QUERY_TEMPLATE

> Defines a template query that can be used by users to build a query based patient list.

**Description:** Defines a template query that can be used to build a query based patient list.  
**Table type:** REFERENCE  
**Primary key:** `TEMPLATE_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `QUERY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of query this template is for. |
| 2 | `TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the template. |
| 3 | `TEMPLATE_NAME` | VARCHAR(50) | NOT NULL |  | The name of the template. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DCP_PL_QUERY_LIST](DCP_PL_QUERY_LIST.md) | `TEMPLATE_ID` |
| [DCP_PL_QUERY_TEMP_ACCESS](DCP_PL_QUERY_TEMP_ACCESS.md) | `TEMPLATE_ID` |
| [DCP_PL_QUERY_VALUE](DCP_PL_QUERY_VALUE.md) | `TEMPLATE_ID` |

