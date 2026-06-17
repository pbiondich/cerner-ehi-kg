# OMF_VIEW_INDICATOR

> Indicators (typically columns) related to a view in omf_view which are filter_only indicators or indicators which have non-required joins in a view(_cd).

**Description:** Indicators (typically columns) related to a view in omf_view.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator code value. Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `REQUIRED_FILTER_IND` | DOUBLE |  |  | Indicates whether a filter is required for this indicator. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VIEW_CD` | DOUBLE | NOT NULL |  | View code value. Other codesets can be used besides 14265 depending on the team defining the value. |
| 9 | `VIEW_STR_SEQ1` | DOUBLE |  |  | Indicates the from/where clause required for this indicator. |
| 10 | `VIEW_STR_SEQ2` | DOUBLE |  |  | Indicates the from/where clause required for this indicator. |
| 11 | `VIEW_STR_SEQ3` | DOUBLE |  |  | Indicates the from/where clause required for this indicator. |
| 12 | `WEIGHT_COLUMN_STR` | VARCHAR(255) |  |  | Column name with table abbreviation attached. Used to point filter weight calculations to a parent table in the PowerVision View. in star schema, this would typically be the foreign key on the fact table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

