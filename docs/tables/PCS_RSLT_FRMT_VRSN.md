# PCS_RSLT_FRMT_VRSN

> This table identifies a version of the presentation format of a result layout.

**Description:** PathNet Common Services Result Format Version  
**Table type:** REFERENCE  
**Primary key:** `PCS_RSLT_FRMT_VRSN_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `NO_RSLT_FOUND_IND` | DOUBLE |  |  | Indicates that additional text should be included if no result is found for the fill group event. |
| 5 | `NO_RSLT_FOUND_TEXT` | VARCHAR(40) |  |  | Defines the text to use when no result is found for the fill group event. |
| 6 | `PCS_RESULT_FORMAT_CD` | DOUBLE | NOT NULL |  | The unique identifier for the result layout format code. |
| 7 | `PCS_RSLT_FRMT_VRSN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a version of the presentation format of a result layout. |
| 8 | `PREV_PCS_RSLT_FRMT_VRSN_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS result format version information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `REVISION_DT_TM` | DATETIME | NOT NULL |  | The revision date and time for the result layout format. |
| 10 | `RSLT_FRMT_VRSN_DESC` | VARCHAR(100) | NOT NULL |  | Contains the description of the result format version. |
| 11 | `RSLT_LAYOUT_FOOTER_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the long text record containing the formatted text that defines the format footer. |
| 12 | `RSLT_LAYOUT_HEADER_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the long text row containing the formatted text that defines the format header. |
| 13 | `RSLT_SET_FOOTER_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the long text row containing the formatted text that that defines the result set footer. |
| 14 | `RSLT_SET_HEADER_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the long text row containing the formatted text that defines the result set header. |
| 15 | `RSLT_SET_ROW_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the long text row containing the formatted text that defines the result set row. |
| 16 | `TABLE_WIDTH_NBR` | DOUBLE | NOT NULL |  | Indicates the width required for the table. |
| 17 | `TEXT_RSLT_IND` | DOUBLE |  |  | Indicates that when a textual result is found for a fill gourp event replacement text should be included in the result cell. |
| 18 | `TEXT_RSLT_TEXT` | VARCHAR(40) |  |  | Defines the text to use in the result cell when a text result is found for a fill group event. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PCS_FRMT_VRSN_ELEMENT](PCS_FRMT_VRSN_ELEMENT.md) | `PCS_RSLT_FRMT_VRSN_ID` |
| [PCS_RSLT_TMPLT_DFLT](PCS_RSLT_TMPLT_DFLT.md) | `PCS_RSLT_FRMT_VRSN_ID` |
| [WP_TEMPLATE_TEXT](WP_TEMPLATE_TEXT.md) | `PCS_RSLT_FRMT_VRSN_ID` |

