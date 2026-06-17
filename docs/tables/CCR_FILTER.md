# CCR_FILTER

> Defines the applicable filter types for content types in a view.

**Description:** Filter  
**Table type:** REFERENCE  
**Primary key:** `FILTER_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_MULTIPLE_IND` | DOUBLE | NOT NULL |  | Determines if this filter may have multiple values associated to it. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CODE_SET_VALUE` | DOUBLE | NOT NULL |  | If the filter type is code set, specifies the code set the filter values originate from. |
| 5 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the content type this filter supports. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FILTER_ID` | DOUBLE | NOT NULL | PK | Identifies the current filter definition. FK from ccr_filter |
| 8 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies what this filter is. |
| 9 | `FILTER_VALUE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of value this filter represents. |
| 10 | `PREV_FILTER_ID` | DOUBLE | NOT NULL |  | Previoius Filter Id - required for versioning |
| 11 | `SRC_TABLE_NAME` | VARCHAR(40) | NOT NULL |  | Identifies the source table for the value of this filter. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CCR_FILTER_VALUE](CCR_FILTER_VALUE.md) | `FILTER_ID` |

