# RAD_TECH_FORMAT

> The Rad_Tech_Format table holds individual radiology technical comment formats.

**Description:** Radiology Technical Comment Formats  
**Table type:** REFERENCE  
**Primary key:** `FORMAT_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FIELD_FORMAT_IND` | DOUBLE | NOT NULL |  | The field_format_ind states if this format is tied to one field or if it is an actual format. 0 = Actual Format, 1 = Field Format |
| 6 | `FORMAT_DESC` | VARCHAR(60) | NOT NULL |  | The format description names a radiology technical comment format. |
| 7 | `FORMAT_DESC_A_NLS` | VARCHAR(240) |  |  | The NLS key for searching in all non-English locales. |
| 8 | `FORMAT_ID` | DOUBLE | NOT NULL | PK | The Format_Id uniquely identifies a row in the Rad_Tech_Format table. It serves no other purpose other than to uniquely identify the row . |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_TECH_FLD_FMT_R](RAD_TECH_FLD_FMT_R.md) | `FORMAT_ID` |
| [RAD_TECH_FMT_ERPRC_R](RAD_TECH_FMT_ERPRC_R.md) | `FORMAT_ID` |

