# CHART_VERT_FORMAT

> chart vertical format

**Description:** This table defines attributes for vertical section formatting  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNML_HILITE_FLAG` | DOUBLE |  |  | This field identifies the type of highlighting that is used for abnormal results |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This is a number which uniquely identifies a chart group |
| 7 | `CRIT_HILITE_FLAG` | DOUBLE |  |  | This field identifies the type of highlighting used for a critical result |
| 8 | `DATE_FORMAT_CD` | DOUBLE | NOT NULL |  | This code identifies the format that should be used when printing the date |
| 9 | `DATE_LBL` | VARCHAR(32) |  |  | This is the label that should print for the date |
| 10 | `DATE_MASK` | VARCHAR(50) |  |  | This field stores a date mask to be used on all date within this group. |
| 11 | `DATE_ORDER` | DOUBLE |  |  | This is the order in which the date should print |
| 12 | `ENCNTR_ALIAS_LBL` | VARCHAR(32) |  |  | encounter alias column label |
| 13 | `ENCNTR_ALIAS_ORDER` | DOUBLE |  |  | the order of encounter alias column |
| 14 | `FLOWSHEET_IND` | DOUBLE |  |  | This tells us if the user selected Vertical section or Vertical Flowsheet section. |
| 15 | `FTNOTE_LOC_FLAG` | DOUBLE |  |  | This is the location where footnotes should print |
| 16 | `INTERP_LOC_FLAG` | DOUBLE |  |  | This is the location where the interpretive data should print |
| 17 | `PERFID_LBL` | VARCHAR(32) |  |  | This is the label that should print to identify the performed_id |
| 18 | `PERFID_LBL_ORDER` | DOUBLE |  |  | This defines the order that the performed_id label should display on the format. |
| 19 | `PERFID_LBL_POS` | DOUBLE |  |  | This defines the position of the performed_id label (i.e. right side or left side) |
| 20 | `REFER_LBL_ORDER` | DOUBLE |  |  | This defines the order that the reference range label should print |
| 21 | `REFER_LBL_POS` | DOUBLE |  |  | This defines the position of the reference range label (i.e. right side or left side) |
| 22 | `REF_RANGE_LBL` | VARCHAR(32) |  |  | This defines what should print on the chart as the reference range label |
| 23 | `REF_RNG_FORM_FLAG` | DOUBLE |  |  | This is the format that the reference range should use to print |
| 24 | `RESLT_START_COL` | DOUBLE |  |  | This field is not used at this time |
| 25 | `RSLT_SEQ_FLAG` | DOUBLE |  |  | This is the order that the results should print in (newest to oldest or oldest to newest) |
| 26 | `STAYDAYS_FORM_FLAG` | DOUBLE |  |  | This is the format in which the day of stay should print |
| 27 | `STAYDAYS_LBL` | VARCHAR(32) |  |  | This is the label that should print for the day of stay field |
| 28 | `STAYDAYS_ORDER` | DOUBLE |  |  | This is the order in which the day of stay field should print |
| 29 | `TEST_LBL` | VARCHAR(32) |  |  | This is the label that should print to identify the procedure |
| 30 | `TEST_LBL_ORDER` | DOUBLE |  |  | This field identifies the order in which the test should print |
| 31 | `TEST_LBL_POS` | DOUBLE |  |  | This field defines where the test name and label will print on the chart (right side or left side) |
| 32 | `TIME_FORMAT_FLAG` | DOUBLE |  |  | This field identifies the format that is used when printing the time on the chart |
| 33 | `TIME_LBL` | VARCHAR(32) |  |  | This is the label that should print for the time on the chart |
| 34 | `TIME_MASK` | VARCHAR(32) |  |  | This field stores time mask used to format all times within this group. |
| 35 | `TIME_ORDER` | DOUBLE |  |  | This is the order in which the time should print |
| 36 | `UNITS_LBL` | VARCHAR(32) |  |  | This is the label that should be printed on the chart for the units |
| 37 | `UNITS_LBL_ORDER` | DOUBLE |  |  | This is the order in which the units and the label should print |
| 38 | `UNITS_LBL_POS` | DOUBLE |  |  | This is the position in which the units should print on the chart (right side or left side) |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

