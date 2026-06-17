# CHART_DEFINITION

> Defines a chart for pediatric growth chart.

**Description:** Chart definition  
**Table type:** REFERENCE  
**Primary key:** `CHART_DEFINITION_ID`  
**Columns:** 32  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHART_DEFINITION_ID` | DOUBLE | NOT NULL | PK | This will be the tables primary key. |
| 7 | `CHART_SOURCE_CD` | DOUBLE | NOT NULL |  | This identifies the source for the chart. |
| 8 | `CHART_TITLE` | VARCHAR(255) |  |  | This identifies the title of the chart. |
| 9 | `CHART_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of chart. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This represent the sequence number of the last entry in CHART_DEFINITION_HIST. |
| 12 | `MAX_AGE` | DOUBLE | NOT NULL |  | This identifies the maximum age in days for which the chart applies. |
| 13 | `MIN_AGE` | DOUBLE | NOT NULL |  | This identifies the minimum age in days for which the chart applies. |
| 14 | `SEX_CD` | DOUBLE | NOT NULL |  | This identifies the gender for which the chart applies. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERSION` | VARCHAR(255) |  |  | This is the version name associated with this chart. |
| 21 | `X_AXIS_SECTION1_MAX_VAL` | DOUBLE | NOT NULL |  | This is the maximum value of the first section of the X axis. |
| 22 | `X_AXIS_SECTION1_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum value of the first section of the X axis. |
| 23 | `X_AXIS_SECTION1_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values in the first section of the X axis. |
| 24 | `X_AXIS_SECTION2_MAX_VAL` | DOUBLE |  |  | This is the maximum value of the second section of the X axis. |
| 25 | `X_AXIS_SECTION2_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum value of the second section of the X axis. |
| 26 | `X_AXIS_SECTION2_MULTIPLIER` | DOUBLE |  |  | This is the multiplier to indicate how section 1 values should relate to section 2 values. |
| 27 | `X_AXIS_SECTION2_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values in the second section of the X axis. |
| 28 | `X_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of measurement displayed on the x axis. |
| 29 | `Y_AXIS_MAX_VAL` | DOUBLE | NOT NULL |  | This is the maximum value on the Y axis. |
| 30 | `Y_AXIS_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum value on the Y axis. |
| 31 | `Y_AXIS_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values on the Y axis. |
| 32 | `Y_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of measurement displayed on the y axis. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CHART_DEFINITION_HIST](CHART_DEFINITION_HIST.md) | `CHART_DEFINITION_ID` |
| [REF_DATASET](REF_DATASET.md) | `CHART_DEFINITION_ID` |
| [REF_DATASTATS](REF_DATASTATS.md) | `CHART_DEFINITION_ID` |

