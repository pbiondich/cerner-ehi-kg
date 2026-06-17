# RES_CD_ARG_QUEUE

> Additional arbitrary data needed to accommodate reference code assignment.

**Description:** Result Code Argument Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARG_GROUP_SEQ` | DOUBLE | NOT NULL |  | The sequence of this argument group in relation to a particular contributor system and reference number. |
| 2 | `ARG_NAME` | VARCHAR(30) | NOT NULL |  | The name of the argument which describes what the argument value is defining. |
| 3 | `ARG_SEQ` | DOUBLE | NOT NULL |  | The sequence of this argument in relation to a particular contributor system and reference number. |
| 4 | `ARG_VALUE` | DOUBLE |  |  | The value of the argument. The meaning of the argument is described by the argument name. |
| 5 | `ASSIGNMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Assignment method which was used to make the reference code assignment. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `REFERENCE_NBR_TXT` | VARCHAR(100) | NOT NULL |  | The combination of the reference number and the contributor system code provides a unique identifier to the origin of the data. |
| 8 | `RES_CD_ARG_QUEUE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies data needed to accommodate reference code assignment. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

