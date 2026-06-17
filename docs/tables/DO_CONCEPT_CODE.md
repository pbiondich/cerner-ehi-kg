# DO_CONCEPT_CODE

> The codes from any standard terminology that are aliases to this contextual unit of meaning.

**Description:** DO_CONCEPT_CODE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_CODE` | VARCHAR(100) | NOT NULL |  | Code from the code system. |
| 2 | `DO_CODE_SYSTEM_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the DO_CODE_SYSTEM table. |
| 3 | `DO_CONCEPT_CODE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DO_CONCEPT_CODE table. |
| 4 | `DO_CONCEPT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the DO_CONCEPT table. |
| 5 | `DO_CONTEXT_VERSION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the DO_CONTEXT_VERSION table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DO_CODE_SYSTEM_ID` | [DO_CODE_SYSTEM](DO_CODE_SYSTEM.md) | `DO_CODE_SYSTEM_ID` |
| `DO_CONCEPT_ID` | [DO_CONCEPT](DO_CONCEPT.md) | `DO_CONCEPT_ID` |
| `DO_CONTEXT_VERSION_ID` | [DO_CONTEXT_VERSION](DO_CONTEXT_VERSION.md) | `DO_CONTEXT_VERSION_ID` |

