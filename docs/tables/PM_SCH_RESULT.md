# PM_SCH_RESULT

> Search results.

**Description:** Search results.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Data type of this column. |
| 2 | `DISPLAY` | VARCHAR(100) |  |  | Display value |
| 3 | `FORMAT` | VARCHAR(100) |  |  | Formatting to apply to this column. |
| 4 | `MEANING` | VARCHAR(12) |  |  | Meaning. |
| 5 | `OPTIONS` | VARCHAR(100) |  |  | Options. |
| 6 | `SCENARIO` | DOUBLE |  |  | Scenario. |
| 7 | `SEQUENCE` | DOUBLE |  |  | Order. |
| 8 | `SETUP_ID` | DOUBLE | NOT NULL | FK→ | Setup ID. |
| 9 | `SORT_FLAG` | DOUBLE |  |  | Sorted. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SETUP_ID` | [PM_SCH_SETUP](PM_SCH_SETUP.md) | `SETUP_ID` |

