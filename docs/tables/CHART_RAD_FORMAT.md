# CHART_RAD_FORMAT

> chart radiology format

**Description:** Stores info for formatting of Radiology chart sections  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CDM_CODE_IND` | DOUBLE |  |  | The indicator for printing or not printing CDM codes |
| 6 | `CDM_DESC_IND` | DOUBLE |  |  | The indicator for printing or not printing CDM description |
| 7 | `CDM_LABEL` | VARCHAR(100) |  |  | Label for CDM Codes. |
| 8 | `CDM_LABEL_STYLE` | VARCHAR(255) |  |  | The style for CDM label. |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | FK to chart_group table |
| 10 | `COR_FOOTNOTE_IND` | DOUBLE |  |  | Indicator to store if to suppress the radiology corrected footnote. |
| 11 | `CPT4_CODE_IND` | DOUBLE |  |  | print or not print CPT4 codes |
| 12 | `CPT4_DESC_IND` | DOUBLE |  |  | print or not print CPT4 description |
| 13 | `CPT4_LABEL` | VARCHAR(100) |  |  | label for CPT4 codes |
| 14 | `CPT4_LABEL_STYLE` | VARCHAR(255) |  |  | style for CPT4 labels |
| 15 | `GROUP_STYLE` | VARCHAR(255) |  |  | Style to apply to group heading |
| 16 | `REASON_ANNOTATION` | DOUBLE |  |  | Used to associate procedures with reasons for exam |
| 17 | `REASON_CAPTION` | VARCHAR(100) |  |  | Label for reason for exam |
| 18 | `REASON_IND` | DOUBLE |  |  | Indicates whether or not to print Reason For Exam |
| 19 | `RESULT_SEQUENCE` | DOUBLE |  |  | Oldest to newest or vice versa |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

