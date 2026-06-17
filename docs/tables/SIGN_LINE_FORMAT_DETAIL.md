# SIGN_LINE_FORMAT_DETAIL

> This table includes the line by line format attributes associated with a signature line format.

**Description:** Signature Line Format Detail Parameters Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_POS` | DOUBLE | NOT NULL |  | This field identifies the column position to which the signature line format element is located. If a non-negative number is included in this field, the field represents the actual column print position. If a negative number is included, the field represents the option to let the data elements and literals 'float' together to appear as a single element. |
| 2 | `DATA_ELEMENT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the data element, from codeset 14287, to beprinted in the column position and line number specified. |
| 3 | `DATA_ELEMENT_FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the data element format, from codeset 22669. This field determines the formatting for the data_element_cd. |
| 4 | `FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identifier representing the signature line format. It is used to join to the SIGN_LINE_FORMAT table, which contains the high-level parameters for the signature line format. |
| 5 | `LINE_NBR` | DOUBLE | NOT NULL |  | This field identifies the line number within the signature line format to which the format information included on this record applies. |
| 6 | `LITERAL_DISPLAY` | VARCHAR(100) |  |  | This field contains the literal display value associated with the literal element, if any, specified to print in the signature line format column position and line number. |
| 7 | `LITERAL_SIZE` | DOUBLE | NOT NULL |  | This field contains the printable size (number of characters) for the associated literal display value. This number is automatically calculated by the value written to the LITERAL_DISPLAY field, butcan be overridden by the user building the signature line format. |
| 8 | `MAX_SIZE` | DOUBLE | NOT NULL |  | This field contains the printable size (number of characters) for the associated data element display value. This number is automatically calculated by the value written to the DATA_ELEMENT_CD field, but can be overridden by the user building the signature line format. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field, in combination with the FORMAT_ID field, uniquely identifies a row on this table. |
| 10 | `SUPPRESS_LINE_IND` | DOUBLE | NOT NULL |  | This field indicates whether a line should be suppressed from the signature line if it is empty. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORMAT_ID` | [SIGN_LINE_FORMAT](SIGN_LINE_FORMAT.md) | `FORMAT_ID` |

