# REF_DATASTATS_HIST

> Defines a historical record of statistical measures for a particular range on a growth chart.

**Description:** Reference Data Statistics History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Action Date Time |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | This represents the sequence number of this entry. Part of Primary Key. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Action Type Flag |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BOX_COX_POWER_VALUE` | DOUBLE |  |  | This is the 'power in the Box-Cox transformation' for the population as given by the source of the chart information. (This is the L in the CDC's LMS parameters.) |
| 10 | `CHART_DEFINITION_ID` | DOUBLE | NOT NULL |  | This is the foreign key to the CHART_DEFINITION table. Each data point belongs to exactly one dataset. |
| 11 | `COEFFNT_VAR_VALUE` | DOUBLE |  |  | This is the generalized coefficient of variation value for the population as given by the source of the chart information. (This is the S in the CDC's LMS parameters.) |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `MEAN_VALUE` | DOUBLE |  |  | This is the mean value for the population as given by the source of the chart information. |
| 14 | `MEDIAN_VALUE` | DOUBLE |  |  | This is the median value for the population as given by the source of the chart information. (This is the M in the CDC's LMS parameters.) |
| 15 | `REF_DATASTATS_ID` | DOUBLE | NOT NULL | FK→ | This will be the table's primary key. Foreign Key from REF_DATASTATS |
| 16 | `STD_DEV_VALUE` | DOUBLE |  |  | This is the standard deviation for the population as given by the source of the chart information. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `X_MAX_VAL` | DOUBLE | NOT NULL |  | This is the maximum val on the X axis for which the stats apply. Units are in the unit_cd of the X axis on the CHART_DEFINITION table. |
| 23 | `X_MIN_VAL` | DOUBLE | NOT NULL |  | This is the minimum val on the X axis for which the stats apply. Units are in the unit_cd of the X axis on the CHART_DEFINITION table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REF_DATASTATS_ID` | [REF_DATASTATS](REF_DATASTATS.md) | `REF_DATASTATS_ID` |

