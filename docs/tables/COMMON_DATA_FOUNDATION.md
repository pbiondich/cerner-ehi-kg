# COMMON_DATA_FOUNDATION

> Used to store processing meanings and give code values universal meaning.

**Description:** Common Data Foundation or CDF_MEANING  
**Table type:** REFERENCE  
**Primary key:** `CDF_MEANING`, `CODE_SET`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDF_MEANING` | VARCHAR(12) | NOT NULL | PK | The actual string value for the cdf meaning |
| 2 | `CODE_SET` | DOUBLE | NOT NULL | PK FK→ | The code set of the cdf meaning |
| 3 | `DEFINITION` | VARCHAR(100) |  |  | The definition for the cdf meaning |
| 4 | `DISPLAY` | VARCHAR(40) | NOT NULL |  | The display string for the cdf meaning |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CODE_CDF_EXT](CODE_CDF_EXT.md) | `CDF_MEANING` |
| [CODE_CDF_EXT](CODE_CDF_EXT.md) | `CODE_SET` |

