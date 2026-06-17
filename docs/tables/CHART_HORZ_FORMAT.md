# CHART_HORZ_FORMAT

> chart horizontal format

**Description:** This table defines the attributes for a horizontal section type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNML_HILITE_FLAG` | DOUBLE |  |  | This defines the type of highlighting that should be used for abnormal results |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This is a unique number that identifies the chart group |
| 7 | `CRIT_HILITE_FLAG` | DOUBLE |  |  | This defines the type of highlighting that should be used for critical results |
| 8 | `DATE_FORMAT_CD` | DOUBLE | NOT NULL |  | This defines the way the date will be formatted |
| 9 | `DATE_MASK` | VARCHAR(50) |  |  | This field stores a date mask to be used on all date within this group |
| 10 | `DATE_ORDER` | DOUBLE |  |  | This defines in which order the date will print |
| 11 | `ENCNTR_ALIAS_ORDER` | DOUBLE |  |  | the order of encounter alias column |
| 12 | `FLOWSHEET_IND` | DOUBLE |  |  | This identifies if the user selected Horizontal section or Horizontal Flowsheet section. |
| 13 | `FTNOTE_LOC_FLAG` | DOUBLE |  |  | This defines where footnotes will print on the chart |
| 14 | `INTERP_LOC_FLAG` | DOUBLE |  |  | This defines where interpretive data will print on the chart |
| 15 | `NORMALH_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the normal high label will print |
| 16 | `NORMALL_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the normal low label will print |
| 17 | `NORMAL_HIGH_LBL` | VARCHAR(32) |  |  | This defines the normal high label that will print on the chart |
| 18 | `NORMAL_LOW_LBL` | VARCHAR(32) |  |  | This defines the normal low label that will print on the chart |
| 19 | `PERFID_LBL` | VARCHAR(32) |  |  | This defines the performed_id label |
| 20 | `PERFID_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the performed_id label will print |
| 21 | `REFER_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the reference range label will print |
| 22 | `REF_RANGE_LBL` | VARCHAR(32) |  |  | This defines the reference range label that will print on the chart |
| 23 | `REF_RNG_FORM_FLAG` | DOUBLE |  |  | This defines the formatting of the reference ranges |
| 24 | `RSLT_SEQ_FLAG` | DOUBLE |  |  | This defines whether results will be printed newest to oldest or oldest to newest |
| 25 | `RSLT_START_COL` | DOUBLE |  |  | This field is not used at this time |
| 26 | `STAYDAYS_ORDER` | DOUBLE |  |  | This defines the order in which the day of stay will print on the chart |
| 27 | `TEST_LBL` | VARCHAR(32) |  |  | This defines the procedure label |
| 28 | `TEST_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the test label will print |
| 29 | `TIME_FORMAT_FLAG` | DOUBLE |  |  | This defines the format that the time will print on the chart |
| 30 | `TIME_MASK` | VARCHAR(32) |  |  | This field stores time mask used to format all times within this group. |
| 31 | `TIME_ORDER` | DOUBLE |  |  | This defines the order in which the time should print |
| 32 | `UNITS_LBL` | VARCHAR(32) |  |  | This defines the units label that will print on the chart |
| 33 | `UNITS_LBL_ORDER` | DOUBLE |  |  | This defines the order in which the units will print on the chart |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `WEEKDAY_ORDER` | DOUBLE |  |  | This defines the order in which the weekday will print on the chart |
| 40 | `WKDAY_FORMAT_FLAG` | DOUBLE |  |  | This defines the format for the weekday that will print on the chart |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

