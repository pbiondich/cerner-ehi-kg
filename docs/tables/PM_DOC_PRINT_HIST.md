# PM_DOC_PRINT_HIST

> Provides the history of documents printed from practice management.

**Description:** Patient Management Document Print History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter related to the printed document. |
| 2 | `OUTPUT_DESTINATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the output destination to which the document was distributed. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person for whom the document was printed. |
| 4 | `PM_DOC_PRINT_HIST_ID` | DOUBLE | NOT NULL |  | Computer generated number to uniquely identify a row on the PM_DOC_PRINT_HIST table. |
| 5 | `PRINTED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person who printed the document. |
| 6 | `PRINTED_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the document that was printed. |
| 7 | `PRINTED_DT_TM` | DATETIME | NOT NULL |  | The date and time the document was printed. |
| 8 | `PRINTED_FILE_NAME` | VARCHAR(100) | NOT NULL |  | The file name of the document that was printed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `OUTPUT_DESTINATION_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRINTED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRINTED_DOCUMENT_ID` | [PM_DOC_DOCUMENT](PM_DOC_DOCUMENT.md) | `DOCUMENT_ID` |

