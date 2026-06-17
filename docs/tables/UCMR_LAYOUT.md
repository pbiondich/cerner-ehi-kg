# UCMR_LAYOUT

> Contains layouts for the unified report builder.

**Description:** Unified Case Manager Reference Layout  
**Table type:** REFERENCE  
**Primary key:** `UCMR_LAYOUT_ID`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Associates this layout with a specific activity type, which will be used to flex the layout properties and filter the selection of a layout. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `LAYOUT_NAME_CD` | DOUBLE | NOT NULL |  | The code value for the layout name. |
| 7 | `LAYOUT_RTF_ID` | DOUBLE | NOT NULL | FK→ | The long blob reference identifier that stores the layout RTF. |
| 8 | `PREV_UCMR_LAYOUT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the layout information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type of report this layout will define, which will be used to flex logic. |
| 10 | `UCMR_LAYOUT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a layout for the unified report builder. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `XML_FORMATTING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row on the long blob table that contains layout formatting information related to this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAYOUT_RTF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `XML_FORMATTING_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [UCMR_LAYOUT_FIELD](UCMR_LAYOUT_FIELD.md) | `UCMR_LAYOUT_ID` |
| [UCMR_LAYOUT_ORDERABLE_R](UCMR_LAYOUT_ORDERABLE_R.md) | `UCMR_LAYOUT_ID` |
| [UCM_REPORT](UCM_REPORT.md) | `UCMR_LAYOUT_ID` |

