# CODE_VALUE_EXTENSION

> The code value extension entity stores the values of the additional values defined by the code set extension entity. Extended fields will be stored as alpha and should be converted by the client application.

**Description:** The code value extension entity stores the values of the add  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | DOUBLE | NOT NULL | FK→ | The code set for the extension. This is a denormalized column and reads should be from Code_value.code_set of the code_value. |
| 2 | `CODE_VALUE` | DOUBLE | NOT NULL | FK→ | code value |
| 3 | `FIELD_NAME` | VARCHAR(32) | NOT NULL | FK→ | The field name of the extension. |
| 4 | `FIELD_TYPE` | DOUBLE |  |  | The data type of the code value extension. This is a denormalized column and reads should be from Code_set_extension.field_type of the code_set/field_name. |
| 5 | `FIELD_VALUE` | VARCHAR(100) |  |  | The actual stored value |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_SET_EXTENSION](CODE_SET_EXTENSION.md) | `CODE_SET` |
| `CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FIELD_NAME` | [CODE_SET_EXTENSION](CODE_SET_EXTENSION.md) | `FIELD_NAME` |

