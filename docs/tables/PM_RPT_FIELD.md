# PM_RPT_FIELD

> Reference table containing all the attributes usable in PM reporting. These rows are your pick lists for headers, filters, and orders.

**Description:** Reference table containing all the attributes usable in PM reporting  
**Table type:** REFERENCE  
**Primary key:** `FIELD_ID`  
**Columns:** 23  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE |  |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the data_status_cd to be set or change. |
| 9 | `DISPLAY_LENGTH` | DOUBLE | NOT NULL |  | This is the recommended default length for this field |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FIELD_DISPLAY` | CHAR(32) |  |  | Text display for the field name |
| 12 | `FIELD_HELP` | CHAR(6) |  |  | Determines what Code Set will be used as help behind this field |
| 13 | `FIELD_ID` | DOUBLE | NOT NULL | PK | Primary Key attribute |
| 14 | `FIELD_NAME` | CHAR(32) | NOT NULL |  | Name of this field as defined in the data dictionary |
| 15 | `FIELD_REPORT_TYPE` | CHAR(1) | NOT NULL |  | Defines the type of report these fields are valid for. Valid values are T = Transaction, C = Census, M = Miscellaenous, and K = Current Case, O = OPF Matches, P = OPF Population, X = OPF Combine, A = AFC |
| 16 | `FIELD_TYPE` | CHAR(4) | NOT NULL |  | Definition of the field. Valid values are DQ8, F8, I2, I4, and C***. |
| 17 | `KEY_IND` | DOUBLE |  |  | Tells whether this field is a key or not |
| 18 | `TABLE_NAME` | CHAR(32) | NOT NULL |  | The table that this field came from as specificied in the data dictionary |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PM_RPT_FILTER](PM_RPT_FILTER.md) | `FIELD_ID` |
| [PM_RPT_GROUP](PM_RPT_GROUP.md) | `FIELD_ID` |
| [PM_RPT_HEADER](PM_RPT_HEADER.md) | `FIELD_ID` |
| [PM_RPT_ORDER](PM_RPT_ORDER.md) | `FIELD_ID` |

