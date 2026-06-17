# SN_RPT_FIELD

> This table contains the size, stacking info, sort sequence, and various other font information about each field in a report.

**Description:** This table contains the field information for each report.  
**Table type:** REFERENCE  
**Primary key:** `RPT_FIELD_ID`  
**Columns:** 26  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BACK_COLOR_PCT` | DOUBLE | NOT NULL |  | Determines the back color for this field. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was first inserted. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the row to be created in the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 6 | `DISPLAY` | VARCHAR(255) | NOT NULL |  | Contains the display value of the field. |
| 7 | `DISPLAY_COL` | DOUBLE | NOT NULL |  | Determines which column this field displays in on the front-end application. |
| 8 | `DISPLAY_ROW` | DOUBLE | NOT NULL |  | Determines which row this field displays in on the front-end application. |
| 9 | `FIELD_SIZE` | DOUBLE | NOT NULL |  | Determines the number of columns that prints for this field. |
| 10 | `FONT_NUM` | DOUBLE | NOT NULL |  | Determines which font prints for this field. |
| 11 | `FONT_SIZE` | DOUBLE | NOT NULL |  | Determines the size of the font that prints for this field. |
| 12 | `FONT_UNDERLINE_IND` | DOUBLE | NOT NULL |  | Determines if this field is underlined or not. |
| 13 | `LINE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of line that surrounds this field. |
| 14 | `LINE_IND` | DOUBLE | NOT NULL |  | Determines if a '____' can be used as the value for this field. |
| 15 | `REPEAT_IND` | DOUBLE | NOT NULL |  | Determines if this field repeats within the report. This field must be sorted if the repeat_ind is equal to zero. |
| 16 | `RPT_FIELD_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 17 | `RPT_FIELD_REF_ID` | DOUBLE | NOT NULL |  | Foreign key into the SN_RPT_FIELD_REF table to line to the reference information for this field. |
| 18 | `RPT_SECT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key into the SN_RPT_SECT table to indicate which section this field is in. |
| 19 | `SORT_SEQ` | DOUBLE | NOT NULL |  | Determines the sequence that this field is sorted in for the entire report. This is only applicable to section types of 4 (Body). |
| 20 | `START_COL` | DOUBLE | NOT NULL |  | The column that printing starts in for this field. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `WRAP_IND` | DOUBLE | NOT NULL |  | Determines if this field has text wrap turned on or not. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_SECT_ID` | [SN_RPT_SECT](SN_RPT_SECT.md) | `RPT_SECT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_RPT_FIELD_SETTING](SN_RPT_FIELD_SETTING.md) | `RPT_FIELD_ID` |

