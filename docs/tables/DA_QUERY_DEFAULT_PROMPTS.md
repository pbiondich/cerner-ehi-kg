# DA_QUERY_DEFAULT_PROMPTS

> Contains the default prompts for a user of a Discern Analytics 2.0 Query,

**Description:** Discern Analytics Query Default Prompts  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_QUERY_DEFAULT_PROMPTS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DA_QUERY_DEFAULT_PROMPTS table. |
| 2 | `DA_QUERY_ID` | DOUBLE | NOT NULL | FK→ | The query that these prompts apply to. |
| 3 | `DEFAULT_PROMPTS_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Pointer to the LONG_TEXT_REFERENCE row that contains the default prompts for the query. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `USER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user that selected these prompts during the query execution. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_QUERY_ID` | [DA_QUERY](DA_QUERY.md) | `DA_QUERY_ID` |
| `DEFAULT_PROMPTS_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `USER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

