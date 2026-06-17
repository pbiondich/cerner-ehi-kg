# TRACK_LIST_ASSIGNMENT

> Maintain list of assignments. One tracking list can be assigned to multiple positions or users.

**Description:** Track List Assignment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LIST_SEQ` | DOUBLE | NOT NULL |  | List Sequence |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The position_cd or prsnl_id to which this list is being assigned. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Entity Name which correlates with the entity id |
| 4 | `TRACK_LIST_ASSIGNMENT_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 5 | `TRACK_LIST_ID` | DOUBLE | NOT NULL | FK→ | The tracking list that is assigned Foreign Key value from TRACK_LIST. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_LIST_ID` | [TRACK_LIST](TRACK_LIST.md) | `TRACK_LIST_ID` |

