# TRACK_GROUP

> Table used to store Parent/Child relationships between tracking reference tables and other code value records.

**Description:** Tracking Group Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_TABLE` | VARCHAR(40) |  |  | Child Table |
| 2 | `CHILD_VALUE` | DOUBLE | NOT NULL |  | Child Value |
| 3 | `COLLATION_SEQ` | DOUBLE |  |  | Collation SequenceColumn |
| 4 | `PARENT_VALUE` | DOUBLE | NOT NULL |  | Parent Value |
| 5 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group CodeColumn |
| 6 | `TRACKING_RULE` | VARCHAR(200) |  |  | Tracking RuleColumn |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

