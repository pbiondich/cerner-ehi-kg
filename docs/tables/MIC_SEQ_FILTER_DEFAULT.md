# MIC_SEQ_FILTER_DEFAULT

> This reference table contains the default filter value(s) for a specified filter on a sequence.

**Description:** Microbiology Sequence Filter Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_BEGIN_STRING` | VARCHAR(100) |  |  | This field is used to store the beginning string value for the default filter row. |
| 2 | `FILTER_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the mic_seq_filter table. The field contains the internal identification code assigned to the filter stored on code_set 25212. |
| 3 | `FILTER_END_STRING` | VARCHAR(100) |  |  | This field is used to store the ending string value for the default filter row. |
| 4 | `FILTER_FLAG` | DOUBLE |  |  | This field is used to store a small numeric value for the default filter row. |
| 5 | `FILTER_NBR` | DOUBLE |  |  | This field is used to store a large numeric value for the default filter row. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field is used to store a code value or identification for the default filter row. The parent_entity_name will determine which table the value came from. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | This field is used to store the name of the table that places a value in the parent_entity_id field. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field, in conjunction with the value included in the sequence_id and filter_cd field, uniquely identifies a row on this table. |
| 9 | `SEQUENCE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to sequence information stored on the mic_seq_filter and mic_sequence reference table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_CD` | [MIC_SEQ_FILTER](MIC_SEQ_FILTER.md) | `FILTER_CD` |
| `SEQUENCE_ID` | [MIC_SEQ_FILTER](MIC_SEQ_FILTER.md) | `SEQUENCE_ID` |

