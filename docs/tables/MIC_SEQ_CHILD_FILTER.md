# MIC_SEQ_CHILD_FILTER

> This reference table contains filter value(s) and defaults for a specified 'child' filter on a sequence.

**Description:** Microbiology Sequence Child Filter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_BEGIN_STRING` | VARCHAR(100) |  |  | This field is used to store the beginning string value for the default filter row. |
| 2 | `FILTER_CD` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to the mic_seq_filter table. The field contains the internal identification code assigned to the filter stored on code_set 25212. |
| 3 | `FILTER_END_STRING` | VARCHAR(100) |  |  | This field is used to store the ending string value for the default filter row. |
| 4 | `FILTER_FLAG` | DOUBLE |  |  | This field is used to store a small numeric value for the default filter row. |
| 5 | `FILTER_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification for this reference table. |
| 6 | `FILTER_NBR` | DOUBLE |  |  | This field is used to store a large numeric value for the default filter row. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field is used to store a code value or identification for the default filter row. The parent_entity_name will determine which table the value came from. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This field is used to store the name of the table that places a value in the parent_entity_id field. |
| 9 | `PARENT_FILTER_ID` | DOUBLE | NOT NULL |  | This field is used to store an identification for the 'parent' filter row. The parent_entity_name will determine which table the value came from. |
| 10 | `PARENT_FILTER_NAME` | VARCHAR(32) | NOT NULL |  | This field is used to store the name of the 'parent filter' table. Currently, this column is only valued with 'MIC_SEQ_FILTER_DEFAULT'. |
| 11 | `PARENT_SEQ` | DOUBLE | NOT NULL |  | This field is used in conjunction with the PARENT_FILTER_NAME and PARENT_FILTER_ID columns to identify the 'parent' filter row. When the PARENT_FILTER_NAME is valued with MIC_SEQ_FILTER_DEFAULT this field maps to the SEQUENCE column on the MIC_SEQ_FILTER_DEFAULT table. |
| 12 | `SEQUENCE_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to sequence information stored on the mic_seq_filter and mic_sequence reference table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

