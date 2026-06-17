# DCP_PL_QUERY_VALUE

> "Defines the value of parameters in created query based patient list."

**Description:** DCP PL QUERY VALUE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for parameter |
| 2 | `PARAMETER_SEQ` | DOUBLE | NOT NULL |  | Sequence which identifies for which parameter the value is defined for. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the parent entity. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the parent entity table |
| 5 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of patient list.Column |
| 6 | `QUERY_VALUE_ID` | DOUBLE | NOT NULL |  | Unique identifier for value |
| 7 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Identifier for query template for which this value is defined. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_DT` | DATETIME |  |  | The date value. |
| 14 | `VALUE_NAME` | VARCHAR(25) | NOT NULL |  | The name of the value. |
| 15 | `VALUE_SEQ` | DOUBLE | NOT NULL |  | Sequence of the value for those that have multiple values. |
| 16 | `VALUE_STRING` | VARCHAR(100) |  |  | The textual value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARAMETER_ID` | [DCP_PL_QUERY_PARAMETER](DCP_PL_QUERY_PARAMETER.md) | `PARAMETER_ID` |
| `PATIENT_LIST_ID` | [DCP_PL_QUERY_LIST](DCP_PL_QUERY_LIST.md) | `PATIENT_LIST_ID` |
| `TEMPLATE_ID` | [DCP_PL_QUERY_TEMPLATE](DCP_PL_QUERY_TEMPLATE.md) | `TEMPLATE_ID` |

