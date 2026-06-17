# CODE_CDF_EXT

> cdf meanings can be extended by adding additional parameters to the code_cdf_ext table. This is done in a name value pair lookup approach. Each additional parameter becomes a row on the code cddf ext entity.

**Description:** cdf_meaning extensions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FIELD` | VARCHAR(50) |  |  | Not currently used |
| 2 | `CDF_MEANING` | VARCHAR(12) | NOT NULL | FK→ | The cdf_meaning that the extension is for. |
| 3 | `CODE_SET` | DOUBLE | NOT NULL | FK→ | The code set of the cdf extension |
| 4 | `FIELD_DEFAULT` | VARCHAR(50) |  |  | The default value |
| 5 | `FIELD_HELP` | VARCHAR(100) |  |  | A simple caption explaining the field |
| 6 | `FIELD_IN_MASK` | VARCHAR(50) |  |  | The input mask for the cdf extension |
| 7 | `FIELD_LEN` | DOUBLE |  |  | The length of the cdf extension |
| 8 | `FIELD_NAME` | VARCHAR(32) | NOT NULL |  | The field name of the extension. |
| 9 | `FIELD_OUT_MASK` | VARCHAR(50) |  |  | The output mask for the cdf extension |
| 10 | `FIELD_PROMPT` | VARCHAR(50) |  |  | The prompt for the cdf extension |
| 11 | `FIELD_SEQ` | DOUBLE |  |  | The order in which the cdf extension is prompted for. |
| 12 | `FIELD_TYPE` | DOUBLE |  |  | The data type of the cdf extension |
| 13 | `FIELD_VALUE` | VARCHAR(100) |  |  | The actual stored value |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VAL_CODE_SET` | DOUBLE |  |  | The code_set that all responses must exist in |
| 20 | `VAL_CONDITION` | VARCHAR(100) |  |  | The check for valid values (i.e. only allow X and Z) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDF_MEANING` | [COMMON_DATA_FOUNDATION](COMMON_DATA_FOUNDATION.md) | `CDF_MEANING` |
| `CODE_SET` | [COMMON_DATA_FOUNDATION](COMMON_DATA_FOUNDATION.md) | `CODE_SET` |

