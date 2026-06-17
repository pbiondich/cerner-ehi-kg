# DCP_PL_QUERY_PARAMETER

> Defines the parameters available for query types.

**Description:** DCP PL QUERY PARAMETER  
**Table type:** REFERENCE  
**Primary key:** `PARAMETER_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MULTIPLICITY_IND` | DOUBLE |  |  | Indicates whether the parameter supports multiple values. |
| 2 | `PARAMETER_DESC` | VARCHAR(255) | NOT NULL |  | Textual description and instructions for the parameter. |
| 3 | `PARAMETER_ID` | DOUBLE | NOT NULL | PK | Unique identifier for parameter |
| 4 | `PARAMETER_NAME` | VARCHAR(50) | NOT NULL |  | The name of the parameter |
| 5 | `PARAMETER_SEQ` | DOUBLE | NOT NULL |  | The sequence of the parameter for the specified query type. |
| 6 | `PARAMETER_TYPE_CD` | DOUBLE | NOT NULL |  | They type of parameter. |
| 7 | `QUERY_TYPE_CD` | DOUBLE | NOT NULL |  | They type of query that the parameter is defined for. |
| 8 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether the parameter requires a value to be specified. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DCP_PL_QUERY_VALUE](DCP_PL_QUERY_VALUE.md) | `PARAMETER_ID` |

