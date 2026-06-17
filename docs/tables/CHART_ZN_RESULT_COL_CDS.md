# CHART_ZN_RESULT_COL_CDS

> The normalcy codes assigned to a result column in a new version zone.

**Description:** Result column normalcy codes for new version of zonal section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | A number that uniquely identifies a chart group. |
| 6 | `COLUMN_SEQ` | DOUBLE | NOT NULL | FK→ | The order sequence of the result column containing these normalcy codes. |
| 7 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | The code value for the defined normalcy code |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `ZONE_SEQ` | DOUBLE | NOT NULL | FK→ | The order sequence for the containing zone. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_ZN_RESULT_COL](CHART_ZN_RESULT_COL.md) | `CHART_GROUP_ID` |
| `COLUMN_SEQ` | [CHART_ZN_RESULT_COL](CHART_ZN_RESULT_COL.md) | `COLUMN_SEQ` |
| `ZONE_SEQ` | [CHART_ZN_RESULT_COL](CHART_ZN_RESULT_COL.md) | `ZONE_SEQ` |

