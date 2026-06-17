# CODE_SET_EXTENSION

> Code sets can be extended by adding additional parameters to the code set definition. This is done in a name value pair lookup approach. Each additional parameter becomes a row on the code set extension entity.

**Description:** Code set extensions  
**Table type:** REFERENCE  
**Primary key:** `CODE_SET`, `FIELD_NAME`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FIELD` | VARCHAR(50) |  |  | Not currently used |
| 2 | `CODE_SET` | DOUBLE | NOT NULL | PK FK→ | The code set for the code value |
| 3 | `FIELD_DEFAULT` | VARCHAR(50) |  |  | The default value |
| 4 | `FIELD_HELP` | VARCHAR(100) |  |  | A simple caption explaining the field |
| 5 | `FIELD_IN_MASK` | VARCHAR(50) |  |  | The input mask for the code value extension |
| 6 | `FIELD_LEN` | DOUBLE |  |  | The length of the code value extension |
| 7 | `FIELD_NAME` | VARCHAR(32) | NOT NULL | PK | The field name of the extension. |
| 8 | `FIELD_OUT_MASK` | VARCHAR(50) |  |  | The output mask for the code value extension |
| 9 | `FIELD_PROMPT` | VARCHAR(50) |  |  | The prompt for the code value extension |
| 10 | `FIELD_SEQ` | DOUBLE |  |  | The order in which the code value extension is prompted for. |
| 11 | `FIELD_TYPE` | DOUBLE |  |  | The data type of the code value extension |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VALIDATION_CODE_SET` | DOUBLE |  |  | The code_set that all responses must exist in |
| 18 | `VALIDATION_CONDITION` | VARCHAR(100) |  |  | The check for valid values (i.e. only allow X and Z) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CODE_VALUE_EXTENSION](CODE_VALUE_EXTENSION.md) | `CODE_SET` |
| [CODE_VALUE_EXTENSION](CODE_VALUE_EXTENSION.md) | `FIELD_NAME` |

