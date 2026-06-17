# PM_FILTER_VALUES

> This table holds the relationship for a filter value.

**Description:** This table contains relationships for filter values.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_VALUE` | VARCHAR(100) | NOT NULL |  | Initial value for filter. |
| 2 | `END_VALUE` | VARCHAR(100) |  |  | Last value for filter values. |
| 3 | `FIELD_TYPE` | VARCHAR(12) |  |  | Type of field for filter |
| 4 | `PM_FILTER_ID` | DOUBLE | NOT NULL | FK→ | foreign key |
| 5 | `PM_FILTER_VALUES_ID` | DOUBLE | NOT NULL |  | primary key |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type flag for value |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_FILTER_ID` | [PM_FILTER](PM_FILTER.md) | `PM_FILTER_ID` |

