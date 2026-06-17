# TRACK_FILTER_VALUE

> Describes the data values for a custom tracking field that will be included when filtering.

**Description:** TRACK FILTER VALUE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OPERATOR_FLAG` | DOUBLE | NOT NULL |  | Operator to be used when evaluating this filter value.EQUALS = 0, LESS THAN = 1, GREATER THAN = 2, LESS THAN EQUALS = 3, GREATER THAN EQUALS = 4, STARTS WITH = 5, CONTAINS = 6 |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID value from the parent table identified in PARENT_ENTITY_NAME |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the Parent Entity |
| 4 | `TRACK_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key ID from the TRACK FILTER table for the filter that these refinements are describing |
| 5 | `TRACK_FILTER_VALUE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALUE_AMT` | DOUBLE | NOT NULL |  | Double data value to include when filtering |
| 12 | `VALUE_DT_TM` | DATETIME |  |  | Date data value to include when filtering |
| 13 | `VALUE_TXT` | VARCHAR(128) | NOT NULL |  | Text data value to include when filtering |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_FILTER_ID` | [TRACK_FILTER](TRACK_FILTER.md) | `TRACK_FILTER_ID` |

