# CHART_MAR_FORMAT

> Stores the formatting parameters for the MAR section in the Chart Format Builder

**Description:** Formatting parameters for MAR section  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_BY_LBL` | VARCHAR(32) |  |  | The administered by column header |
| 6 | `ADMIN_BY_ORDER` | DOUBLE |  |  | The horizontal order position of the administered by column. |
| 7 | `ADMIN_DETAILS_LBL` | VARCHAR(32) |  |  | The administration details column header. |
| 8 | `ADMIN_DETAILS_ORDER` | DOUBLE |  |  | The horizontal order position of the administration details column. |
| 9 | `ADMIN_DT_TM_LBL` | VARCHAR(32) |  |  | The administration date/time column header |
| 10 | `ADMIN_DT_TM_ORDER` | DOUBLE |  |  | The horizontal order position of the administration date/time column. |
| 11 | `ADMIN_SEQ_IND` | DOUBLE |  |  | Indicates the sequencing of administrations. 0 is chronological, 1 is reverse chronological. |
| 12 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The primary identifier for the chart group to which the formatting information belongs. |
| 13 | `DATE_MASK` | VARCHAR(50) | NOT NULL |  | The format for dates within the section. |
| 14 | `DISPENSED_MNEMONIC_IND` | DOUBLE |  |  | Indicates whether or not the dispensed mnemonic column will appear on the chart. |
| 15 | `INCLUDE_IMG_FOOTER_IND` | DOUBLE | NOT NULL |  | Stores indicator if the image footer is included |
| 16 | `INCLUDE_IMG_HEADER_IND` | DOUBLE | NOT NULL |  | Stores indicator if the image header is included |
| 17 | `MED_SEQ_FLAG` | DOUBLE |  |  | Specifies the order in which the different medication types will appear in the chart. This has been replaced by the section_order field. Values will be restricted to numbers 0 thru 5 by a constraint. |
| 18 | `ORDERED_AS_MNEMONIC_IND` | DOUBLE |  |  | Indicates whether or not the ordered as mnemonic column will appear on the chart. |
| 19 | `ORDER_DETAILS_LBL` | VARCHAR(32) |  |  | The label associated with the order details. |
| 20 | `PRIMARY_MNEMONIC_LBL` | VARCHAR(32) |  |  | The label associated with the primary mnemonic |
| 21 | `SECTION_ORDER` | DOUBLE |  |  | Specifies the order in which the different medication types will appear in the chart. This replaces column MED_SEQ_FLAG. 7/28/03. |
| 22 | `TIME_MASK` | VARCHAR(32) | NOT NULL |  | The format for times within the section. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

