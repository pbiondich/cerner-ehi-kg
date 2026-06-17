# DM_STAT_SNAPS_VALUES

> Name value pair table for generically storing database statistics. This is an activity table.

**Description:** Statistical Snapshot Values  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_STAT_SNAP_ID` | DOUBLE | NOT NULL | FK→ | The snapshot id from the DM_STAT_SNAPS table. |
| 2 | `STAT_CLOB_VAL` | LONGTEXT |  |  | stat clob value |
| 3 | `STAT_DATE_DT_TM` | DATETIME |  |  | Used to store the statistic value if a date. STAT_TYPE will be set to 3 if this column is populated. |
| 4 | `STAT_NAME` | VARCHAR(80) | NOT NULL |  | Name of the statistic captured. |
| 5 | `STAT_NUMBER_VAL` | DOUBLE |  |  | Used to store the statistic value if a number. STAT_TYPE will be set to 1 if this column is populated. |
| 6 | `STAT_SEQ` | DOUBLE | NOT NULL |  | Used to indicate time periods if this parameter can have multiple values for a single date. |
| 7 | `STAT_STR_VAL` | VARCHAR(255) |  |  | Used to store the statistic value if a string. STAT_TYPE will be set to 2 if this column is populated. |
| 8 | `STAT_TYPE` | DOUBLE | NOT NULL |  | Used to indicate the data type for the statistic. A value of 1 indicates that the STAT_NUMBER_VAL is populated. 2 indicates that the STAT_STR_VAL is populated. 3 indicates that the STAT_DATE_DT_TM is populated. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_STAT_SNAP_ID` | [DM_STAT_SNAPS](DM_STAT_SNAPS.md) | `DM_STAT_SNAP_ID` |

