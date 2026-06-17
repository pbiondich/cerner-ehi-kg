# CODE_VALUE_OUTBOUND

> This table is used to provider outbound interface mechanisms a translation from code_value to the receiving system's nomenclature.

**Description:** Outbound alias translations  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS` | VARCHAR(100) | NOT NULL |  | The actual outbound alias |
| 2 | `ALIAS_TYPE_MEANING` | VARCHAR(12) |  |  | The meaning of the alias. Used when alias is not unique enough within a code_set. |
| 3 | `CODE_SET` | DOUBLE | NOT NULL | FK→ | The Code Set for the code_value. - This is a denormalized column and reads should be from Code_value.code_set of the code_value |
| 4 | `CODE_VALUE` | DOUBLE | NOT NULL | FK→ | Code value of the outbound alias. This is a denormalized column and reads should be from Code_value.code_set of the code_value. |
| 5 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Contributing System CD for the destination system |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |
| `CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

