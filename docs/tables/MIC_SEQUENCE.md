# MIC_SEQUENCE

> This reference table contains a single record for every sequence included in the PathNet Microbiology system. It is a key table for most reports (reports retrieve information based upon a defined sequence).

**Description:** Microbiology Sequence  
**Table type:** REFERENCE  
**Primary key:** `SEQUENCE_ID`  
**Columns:** 10  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(60) |  |  | This field stores the description associated with the sequence. |
| 3 | `DISPLAY` | VARCHAR(40) |  |  | This field stores the display associated with the sequence. |
| 4 | `SEQUENCE_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the sequence (and itsassociated parameters). This value is used to join to other tables, such as the mic_seq_sort table. |
| 5 | `SEQ_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field is used to store the type of sequence (Management or Statistical). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [MIC_SEQ_FILTER](MIC_SEQ_FILTER.md) | `SEQUENCE_ID` |
| [MIC_SEQ_PRINTER](MIC_SEQ_PRINTER.md) | `SEQUENCE_ID` |
| [MIC_SEQ_REPORT_R](MIC_SEQ_REPORT_R.md) | `SEQUENCE_ID` |
| [MIC_SEQ_SERVICE_RESOURCE](MIC_SEQ_SERVICE_RESOURCE.md) | `SEQUENCE_ID` |
| [MIC_SEQ_SORT](MIC_SEQ_SORT.md) | `SEQUENCE_ID` |

