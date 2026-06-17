# CKI_ENTITY_RELTN

> Provide a generic mechanism for specifying a CKI for some other DB entity.

**Description:** Relate a CKI to a DB entity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI` | VARCHAR(255) | NOT NULL |  | A unique external identifier for CKI |
| 2 | `CKI_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | Entity ID of parent table to which this row is related as a child. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the CKI_ENTITY_RELTN row is related |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

