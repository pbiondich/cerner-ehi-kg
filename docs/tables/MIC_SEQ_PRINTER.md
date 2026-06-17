# MIC_SEQ_PRINTER

> This reference table contains the printers associated with a sequence.

**Description:** Microbiology Sequence Printer  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NBR_OF_COPIES` | DOUBLE |  |  | This field contains the 'number of copies' value specified by the user when the sequence was executed. |
| 2 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the output destination (related to a printer and a print queue) used to print the output produced after executing the sequence. |
| 3 | `SEQUENCE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to sequence information stored on the mic_sequence reference table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `SEQUENCE_ID` | [MIC_SEQUENCE](MIC_SEQUENCE.md) | `SEQUENCE_ID` |

