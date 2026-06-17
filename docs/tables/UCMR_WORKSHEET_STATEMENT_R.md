# UCMR_WORKSHEET_STATEMENT_R

> This table stores statements associated with a worksheet.

**Description:** Unified Case Management Reference Worksheet Statement Relation  
**Table type:** REFERENCE  
**Primary key:** `UCMR_WORKSHEET_STATEMENT_R_ID`  
**Columns:** 25  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | A default for any coded list accepts. The code set of this default is determined by the code_set attribute. |
| 5 | `DEFAULT_NBR` | DOUBLE | NOT NULL |  | If the accept type is numeric, the default number will be stored here. If the type is checkbox, the value of 1 will be stored for True or 0 for false. |
| 6 | `DEFAULT_TXT` | VARCHAR(250) |  |  | A default for free text accept types. Also can store defaults for date accept types (e.g., current date) |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LABEL_TXT` | VARCHAR(250) |  |  | Text that appears on the protocol worksheet as the label for an accept prompt. |
| 9 | `LAYOUT_AREA_NAME` | VARCHAR(250) |  |  | Identifies the area of the statement as Input (INPUT), Output(OUTPUT) or Process (any other string). Worksheet Statements in Process area will either have LAYOUT or a unique spread name as a parent. |
| 10 | `NOTES_ID` | DOUBLE | NOT NULL | FK→ | Stores formatted rich text associated with a worksheet statement. |
| 11 | `ORDER_LEVEL_IND` | DOUBLE | NOT NULL |  | Indicates that this is an order level worksheet statement. |
| 12 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Set to True if the user must enter a value in the statement before the worksheet can be completed. |
| 13 | `UCMR_STATEMENT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the associated statement. |
| 14 | `UCMR_WORKSHEET_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier for the associated worksheet. |
| 15 | `UCMR_WORKSHEET_STATEMENT_R_ID` | DOUBLE | NOT NULL | PK | Identifies a unique relationship between a worksheet and a statement. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WORKSHEET_STMT_NAME` | VARCHAR(40) | NOT NULL |  | Contains the worksheet statement name. |
| 22 | `WORKSHEET_STMT_NAME_KEY` | VARCHAR(40) |  |  | Contains the worksheet statement name in uppercase with spaces removed. |
| 23 | `WORKSHEET_STMT_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | WORKSHEET_STMT_NAME_KEY_A_NLS column |
| 24 | `WORKSHEET_STMT_NAME_KEY_NLS` | VARCHAR(82) |  |  | Stores the corresponding non-English character set value for the worksheet statement name. |
| 25 | `XML_FORMATTING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field stores statement formatting information in an xml blob. This information may include font, bold, calculation formula or any other information pertaining the statement within a worksheet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTES_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `UCMR_WORKSHEET_ID` | [UCMR_WORKSHEET](UCMR_WORKSHEET.md) | `UCMR_WORKSHEET_ID` |
| `XML_FORMATTING_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |
| [UCMR_WS_STMT_ASSAY_R](UCMR_WS_STMT_ASSAY_R.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |
| [UCMR_WS_STMT_VALIDATION](UCMR_WS_STMT_VALIDATION.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |
| [UCM_PTL_RESULT](UCM_PTL_RESULT.md) | `UCMR_WORKSHEET_STATEMENT_ID` |

