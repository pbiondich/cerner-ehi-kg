# SECTION_ATTRIBUTE

> The Section Attribute defines the subject area detail attributes that are defined by the section.

**Description:** Section Attribute  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COLUMN_NUM` | DOUBLE | NOT NULL |  | Defines the column that the attribute is displayed. |
| 7 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | Defines the order of the attributes within the column. |
| 8 | `DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the attribute as a literal or a codified attribute. |
| 9 | `DETAIL_VALUE` | VARCHAR(255) |  |  | The value of the literal. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `HEIGHT` | DOUBLE |  |  | Not Used. |
| 12 | `OUTPUT_MASK` | VARCHAR(50) |  |  | Not Used. |
| 13 | `ROW_NUM` | DOUBLE | NOT NULL |  | Not Used. |
| 14 | `SECTION_ID` | DOUBLE | NOT NULL |  | Unique identifier for the section table. |
| 15 | `SEP_STRING` | CHAR(18) |  |  | Not Used. |
| 16 | `SEP_STR_LENGTH` | DOUBLE |  |  | Not Used. |
| 17 | `SORT_DIRECTION_CD` | DOUBLE | NOT NULL |  | Not Used. |
| 18 | `SUBJ_AREA_DTL_CD` | DOUBLE | NOT NULL |  | Defines the codified attribute. |
| 19 | `TRIM_CHAR` | CHAR(1) |  |  | Not Used. |
| 20 | `TRIM_TYPE_CD` | DOUBLE | NOT NULL |  | Not Used. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `WIDTH` | DOUBLE |  |  | Defines the width of a column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

