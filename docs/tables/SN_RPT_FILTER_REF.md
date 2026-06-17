# SN_RPT_FILTER_REF

> This table contains all of the filters associated with a given report type.

**Description:** SN RPT FILTER REF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | The display value for the filter. |
| 2 | `DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of control that will be used to collect information for this filter. For example: a provider control, list box, text box, etc. |
| 3 | `FILTER_DATA` | VARCHAR(255) |  |  | Contains miscellaneous information about the filter. For example it could contain information about which code set the filter values come from, or if the provider selection control should be limited to just physicians, or the actual values for this filter. |
| 4 | `FILTER_KEY` | VARCHAR(20) | NOT NULL |  | The unique key for this filter. This is a SurgiNet defined key that is used within the report scripts to identify this filter. |
| 5 | `FILTER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of filter that this is. |
| 6 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Determines if this filter is required to run the given report type. |
| 7 | `RPT_FILTER_REF_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `RPT_TYPE_CD` | DOUBLE | NOT NULL |  | Determines which report type these filters apply to. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

