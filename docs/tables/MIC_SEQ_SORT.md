# MIC_SEQ_SORT

> This reference table contains the sorts associated with a sequence.

**Description:** Microbiology Sequence Sort  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASCENDING_IND` | DOUBLE |  |  | This indicator value specifies whether or not the report generated from the sequence should be ordered ascending or descending by the associated sort field. |
| 2 | `PAGE_BREAK_IND` | DOUBLE |  |  | This indicator value specifies whether or not the report generated from the sequence should page break on the associated sort field. |
| 3 | `SEQUENCE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to sequence information stored on the mic_sequence reference table. |
| 4 | `SORT_CD` | DOUBLE | NOT NULL |  | If a sort was entered for the sequence, this field contains the internal identification code assigned to the sort. Sorts are stored on code_set 25213. |
| 5 | `SORT_SEQ` | DOUBLE |  |  | This field contains a numeric value that is used to order sorts used for a sequence. For example, this field would be used to sequence service resource #1 and task date/time #2. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQUENCE_ID` | [MIC_SEQUENCE](MIC_SEQUENCE.md) | `SEQUENCE_ID` |

