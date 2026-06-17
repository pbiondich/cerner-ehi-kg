# PCS_RSLT_LAYOUT

> This table identifies a result layout which contains a list of event codes, lookback scope and optional formatting for retrieving patient results.

**Description:** PathNet Common Services Result Layout  
**Table type:** REFERENCE  
**Primary key:** `PCS_RSLT_LAYOUT_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CUSTOM_SCRIPT_NAME` | VARCHAR(100) |  |  | This is used to save the custom script name which is entered from template. There can be different script for each different template. The custom script will be executed from pcs_get_grid_pat_rslts and the output will be displayed in a report. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LOOKBACK_DAYS_NBR` | DOUBLE | NOT NULL |  | The number of days to look back when performing the result query. (Numeric value between 1 and 999) |
| 6 | `MAX_RESULTS_NBR` | DOUBLE | NOT NULL |  | The maximum number of result sets to return for each layout group. (Numeric value between 1 and 9) |
| 7 | `PCS_RSLT_LAYOUT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a result layout which contains a list of event codes, lookback scope, and optional formatting for retrieving patient results. |
| 8 | `PREV_PCS_RSLT_LAYOUT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the PCS Result Layout information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RSLT_LAYOUT_DESC` | VARCHAR(100) | NOT NULL |  | The description of what the result layout contains. |
| 10 | `RSLT_LAYOUT_NAME` | VARCHAR(100) | NOT NULL |  | Contains the Name of the Result Layout. |
| 11 | `RSLT_LAYOUT_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Contains the name of the result layout in all capitals and all special characters removed. |
| 12 | `SORT_ORDER_FLAG` | DOUBLE | NOT NULL |  | Defines how the result sets will be sorted within each layout group. 0 = Ascending; 1 = Descending |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PCS_LAYOUT_GROUP](PCS_LAYOUT_GROUP.md) | `PCS_RSLT_LAYOUT_ID` |
| [PCS_RSLT_TMPLT_DFLT](PCS_RSLT_TMPLT_DFLT.md) | `PCS_RSLT_LAYOUT_ID` |
| [WP_TEMPLATE_TEXT](WP_TEMPLATE_TEXT.md) | `PCS_RSLT_LAYOUT_ID` |

