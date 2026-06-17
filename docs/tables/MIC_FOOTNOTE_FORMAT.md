# MIC_FOOTNOTE_FORMAT

> This reference table contains a record for each detail that defines a footnote format.

**Description:** Microbiology Footnote Format  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODED_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the coded response, if any, associated withthe format detail on the line number specified. |
| 2 | `DATA_ELEMENT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the data element to be printed in the footnote detail on the line number specified. |
| 3 | `DATE_FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the date format associated with the format detail if a date element is selected in the DATA_ELEMENT_CD field. |
| 4 | `FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code assigned to display format of the correlation message. |
| 5 | `LINE_NUMBER` | DOUBLE | NOT NULL |  | This field identifies the line number within the footnote format to which the format information included on this record applies. |
| 6 | `LITERAL` | VARCHAR(255) |  |  | This field contains the literal display value associated with the data element, if any, specified to print in the footnote format detail. |
| 7 | `MAX_SIZE` | DOUBLE |  |  | This field contains the printable size (number of characters) for the associated data element IF the data element includes a free text comment. |
| 8 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | This field contains a value indicating that the footnote format detail is required or not required to be completed by the user. |
| 9 | `SEPARATOR` | DOUBLE |  |  | This field identifies the number of spaces between the LITERAL and DATA_ELEMENT defined in the format detail. |
| 10 | `SEPARATOR2` | DOUBLE |  |  | This field identifies the number of spaces in front of the LITERAL defined in the format detail. |
| 11 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a sequence value that, when combined with the FORMAT_CD make the unique table key value. It also determines the order in which the details are displayed in the footnote |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

