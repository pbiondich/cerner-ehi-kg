# EEM_ABN_FORM

> EEM ABN Form

**Description:** This table is used to denote any ABN form that was printed  
**Table type:** ACTIVITY  
**Primary key:** `ABN_FORM_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_FORM_ID` | DOUBLE | NOT NULL | PK FK→ | ABN Form Identifier |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `EEM_REPORT_ID` | DOUBLE | NOT NULL | FK→ | EEM Report Identifier |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FILE_NAME` | VARCHAR(255) |  |  | File Name |
| 10 | `NBR_COPIES` | DOUBLE | NOT NULL |  | Requested Number of Copies |
| 11 | `OFFLINE_FORM_IND` | DOUBLE | NOT NULL |  | Offline Form Indicator |
| 12 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | Output Destination Identifier |
| 13 | `SUFFIX` | VARCHAR(50) |  |  | Suffix |
| 14 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Identifier |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABN_FORM_ID` | [EEM_ABN_ACTION](EEM_ABN_ACTION.md) | `ABN_ACTION_ID` |
| `EEM_REPORT_ID` | [SCH_REPORT](SCH_REPORT.md) | `SCH_REPORT_ID` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EEM_ABN_ACTION](EEM_ABN_ACTION.md) | `ABN_FORM_ID` |

