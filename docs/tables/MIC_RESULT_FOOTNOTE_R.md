# MIC_RESULT_FOOTNOTE_R

> This table contains information associating the susceptibility footnote text from the long_text table with the antibiotic.

**Description:** Reference table for footnotes.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the antibiotic. Antibiotics are defined on code set 1011. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the long_text_id associated with the footnote text. The footnote text is stored on the long_text table. |
| 3 | `TASK_LOG_ID` | DOUBLE | NOT NULL |  | This field identifies the unique value assigned to the susceptibility task from the mic_task_log table thus associating the susceptibility task with the footnote. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANTIBIOTIC_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

