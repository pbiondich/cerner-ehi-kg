# GROUP_ENTITY_RELTN

> This table will be used to store relationships between Organization and Organization Group.

**Description:** Group Entity Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | sequence of collation |
| 2 | `GROUP_ENTITY_RELTN_ID` | DOUBLE | NOT NULL |  | The unique ID of the group relation. |
| 3 | `GROUP_ID` | DOUBLE | NOT NULL |  | Group identifier e.g. ORG_SET_ID or PERSON_GROUP_ID |
| 4 | `GROUP_NAME` | VARCHAR(30) | NOT NULL |  | Group Name - e.g. Org group, Personnel Group |
| 5 | `RELATED_ID` | DOUBLE | NOT NULL |  | Related Identifier, e.g. Organization_ID |
| 6 | `RELATED_NAME` | VARCHAR(30) | NOT NULL |  | Related Name, e.g. "ORGANIZATION" |
| 7 | `RELATED_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of relation type |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

