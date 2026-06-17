# CHART_FORMAT

> chart format

**Description:** This table stores the different chart formats and their associated symbols  
**Table type:** REFERENCE  
**Primary key:** `CHART_FORMAT_ID`  
**Columns:** 54  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_SYMBOL` | VARCHAR(1) |  |  | This defines the symbol that will print beside abnormal results |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADDITIONAL_INFO_ID` | DOUBLE | NOT NULL | FK→ | Long text ID of additional information for a chart format. Foreign key link to long_text_reference table. |
| 7 | `ADDRESS_COL_NBR` | DOUBLE | NOT NULL |  | Determines the starting column where the address will be placed in the report. |
| 8 | `ADDRESS_PAGE_IND` | DOUBLE | NOT NULL |  | Indicates if an address cover page needs to be printed for this document. |
| 9 | `ADDRESS_ROTATE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to rotate the address page 90 degrees. |
| 10 | `ADDRESS_ROW_NBR` | DOUBLE | NOT NULL |  | Determines the starting row where the address will be placed in the report. |
| 11 | `ASCII_IND` | DOUBLE | NOT NULL |  | ASCII format indicator. 1 = ASCII format, 0 = not ASCII |
| 12 | `BLANK_PAGE_STMT` | VARCHAR(132) |  |  | Defines the statement that should print on the last page of the chart if the last page is blank. |
| 13 | `CHART_FORMAT_DESC` | VARCHAR(64) |  |  | This is the chart format name |
| 14 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | PK | This is the id that uniquely defines the chart format |
| 15 | `CORRECTED_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that is defined to print beside a corrected result |
| 16 | `CRITICAL_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a critical result |
| 17 | `DATE_MASK` | VARCHAR(50) |  |  | This field stores a date mask to be used on all date within this group. |
| 18 | `DOCUMENT_NAME` | VARCHAR(100) |  |  | This is the name of the facesheet that the user selects in Chart Format Builder |
| 19 | `E_DOC_FTR_NBR` | DOUBLE | NOT NULL |  | Stores the document image footer margin to be applied when exclude footers has been selected |
| 20 | `E_DOC_HDR_NBR` | DOUBLE | NOT NULL |  | Stores the document image header margin to be applied when exclude headers has been selected |
| 21 | `FTNOTES_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a result that has a result comment, corrected footnote or any other footnote. |
| 22 | `FTNOTE_LOC_FLAG` | DOUBLE |  |  | Defines where footnotes will print on the chart. Applies to the entire chart. |
| 23 | `HEADER_PAGE_IND` | DOUBLE |  |  | Indicator for header page. |
| 24 | `HIGH_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a high result |
| 25 | `INCLUDE_PRSNL_HIST_IND` | DOUBLE | NOT NULL |  | Indicator noting whether or not to include a personnel history at the end of the report. |
| 26 | `INTERP_DATA_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a procedure that is defined with interpretive data |
| 27 | `INTERP_LOC_FLAG` | DOUBLE |  |  | Defines where interp data will print on the chart. Applies to the entire chart. |
| 28 | `I_DOC_FTR_NBR` | DOUBLE | NOT NULL |  | Stores the document image footer margin to be applied when include footers has been selected |
| 29 | `I_DOC_HDR_NBR` | DOUBLE | NOT NULL |  | Stores the document image header margin to be applied when include headers has been selected |
| 30 | `LEFT_MARGIN_NBR` | DOUBLE | NOT NULL |  | Stores the document image left margin to be applied |
| 31 | `LOW_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a low result |
| 32 | `NEW_RESULT_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside a new result |
| 33 | `ORD_COMMENT_FLAG` | DOUBLE |  |  | Tells whether order comments are suppressed for this chart or not. |
| 34 | `PAGE_BRK_IND` | DOUBLE |  |  | Format level page break indicator. |
| 35 | `PRESERVE_INTERP_IND` | DOUBLE | NOT NULL |  | 0 - Ignore RTF formatting for interpretive data in the printed chart. (Strip out plain text will occur.) 1 - Preserve RTF formatting for interpretive data in the printed chart. (Strip out plain text will NOT occur.) |
| 36 | `PROGRAM_NAME` | VARCHAR(100) |  |  | This is the actual program name of the facesheet. |
| 37 | `PRSNL_IDENT_FLAG` | DOUBLE |  |  | The personnel identifier for the chart format. This is used for corrected footnotes. |
| 38 | `REF_LAB_FLAG` | DOUBLE |  |  | Tells whether refrance lab footnotes are suppressed |
| 39 | `REF_LAB_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside the name of the procedure if it has been performed at a reference lab |
| 40 | `REPAGINATE_OFF_IND` | DOUBLE | NOT NULL |  | Indicator to NOT repaginate while printing charts. |
| 41 | `RESUBMIT_DISCLAIMER_ID` | DOUBLE | NOT NULL | FK→ | ID to the long_text table which contains the resubmit disclaimer. |
| 42 | `REVIEW_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that is defined to print beside the result if the result has been flagged for review |
| 43 | `RIGHT_MARGIN_NBR` | DOUBLE | NOT NULL |  | Stores the document image right margin to be applied |
| 44 | `SEX_AGE_CHANGE_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print beside the result if a change to age or sex has been made causing the reference ranges to change |
| 45 | `STAT_SYMBOL` | VARCHAR(1) |  |  | This is the symbol that will print next to the result of a procedure that has been ordered stat |
| 46 | `SUPPRESS_NA_IND` | DOUBLE | NOT NULL |  | the Suppress N/A Indicator |
| 47 | `TEMPLATE_LOC` | VARCHAR(255) |  |  | This is the location and name of the template portion of the chart format |
| 48 | `TIME_MASK` | VARCHAR(50) |  |  | This field stores time mask to be used to format all times within this chart format. |
| 49 | `UNIQUE_IDENT` | VARCHAR(60) |  |  | the Unique Identifier |
| 50 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 51 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 52 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 53 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 54 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDITIONAL_INFO_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RESUBMIT_DISCLAIMER_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (10)

| From table | Column |
|------------|--------|
| [CHART_FORMAT_CODES](CHART_FORMAT_CODES.md) | `CHART_FORMAT_ID` |
| [CHART_FORM_MM_FLDS](CHART_FORM_MM_FLDS.md) | `CHART_FORMAT_ID` |
| [CHART_FORM_SECTS](CHART_FORM_SECTS.md) | `CHART_FORMAT_ID` |
| [CHART_IMAGE_MM_FLDS](CHART_IMAGE_MM_FLDS.md) | `CHART_FORMAT_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `CHART_FORMAT_ID` |
| [CHART_TRIGGER](CHART_TRIGGER.md) | `CHART_FORMAT_ID` |
| [EXPEDITE_FORMAT](EXPEDITE_FORMAT.md) | `CHART_FORMAT_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `CHART_FORMAT_ID` |
| [EXPEDITE_PARAMS](EXPEDITE_PARAMS.md) | `CHART_FORMAT_ID` |
| [LOCATION](LOCATION.md) | `CHART_FORMAT_ID` |

