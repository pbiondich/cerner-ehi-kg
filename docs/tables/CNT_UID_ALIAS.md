# CNT_UID_ALIAS

> Table to hold UID aliasing

**Description:** CNT_UID_ALIAS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_UID` | VARCHAR(100) | NOT NULL |  | This field contains the UID for the CNT item that is aliased |
| 2 | `CNT_UID_ALIAS` | VARCHAR(100) | NOT NULL |  | This field contains the alias for the given UID and Domain |
| 3 | `CNT_UID_ALIAS_ID` | DOUBLE | NOT NULL |  | This field is a PK sequence value for the table. |
| 4 | `CNT_UID_DOMAIN` | VARCHAR(50) |  |  | This defines the domain for CNT that the alias is for. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

