# MIC_SEQ_FILTER

> This reference table contains the filters associated with a sequence.

**Description:** Microbiology Sequence Filter  
**Table type:** REFERENCE  
**Primary key:** `FILTER_CD`, `SEQUENCE_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_CD` | DOUBLE | NOT NULL | PK | If a filter was entered for the sequence, this field contains the internal identification code assigned to the filter. Filters are stored on code_set 25212. |
| 2 | `SEQUENCE_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the foreign key value used to join to sequence information stored on the mic_sequence reference table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQUENCE_ID` | [MIC_SEQUENCE](MIC_SEQUENCE.md) | `SEQUENCE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_SEQ_FILTER_DEFAULT](MIC_SEQ_FILTER_DEFAULT.md) | `FILTER_CD` |
| [MIC_SEQ_FILTER_DEFAULT](MIC_SEQ_FILTER_DEFAULT.md) | `SEQUENCE_ID` |

