# UCM_REPORT_FIELD

> Stores activity data for Document Case Report application

**Description:** Unified Case Manager - Report Field  
**Table type:** ACTIVITY  
**Primary key:** `UCM_REPORT_FIELD_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `OD_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence of the order detail data for this field. |
| 6 | `OD_DETAIL_SEQ` | DOUBLE | NOT NULL |  | The detail sequence of the order detail data for this field. |
| 7 | `OD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the source order of the order detail data for this field. |
| 8 | `PREV_UCM_REPORT_FIELD_ID` | DOUBLE | NOT NULL |  | Used to track versions of the report field information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | If populated, identifies the source result for this field. |
| 10 | `UCMR_LAYOUT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | Identifies the layout field reference for this report field. |
| 11 | `UCM_PTL_RESULT_ID` | DOUBLE | NOT NULL | FK→ | If populated, identifies the source protocol result for this field. |
| 12 | `UCM_REPORT_FIELD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies activity data for Document Case Report application. |
| 13 | `UCM_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the activity report for this field. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |
| `UCMR_LAYOUT_FIELD_ID` | [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_FIELD_ID` |
| `UCM_PTL_RESULT_ID` | [UCM_PTL_RESULT](UCM_PTL_RESULT.md) | `UCM_PTL_RESULT_ID` |
| `UCM_REPORT_ID` | [UCM_REPORT](UCM_REPORT.md) | `UCM_REPORT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCM_KARYOTYPE](UCM_KARYOTYPE.md) | `UCM_REPORT_FIELD_ID` |
| [UCM_RPT_FIELD_IMAGE](UCM_RPT_FIELD_IMAGE.md) | `UCM_REPORT_FIELD_ID` |

