# ADVANCED_DELTA

> Stores parameters used for advanced delta checking for General Lab applications

**Description:** Advanced Delta Checking  
**Table type:** REFERENCE  
**Primary key:** `ADVANCED_DELTA_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADVANCED_DELTA_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific advanced delta check row. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DELTA_CHECK_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific type of delta checking (such as absolute, percent, and so on). |
| 8 | `DELTA_HIGH` | DOUBLE |  |  | Stores the value for the high end of the range for delta checking. |
| 9 | `DELTA_IND` | DOUBLE | NOT NULL |  | Stores the indicator that is used to determine whether a delta checking range has been entered. Valid values are 0 - no range, 1 - low value only, 2 - high value only, 3 - both low and high values. |
| 10 | `DELTA_LOW` | DOUBLE |  |  | Used to store the value for the low range to be used for delta checking. |
| 11 | `DELTA_MINUTES` | DOUBLE |  |  | Defines the number of minutes used to evaluate the delta check rule. |
| 12 | `DELTA_VALUE` | DOUBLE |  |  | Defines the value used to evaluate delta checking. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific reference range associated with the advanced delta checking parameters. Creates a relationship to the reference range factor table. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERFORM_RESULT](PERFORM_RESULT.md) | `ADVANCED_DELTA_ID` |

