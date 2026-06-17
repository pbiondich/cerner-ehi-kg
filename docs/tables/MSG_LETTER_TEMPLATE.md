# MSG_LETTER_TEMPLATE

> Points to the letter template assigned to a user or position.

**Description:** MSG_LETTER_TEMPLATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Row in the LONG_BLOB_REFERENCE table that holds the assigned template text. |
| 2 | `MSG_LETTER_TEMPLATE_ID` | DOUBLE | NOT NULL |  | Primary key |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position assigned to the referenced template. Will be zero if PRSNL_ID is non-zero. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel assigned to the referenced template. Will be zero if POSITION_CD is non-zero. |
| 5 | `TEMPLATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines the type of template being saved. 0 represents the standard default result letter template, and 1 represents the patient ad hoc letter template. |
| 6 | `TEXT_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence the text entries should be read back if they spans multiple blob rows. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

