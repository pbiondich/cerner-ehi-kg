# PREFDIR_CONTEXT

> A 'context' is a term used to identify the level at which preferences are being defined. Examples of a context are Users, Positions, Locations, Default (System/Org wide) etc. Contexts are defined by application architects.

**Description:** Preference directory context.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTRY_ID` | DOUBLE | NOT NULL |  | Entry id that we are setting a context for. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `VALUE` | VARCHAR(64) | NOT NULL |  | Normalized attribute values |
| 8 | `VALUE_UPPER` | VARCHAR(64) | NOT NULL |  | An upper case version of the value is stored for string comparison purposes for an equality search. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

