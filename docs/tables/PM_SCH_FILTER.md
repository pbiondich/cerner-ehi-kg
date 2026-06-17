# PM_SCH_FILTER

> Search filter.

**Description:** Search filter.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Date type. |
| 2 | `DISPLAY` | VARCHAR(100) |  |  | Display value |
| 3 | `HIDDEN_IND` | DOUBLE |  |  | Hidden. |
| 4 | `MEANING` | VARCHAR(12) |  |  | Meaning. |
| 5 | `OPTIONS` | VARCHAR(100) |  |  | Options. |
| 6 | `REQUIRED_IND` | DOUBLE |  |  | Required indicator. |
| 7 | `SCENARIO` | DOUBLE |  |  | Scenario. |
| 8 | `SEQUENCE` | DOUBLE |  |  | Order. |
| 9 | `SETUP_ID` | DOUBLE | NOT NULL | FK→ | Setup ID. |
| 10 | `VALUE` | VARCHAR(100) |  |  | Value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SETUP_ID` | [PM_SCH_SETUP](PM_SCH_SETUP.md) | `SETUP_ID` |

