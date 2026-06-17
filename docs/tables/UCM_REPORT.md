# UCM_REPORT

> Stores activity data for Document Case Report application

**Description:** Unified Case Manager - Report  
**Table type:** ACTIVITY  
**Primary key:** `UCM_REPORT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LAST_REFRESH_DT_TM` | DATETIME | NOT NULL |  | The date and time of when the field data was last refreshed. |
| 6 | `LAYOUT_VERSION_DT_TM` | DATETIME | NOT NULL |  | Used with ucmr_layout_id to identify the correct layout version for this activity record. |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the corresponding order for this report. |
| 8 | `PREV_UCM_REPORT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the report information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `REPORT_RTF_ID` | DOUBLE | NOT NULL | FK→ | The long blob identifier which sotres the layout RTF. |
| 10 | `UCMR_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the reference layout for this report. |
| 11 | `UCM_REPORT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies activity data for Document Case Report application. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REPORT_RTF_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `UCMR_LAYOUT_ID` | [UCMR_LAYOUT](UCMR_LAYOUT.md) | `UCMR_LAYOUT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `UCM_REPORT_ID` |

