# CNT_DS_SECTION_R

> Identifies the relationship between CNT_DS_KEY and CNT_DS_SECTION_KEY.

**Description:** Content Doc Set Section Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_DS_KEY_UID` | VARCHAR(100) | NOT NULL |  | UID of the doc set, used for relating doc set and section |
| 2 | `CNT_DS_SECTION_KEY_UID` | VARCHAR(100) | NOT NULL |  | UID of the doc set section, used for relating doc set and section |
| 3 | `CNT_DS_SECTION_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_DS_SECTION_R table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

