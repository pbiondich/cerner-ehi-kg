# PCS_RSLT_TMPLT_DFLT

> This table identifies defaults to be applied to word processing templates that include the result layout.

**Description:** PathNet Common Services Result Template Default  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `NO_RESULTS_TEXT` | VARCHAR(250) | NOT NULL |  | Text defined to display if no results are found for the result layout. |
| 5 | `NO_RESULTS_TEXT_IND` | DOUBLE | NOT NULL |  | Indicates whether text has been defined to include if no results are found for the result layout. |
| 6 | `PCS_RSLT_FRMT_VRSN_ID` | DOUBLE | NOT NULL | FK→ | Defines the default format version that will be applied to the result layout in the word processing template. |
| 7 | `PCS_RSLT_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related result layout. |
| 8 | `PCS_RSLT_TMPLT_DFLT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the defaults to be applied to word processing templates that include the result layout. |
| 9 | `PREV_PCS_RSLT_TMPLT_DFLT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS Result Template Default information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `TEXT_DISPLAY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the text to display for the result layout within the word processing template. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCS_RSLT_FRMT_VRSN_ID` | [PCS_RSLT_FRMT_VRSN](PCS_RSLT_FRMT_VRSN.md) | `PCS_RSLT_FRMT_VRSN_ID` |
| `PCS_RSLT_LAYOUT_ID` | [PCS_RSLT_LAYOUT](PCS_RSLT_LAYOUT.md) | `PCS_RSLT_LAYOUT_ID` |
| `TEXT_DISPLAY_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

