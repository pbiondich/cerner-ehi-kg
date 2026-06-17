# CHART_ZN_FORM_ZONE

> chart zone format zone

**Description:** This table defines the attributes for a paticular zone in a zonal section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALL_RSLT_COL` | DOUBLE |  |  | This defines whether all results will print in a single column on the chart |
| 6 | `ALL_RSLT_LBL` | VARCHAR(32) |  |  | This defines the all results label that should print on the chart |
| 7 | `ALPHA_ABN_RSLT_COL` | DOUBLE |  |  | This is defines the column where abnormal alpha results will print |
| 8 | `ALPHA_ABN_RSLT_LBL` | VARCHAR(32) |  |  | This defines the abnormal alpha result label that should print on the chart |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL |  | This number uniquely identifies the chart group |
| 10 | `CRIT_RSLT_COL` | DOUBLE |  |  | This identifies the column in which critical results should print |
| 11 | `CRIT_RSLT_LBL` | VARCHAR(32) |  |  | This defines the critical results label that should print on the chart |
| 12 | `HIGH_RSLT_COL` | DOUBLE |  |  | This defines the column in which high results should print |
| 13 | `HIGH_RSLT_LBL` | VARCHAR(32) |  |  | This defines the high results label that should print on the chart |
| 14 | `LOW_RSLT_COL` | DOUBLE |  |  | This defines the column in which low results should print |
| 15 | `LOW_RSLT_LBL` | VARCHAR(32) |  |  | This defines the low results label that should print on the chart |
| 16 | `NORMAL_RSLT_COL` | DOUBLE |  |  | This defines the column in which the normal results should print |
| 17 | `NORMAL_RSLT_LBL` | VARCHAR(32) |  |  | This defines the normal results label that should print on the chart |
| 18 | `REF_RANGE_COL` | DOUBLE |  |  | This defines the column in which the reference ranges should print |
| 19 | `REF_RANGE_LBL` | VARCHAR(32) |  |  | This defines the reference range label that should print on the chart |
| 20 | `TEST_COL` | DOUBLE |  |  | This defines the column in which the procedure name should print |
| 21 | `TEST_LBL` | VARCHAR(32) |  |  | This defines the test label that should print on the chart |
| 22 | `UNITS_COL` | DOUBLE |  |  | This defines the column units should print in |
| 23 | `UNITS_LBL` | VARCHAR(32) |  |  | This defines the units label that should print on the chart |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `ZONE_SEQ` | DOUBLE | NOT NULL |  | This defines the zone within the zonal section |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

