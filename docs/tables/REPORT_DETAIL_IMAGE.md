# REPORT_DETAIL_IMAGE

> This table is the relation table between the case_report and blob_reference tables. It specifies which sections of the anatomic pathology report contain additional blob (ie image) data.

**Description:** report_detail_image  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `REPORT_DETAIL_ID` | DOUBLE | NOT NULL |  | This field uniquely identifies a row included on the Report_Detail_Image table. |
| 2 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the anatomic pathology report_id that relates the blob_reference table back to the case_report table. |
| 3 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | This field contains the value of the task_assay_cd that represents a particular report section of a anatomic pathology report. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_ID` | [CASE_REPORT](CASE_REPORT.md) | `REPORT_ID` |

