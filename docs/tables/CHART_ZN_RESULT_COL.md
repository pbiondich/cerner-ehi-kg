# CHART_ZN_RESULT_COL

> Contains the result columns for a zone in the new version of the zonal section.

**Description:** Zone result columns  
**Table type:** REFERENCE  
**Primary key:** `CHART_GROUP_ID`, `COLUMN_SEQ`, `ZONE_SEQ`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | PK FK→ | A number that uniquely identifies a chart group. |
| 6 | `COLUMN_SEQ` | DOUBLE | NOT NULL | PK | The column number of the result column. The value should always be greater than 0 because a 0 value would imply that it does not appear on the chart, and it should not be in the table if it is not in the chart. |
| 7 | `COL_INDEX` | DOUBLE |  |  | The relative column number among other result columns in the zone. A value of 1 means that it is the first result column, a value of 2 means that it is the second, etc. This is used in part of the interface in the Chart Format Builder. |
| 8 | `DESCRIPTION` | VARCHAR(32) |  |  | The column header. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `ZONE_SEQ` | DOUBLE | NOT NULL | PK FK→ | The order sequence of the zone containing this result column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_DYN_ZONE_FORM](CHART_DYN_ZONE_FORM.md) | `CHART_GROUP_ID` |
| `ZONE_SEQ` | [CHART_DYN_ZONE_FORM](CHART_DYN_ZONE_FORM.md) | `ZONE_SEQ` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CHART_ZN_RESULT_COL_CDS](CHART_ZN_RESULT_COL_CDS.md) | `CHART_GROUP_ID` |
| [CHART_ZN_RESULT_COL_CDS](CHART_ZN_RESULT_COL_CDS.md) | `COLUMN_SEQ` |
| [CHART_ZN_RESULT_COL_CDS](CHART_ZN_RESULT_COL_CDS.md) | `ZONE_SEQ` |

