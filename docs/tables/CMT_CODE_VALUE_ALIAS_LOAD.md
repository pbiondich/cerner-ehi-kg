# CMT_CODE_VALUE_ALIAS_LOAD

> Used only to load CMT data to the CODE_VALUE_ALIAS table.

**Description:** CMT_CODE_VALUE_ALIAS_LOAD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIAS` | VARCHAR(255) | NOT NULL |  | Loads ALIAS on CODE_VALUE_ALIAS. |
| 2 | `ALIAS_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | Loads ALIAS_TYPE_MEANING on CODE_VALUE_ALIAS. |
| 3 | `CODE_SET` | DOUBLE | NOT NULL |  | Loads CODE_SET on CODE_VALUE_ALIAS. |
| 4 | `CODE_VALUE_UUID` | VARCHAR(100) | NOT NULL |  | Loads CODE_VALUE_UUID on CODE_VALUE_ALIAS. |
| 5 | `CONTRIBUTOR_SOURCE_MEAN` | VARCHAR(12) | NOT NULL |  | Loads CONTRIBUTOR_SOURCE_MEAN on CODE_VALUE_ALIAS. |
| 6 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Loads PRIMARY_IND on CODE_VALUE_ALIAS. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

