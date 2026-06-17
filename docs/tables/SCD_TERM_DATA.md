# SCD_TERM_DATA

> Additional term data which is stored with specialized terms types. Activity data.

**Description:** SCD Term Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FKEY_ENTITY_NAME` | VARCHAR(32) |  |  | Entity (table name) for link to another entity |
| 2 | `FKEY_ID` | DOUBLE | NOT NULL |  | key to a foreign table (table identified by FKEY_ENTITY_NAME). |
| 3 | `SCD_TERM_DATA_ID` | DOUBLE | NOT NULL | FK→ | Term Id for the term data, slaved to scr_term_id |
| 4 | `SCD_TERM_DATA_KEY` | VARCHAR(255) |  |  | Term Data Key |
| 5 | `SCD_TERM_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | type/formate/use of the data in this row. |
| 6 | `UNITS_CD` | DOUBLE | NOT NULL |  | units for the term. |
| 7 | `VALUE_DT_TM` | DATETIME |  |  | Date/Time Value of node. |
| 8 | `VALUE_DT_TM_OS` | DOUBLE |  |  | Offset, in fractional days, from VALUE_DT_TM. |
| 9 | `VALUE_NUMBER` | DOUBLE |  |  | Number value of node. If the term contains a number, this column will be populated. |
| 10 | `VALUE_TEXT` | VARCHAR(255) |  |  | Value text of node. |
| 11 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCD_TERM_DATA_ID` | [SCD_TERM](SCD_TERM.md) | `SCD_TERM_ID` |

