# INTERP_COMPONENT

> The discrete task assays that should be used to create interpretation.

**Description:** Interpretation Component  
**Table type:** REFERENCE  
**Primary key:** `INTERP_DETAIL_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CROSS_DRAWN_DT_TM_IND` | DOUBLE |  |  | The value of this indicator will be a 1 if the interpretation should be made across different drawn dates and times for the specimens used in the testing. The value of this indicator will be a 0 if the interpretation should only be made across the same drawn dates and times for the specimens used in the testing. |
| 6 | `INCLUDED_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This column is the code value that represents the discrete task assay that is included in the interpretation pattern. |
| 7 | `INTERP_DETAIL_ID` | DOUBLE | NOT NULL | PK | This is a unique number that identifies the interpretation detail. |
| 8 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | This column is a unique number that identifies the interpretation. |
| 9 | `RESULT_REQ_FLAG` | DOUBLE |  |  | This column determines whether a result for the component of the interpretation is required or not, for the pattern to be valid. |
| 10 | `SEQUENCE` | DOUBLE |  |  | A sequence number used to list and display the components of the interpretation pattern in the correct sequence. |
| 11 | `TIME_WINDOW_MINUTES` | DOUBLE |  |  | The number of minutes defined for the time window in which this interpretation can be made. |
| 12 | `TIME_WINDOW_UNITS_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the time window (ex. "Days"). |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERIFIED_FLAG` | DOUBLE |  |  | This flag determines whether the components of the interpretation have to be verified or not, for the interpretation to be valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INCLUDED_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `INTERP_ID` | [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `INTERP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [INTERP_RANGE](INTERP_RANGE.md) | `INTERP_DETAIL_ID` |
| [RESULT_HASH](RESULT_HASH.md) | `INTERP_DETAIL_ID` |

