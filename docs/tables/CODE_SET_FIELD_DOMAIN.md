# CODE_SET_FIELD_DOMAIN

> Codes sets may have the ability to filter the code values that are displayed based on certain user defined parameters. The code set field domain entity contains a list of valid code sets that can be used to establish code set filtering.

**Description:** The code_set_field_domain entity contains a list of valid co  
**Table type:** REFERENCE  
**Primary key:** `CODE_SET`, `REFERENCE`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_SET` | DOUBLE | NOT NULL | PK FK→ | Not currently used |
| 2 | `REFERENCE` | DOUBLE | NOT NULL | PK | Not currently used |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CODE_SET_DOMAIN](CODE_SET_DOMAIN.md) | `CODE_SET` |
| [CODE_SET_DOMAIN](CODE_SET_DOMAIN.md) | `REFERENCE` |

