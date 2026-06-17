# CONFIG_PREFS

> This table is meant to flexibly store software configuration information

**Description:** CONFIGURATION PREFERENCES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_NAME` | VARCHAR(255) | NOT NULL |  | The name portion of the name-value pair for this configuration row. |
| 2 | `CONFIG_PREFS_ID` | DOUBLE | NOT NULL |  | This is the primary index for this table assigned from the CareNet sequence. |
| 3 | `CONFIG_VALUE` | VARCHAR(256) |  |  | The value portion of the name-value pair for this configuration row. |
| 4 | `FLEXED_BY` | VARCHAR(12) | NOT NULL |  | cdf_meaning from 14282 stating how a row is being flexed |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary index of the row from the parent table, if applicable, of how this row of configuration row is being flexed. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent table, if applicable, of how this row of configuration row is being flexed. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

