# CHART_ZONAL_FORMAT

> chart zone format

**Description:** This table defines the formatting for a zonal section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNML_HILITE_FLAG` | DOUBLE |  |  | This defines the type of highlighting for abnormal results |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This number uniqely identifies the chart group |
| 7 | `COLLECT_DATE_CHK` | DOUBLE |  |  | Contains a value of either 1 or 0 indicating whether the collection date should appear above all zones in the new version of the zonal section. |
| 8 | `COLLECT_DATE_LBL` | VARCHAR(32) |  |  | The label that appears before the collection date and time above a zone in the new version of the zonal section. This only appears if the collect_date_chk = 1 |
| 9 | `CRIT_HILITE_FLAG` | DOUBLE |  |  | This defines the highlighting for critical results |
| 10 | `DATE_FORMAT_CD` | DOUBLE | NOT NULL |  | This code defines the type of formatting that should be used when the date is printed on the chart |
| 11 | `DATE_MASK` | VARCHAR(50) |  |  | This field stores a date mask to be used on all date within this group. |
| 12 | `FTNOTE_LOC_FLAG` | DOUBLE |  |  | This defines where footnotes should be printed on the chart |
| 13 | `INTERP_LOC_FLAG` | DOUBLE |  |  | This defines where the interpretive data should print |
| 14 | `ORDER_GROUP_IND` | DOUBLE | NOT NULL |  | Indicator for noting to group results by order_id |
| 15 | `REF_RNG_FORM_FLAG` | DOUBLE |  |  | This defines the format that the reference range should use when printing on the chart |
| 16 | `RSLT_SEQ_FLAG` | DOUBLE |  |  | This defines the order in which the results should print |
| 17 | `TIME_FORMAT_FLAG` | DOUBLE |  |  | This defines the format that the time should used when printed on the chart |
| 18 | `TIME_MASK` | VARCHAR(32) |  |  | This field stores time mask used to format all times for this group. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

