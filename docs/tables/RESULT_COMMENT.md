# RESULT_COMMENT

> Table defines the relationship for chartable and non-chartable text for a result.

**Description:** Result Comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Starts at one and is incremented for each version of a comment that is stored in the table. Used for tracking the different versions of comments entered into the system. |
| 2 | `COMMENT_DT_TM` | DATETIME |  |  | Defines the date and time the comment was entered in the system. |
| 3 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | A unique internal system assigned number that identifies a specific person/user who entered the comment information. Creates a relationship to the personnel (prsnl) table. |
| 4 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific type of comment as either chartable or non-chartable. |
| 5 | `COMMENT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a specific comment text. Creates a relationship to the long text table. |
| 7 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique internal system assigned number that identifies a specific result that the comment applies to. Creates a relationship to the result table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |

