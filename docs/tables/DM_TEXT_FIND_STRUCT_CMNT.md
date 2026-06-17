# DM_TEXT_FIND_STRUCT_CMNT

> Table to support new Mark as Reviewed feature for Structured Data content containing ECD9 content.

**Description:** Data Management - Text Find Structure Comment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_DT_TM` | DATETIME | NOT NULL |  | Date the comment was written |
| 2 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the personnel id for the user recording this comment |
| 3 | `COMMENT_STATE_FLAG` | DOUBLE | NOT NULL |  | The state of this particular comment |
| 4 | `COMMENT_TEXT` | VARCHAR(1000) |  |  | The text provided to describe why this comment is being added |
| 5 | `DM_TEXT_FIND_STRUCT_CMNT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `DM_TEXT_FIND_STRUCT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to the structured object this row is a comment for |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DM_TEXT_FIND_STRUCT_ID` | [DM_TEXT_FIND_STRUCT](DM_TEXT_FIND_STRUCT.md) | `DM_TEXT_FIND_STRUCT_ID` |

