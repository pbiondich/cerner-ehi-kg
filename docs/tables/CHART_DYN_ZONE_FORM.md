# CHART_DYN_ZONE_FORM

> Defines the parameters for the new version of the zonal section.

**Description:** Charting Dynamic Zone Format parameters  
**Table type:** REFERENCE  
**Primary key:** `CHART_GROUP_ID`, `ZONE_SEQ`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | PK FK→ | This is a number that uniquely identifies a chart group |
| 6 | `PROC_COL` | DOUBLE |  |  | The number of the column where procedure names are placed. If column number is 0, it does not appear on the chart. |
| 7 | `PROC_LBL` | VARCHAR(32) |  |  | The column header of the procedure column. |
| 8 | `REF_RANGE_COL` | DOUBLE |  |  | The number of the column where reference ranges are placed. If column number is 0, it does not appear on the chart. |
| 9 | `REF_RANGE_LBL` | VARCHAR(32) |  |  | The column header of the reference range column. |
| 10 | `UNITS_COL` | DOUBLE |  |  | The number of the column where units are placed. If column number is 0, it does not appear on the chart. |
| 11 | `UNITS_LBL` | VARCHAR(32) |  |  | The column header of the units column. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `ZONE_SEQ` | DOUBLE | NOT NULL | PK | The order sequence of the zone, starting at the left with a sequence of 1. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CHART_ZN_RESULT_COL](CHART_ZN_RESULT_COL.md) | `CHART_GROUP_ID` |
| [CHART_ZN_RESULT_COL](CHART_ZN_RESULT_COL.md) | `ZONE_SEQ` |

