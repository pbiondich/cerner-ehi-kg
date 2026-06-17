# DM_PLAN

> Holds the oracle plans for all request objects

**Description:** DM PLAN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ID` | DOUBLE | NOT NULL |  | Identification number for this step in the execution plan |
| 2 | `OBJECT_INSTANCE` | DOUBLE |  |  | Numbered position of the object name in the original SQL statement |
| 3 | `OBJECT_NAME` | VARCHAR(30) |  |  | Name of the object |
| 4 | `OBJECT_NODE` | VARCHAR(128) |  |  | Name of the database link used to reference the object |
| 5 | `OBJECT_OWNER` | VARCHAR(30) |  |  | Owner of the object |
| 6 | `OBJECT_TYPE` | VARCHAR(30) |  |  | Descriptive modifier that further describes the type of the object |
| 7 | `OPERATION` | VARCHAR(30) |  |  | Name of the operation performed at this step |
| 8 | `OPTIONS` | VARCHAR(30) |  |  | Options used for the operation performed at this step |
| 9 | `PARENT_ID` | DOUBLE |  |  | ID of the next step that operates on the results of this step |
| 10 | `POSITION` | DOUBLE |  |  | Order of processing for steps with the same parent ID. For cost-based optimization, the value in the first row of the plan is the statement's execution cost. For rule-based optimization, the value is null in the first row |
| 11 | `REMARKS` | VARCHAR(80) |  |  | Place for comments that can be added to the steps of the execution plan |
| 12 | `SCHEMA_DATE` | DATETIME | NOT NULL |  | Rev date from DM_SCHEMA_VERSION |
| 13 | `SCRIPT_NAME` | VARCHAR(80) | NOT NULL |  | The script name of the object that the oracle plan was generated for |
| 14 | `SEARCH_COLUMNS` | DOUBLE |  |  | Not currently used |
| 15 | `SQL_STMT_ID` | DOUBLE | NOT NULL |  | unique number generated in order to make the row unique, holds the sequence of steps of the SQL query |
| 16 | `STATEMENT_ID` | VARCHAR(100) | NOT NULL |  | Optional statement identifier specified in the EXPLAIN PLAN statement |
| 17 | `STMT` | LONGTEXT |  |  | Contains the entire SQL query text that is sent to ORACLE |
| 18 | `TIMESTAMP` | DATETIME |  |  | Date and time that the EXPLAIN PLAN statement was used |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

