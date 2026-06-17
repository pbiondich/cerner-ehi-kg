# DM_TEXT_FIND_COMMENT

> Stores a list of unstructured objects the user has chosen to exclude from their interrogator reports.

**Description:** DM_TEXT_FIND_COMMENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_COL_DT_TM` | DATETIME | NOT NULL |  | The date value stored in the column named in comment_col_name to use for comparison by the interrogator application. |
| 2 | `COMMENT_COL_NAME` | VARCHAR(30) | NOT NULL |  | The name of the column used to compare for source object changes. This will likely be 'scriptCompileDate', but other values may be provided. |
| 3 | `COMMENT_DT_TM` | DATETIME | NOT NULL |  | The date this comment was requested. |
| 4 | `COMMENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who is requesting this comment. |
| 5 | `COMMENT_STATE_FLAG` | DOUBLE | NOT NULL |  | The state flag to indicate the state of the comment when it was recorded by the user. |
| 6 | `COMMENT_TEXT` | VARCHAR(1000) |  |  | The message, if any, the user records to indicate why they are excluding this object. |
| 7 | `COMMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type flag indicator used to differentiate between comment types. |
| 8 | `DATA_SOURCE` | VARCHAR(255) | NOT NULL |  | The object source_data identifier, as determined by the interrogator application. |
| 9 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND_CAT table for the category this comment is associated with. |
| 10 | `DM_TEXT_FIND_COMMENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DM_TEXT_FIND_COMMENT table. |
| 11 | `DM_TEXT_FIND_DATA_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND_DATA table for the object being commented on. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DM_TEXT_FIND_CAT_ID` | [DM_TEXT_FIND_CAT](DM_TEXT_FIND_CAT.md) | `DM_TEXT_FIND_CAT_ID` |
| `DM_TEXT_FIND_DATA_ID` | [DM_TEXT_FIND_DATA](DM_TEXT_FIND_DATA.md) | `DM_TEXT_FIND_DATA_ID` |

