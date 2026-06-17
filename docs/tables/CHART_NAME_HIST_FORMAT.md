# CHART_NAME_HIST_FORMAT

> Stores the formatting parameters for the Name History section in the Chart Format Builder.

**Description:** Formatting parameters for Name History section.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM_LBL` | VARCHAR(32) |  |  | This label serves as the column heading for the beg_effective_dt_tm of when the person's name changed. |
| 6 | `BEG_EFFECTIVE_DT_TM_ODR` | DOUBLE |  |  | This is the horizontal order (sequence) of the beg_effective_dt_tm column. |
| 7 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The primary identifier for the chart group to which the formatting information belongs. |
| 8 | `END_EFFECTIVE_DT_TM_LBL` | VARCHAR(32) |  |  | This label serves as the column heading for the end_effective_dt_tm of the person's name. |
| 9 | `END_EFFECTIVE_DT_TM_ODR` | DOUBLE |  |  | This is the horizontal order (sequence) of the end_effective_dt_tm column. |
| 10 | `NAME_LBL` | VARCHAR(32) |  |  | This label serves as the column heading for the person's name. |
| 11 | `NAME_ODR` | DOUBLE |  |  | This is the horizontal order (sequence) of the end_effective_dt_tm column. |
| 12 | `ORDER_SEQ_IND` | DOUBLE |  |  | Specifies the ordering of the name changes, in either newest to oldest (1) or oldest to newest (0) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

