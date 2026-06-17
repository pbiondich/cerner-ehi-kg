# EMPI_NAME_THESAURUS

> Table is used to store the empi AKA names. A row consists of the name group name and then a member of that group. There can be multiple rows for a name group with the same name.

**Description:** Table is used to store the empi AKA names.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMPI_NAME_THESAURUS_ID` | DOUBLE | NOT NULL |  | Unique key to identify a name pair. |
| 2 | `MEMBER` | VARCHAR(40) | NOT NULL |  | A member of a name group. |
| 3 | `NAME_GROUP` | VARCHAR(40) | NOT NULL |  | Name of a name group. Name groups will have multiple members. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

