# CHART_DEFINITION_HIST

> Defines a historical record of a chart for pediatric growth chart.

**Description:** Chart Definition History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Action Date and Time |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | This represents the sequence number of this entry. Part of Primary key. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Action Type Flag |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CHART_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | This will be the table's primary key. Also an FK from parent table. |
| 10 | `CHART_SOURCE_CD` | DOUBLE | NOT NULL |  | This identifies the source for the chart. |
| 11 | `CHART_TITLE` | VARCHAR(255) |  |  | This identifies the title of the chart. |
| 12 | `CHART_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of chart. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `MAX_AGE` | DOUBLE | NOT NULL |  | This identifies the maximum age in days for which the chart applies. |
| 15 | `MIN_AGE` | DOUBLE | NOT NULL |  | This identifies the minimum age in days for which the chart applies. |
| 16 | `SEX_CD` | DOUBLE | NOT NULL |  | This identifies the gender for which the chart applies. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VERSION` | VARCHAR(255) |  |  | This is the version name associated with this chart. |
| 23 | `X_AXIS_SECTION1_MAX_VAL` | DOUBLE | NOT NULL |  | This is the maximum value of the first section of the X axis. |
| 24 | `X_AXIS_SECTION1_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum value of the first section of the X axis. |
| 25 | `X_AXIS_SECTION1_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values in the first section of the X axis. |
| 26 | `X_AXIS_SECTION2_MAX_VAL` | DOUBLE |  |  | This is the maximum value of the second section of the X axis. |
| 27 | `X_AXIS_SECTION2_MIN_VAL` | DOUBLE |  |  | This is the minimum value of the second section of the X axis. |
| 28 | `X_AXIS_SECTION2_MULTIPLIER` | DOUBLE |  |  | This is the multiplier to indicate how section 1 values should relate to section 2 values. |
| 29 | `X_AXIS_SECTION2_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values in the second section of the X axis. |
| 30 | `X_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of measurement displayed on the x axis. |
| 31 | `Y_AXIS_MAX_VAL` | DOUBLE | NOT NULL |  | This is the maximum value on the Y axis. |
| 32 | `Y_AXIS_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum value on the Y axis. |
| 33 | `Y_AXIS_UNIT_CD` | DOUBLE | NOT NULL |  | This is the unit code of the values on the Y axis. |
| 34 | `Y_TYPE_CD` | DOUBLE | NOT NULL |  | This identifies the type of measurement displayed on the y axis. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_DEFINITION_ID` | [CHART_DEFINITION](CHART_DEFINITION.md) | `CHART_DEFINITION_ID` |

