# PREFDIR_MULTIVALUE

> This table stores meta data about a preference value for an entry. A non zero value indicates the entry can contain more than 1 value.

**Description:** Meta data table for a preference entry  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTRY_ID` | DOUBLE | NOT NULL | FK→ | This is the id that uniquely identifies a preference in the prefdir_entrydata table. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VALUE` | VARCHAR(4) | NOT NULL |  | Value indicating if a preference entry can contain a single value or more than 1 value. |
| 8 | `VALUE_UPPER` | VARCHAR(4) | NOT NULL |  | The upper case version of value for sorting purposes. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENTRY_ID` | [PREFDIR_ENTRYDATA](PREFDIR_ENTRYDATA.md) | `ENTRY_ID` |

