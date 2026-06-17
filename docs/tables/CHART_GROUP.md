# CHART_GROUP

> chart group

**Description:** This table defines the chart groups for a given chart section  
**Table type:** REFERENCE  
**Primary key:** `CHART_GROUP_ID`  
**Columns:** 15  
**Referenced by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CG_SEQUENCE` | DOUBLE |  |  | This is number that is assigned to the chart group that defines the order in which it will print within a section |
| 6 | `CHART_GROUP_DESC` | VARCHAR(64) |  |  | Description of the Chart Group |
| 7 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | PK | This is a unique number assigned to a chart group within a chart format |
| 8 | `CHART_SECTION_ID` | DOUBLE | NOT NULL | FK→ | This is a unique number assigned to a section within a chart format |
| 9 | `ENHANCED_LAYOUT_IND` | DOUBLE |  |  | This identifies if the user selected this section (to which this group belongs) to be an enhanced layout. |
| 10 | `MAX_RESULTS` | DOUBLE |  |  | This field is not used at this time |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_SECTION_ID` | [CHART_SECTION](CHART_SECTION.md) | `CHART_SECTION_ID` |

## Referenced by (22)

| From table | Column |
|------------|--------|
| [CHART_AP_FORMAT](CHART_AP_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_DOC_FORMAT](CHART_DOC_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_DYN_ZONE_FORM](CHART_DYN_ZONE_FORM.md) | `CHART_GROUP_ID` |
| [CHART_FLEX_FORMAT](CHART_FLEX_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_FORMAT_CODES](CHART_FORMAT_CODES.md) | `CHART_GROUP_ID` |
| [CHART_GENERIC_FORMAT](CHART_GENERIC_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_GL_FORMAT](CHART_GL_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `CHART_GROUP_ID` |
| [CHART_HLA_FORMAT](CHART_HLA_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_HORZ_FORMAT](CHART_HORZ_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_IMMUNIZ_FORMAT](CHART_IMMUNIZ_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_LISTVIEW_FORMAT](CHART_LISTVIEW_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_MAR_FORMAT](CHART_MAR_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_MICRO_FORMAT](CHART_MICRO_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_NAME_HIST_FORMAT](CHART_NAME_HIST_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_ORDERS_FORMAT](CHART_ORDERS_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_ORD_SUM_FILTER](CHART_ORD_SUM_FILTER.md) | `CHART_GROUP_ID` |
| [CHART_PROCHIST_FORMAT](CHART_PROCHIST_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_RAD_FORMAT](CHART_RAD_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_VERT_FORMAT](CHART_VERT_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_XENCNTR_FORMAT](CHART_XENCNTR_FORMAT.md) | `CHART_GROUP_ID` |
| [CHART_ZONAL_FORMAT](CHART_ZONAL_FORMAT.md) | `CHART_GROUP_ID` |

