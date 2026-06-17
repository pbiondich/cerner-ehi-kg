# UCM_DSR_PANEL_INFO

> Stores panel information about a set of variant results for an order.

**Description:** Unified Case Manager Document Sequencing Results Panel Info  
**Table type:** ACTIVITY  
**Primary key:** `UCM_DSR_PANEL_INFO_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CORRECTED_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the variant is capable of being pulled into Document Case Report. When a variant is marked as reportable and corrected the value will be 1. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `LAST_RPT_UPDT_DT_TM` | DATETIME |  |  | The last date and time the set of reportable variants was corrected. |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order (i.e., panel) used to obtain this variant result. |
| 8 | `PREV_UCM_DSR_PANEL_INFO_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the DSR panel group information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `SORT_COLUMN_CD` | DOUBLE |  |  | Determines the column by which sort has to be applied on variants. |
| 10 | `SORT_FLAG` | DOUBLE |  |  | Determines the way in which the sort has to be applied on variants. 0 - no sort 1 - ascending order 2 - descendng order |
| 11 | `UCM_DSR_PANEL_INFO_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies panel information about a set of variant results for an order. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PREV_UCM_DSR_PANEL_INFO_ID` | [UCM_DSR_PANEL_INFO](UCM_DSR_PANEL_INFO.md) | `UCM_DSR_PANEL_INFO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_DSR_PANEL_INFO](UCM_DSR_PANEL_INFO.md) | `PREV_UCM_DSR_PANEL_INFO_ID` |

