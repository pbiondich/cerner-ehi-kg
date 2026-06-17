# UCMR_LAYOUT_FIELD

> Stores a layou field for the unified report builder.

**Description:** Unified Case Manager Reference Layout Field  
**Table type:** REFERENCE  
**Primary key:** `UCMR_LAYOUT_FIELD_ID`  
**Columns:** 29  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ALLOW_CAPTION_IND` | DOUBLE | NOT NULL |  | Indicates whether to allow captions for Image Type fields. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CERNER_DEFINED_CD` | DOUBLE | NOT NULL |  | Identifies the source Cerner Defined element of a case field. |
| 6 | `COLUMN_CNT` | DOUBLE | NOT NULL |  | Indicates the number of columns to occupy when inserting images. |
| 7 | `DEVICE_ALIAS_NAME` | VARCHAR(40) |  |  | Stores the field name of an external device's result. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FIELD_DESC_TXT` | VARCHAR(60) |  |  | Non unique description for this field. |
| 10 | `FIELD_HEADER_TXT` | VARCHAR(40) |  |  | Header that displays with field in layout. |
| 11 | `FIELD_NAME` | VARCHAR(40) |  |  | Name for this field that will be unique within the layout. |
| 12 | `FIELD_OPTION_FLAG` | DOUBLE | NOT NULL |  | Indicates whether to require field, suppress field, or allow missing data value. 0 - Allow Missing Data Value 1 - Required Field 2 - Suppress Field |
| 13 | `FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to identify the type of the field. 0 - Case 1 - Edit 2 - Supplemental |
| 14 | `MISSING_DATA_VALUE_TXT` | VARCHAR(40) |  |  | Displays in a field when no data is present from the source. |
| 15 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | Identifies the source Order Entry Field element of a case field. |
| 16 | `PREVIEW_DATA_VALUE_TXT` | VARCHAR(40) |  |  | Displays in a field at build time. |
| 17 | `PREV_UCMR_LAYOUT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the field information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 18 | `REFERENCE_TYPE_CD` | DOUBLE | NOT NULL |  | If this field is a reference field, this will store the type of data that will be displayed in the reference field. |
| 19 | `RELATED_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Associates one layout field to another layout field. |
| 20 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the source of the data the field displays. |
| 21 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Identifies the source task assay of a case field. |
| 22 | `UCMR_LAYOUT_FIELD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a stored layout field for unified report builder. |
| 23 | `UCMR_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the parent layout for this field. |
| 24 | `UCMR_WORKSHEET_STATEMENT_R_ID` | DOUBLE | NOT NULL | FK→ | Identifies the source worksheet statement of a case field. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_UCMR_LAYOUT_FIELD_ID` | [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |
| `RELATED_FIELD_ID` | [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |
| `UCMR_LAYOUT_ID` | [UCMR_LAYOUT](UCMR_LAYOUT.md) | `UCMR_LAYOUT_ID` |
| `UCMR_WORKSHEET_STATEMENT_R_ID` | [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [SIGN_LINE_LAYOUT_FIELD_R](SIGN_LINE_LAYOUT_FIELD_R.md) | `UCMR_LAYOUT_FIELD_ID` |
| [UCMR_DSR_FIELD_COLUMN](UCMR_DSR_FIELD_COLUMN.md) | `UCMR_LAYOUT_FIELD_ID` |
| [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `PREV_UCMR_LAYOUT_FIELD_ID` |
| [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `RELATED_FIELD_ID` |
| [UCMR_LAYOUT_FIELD_TMPLT_R](UCMR_LAYOUT_FIELD_TMPLT_R.md) | `UCMR_LAYOUT_FIELD_ID` |
| [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |

