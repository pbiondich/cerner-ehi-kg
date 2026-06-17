# AP_CASE_SYNOPTIC_WS

> This table maintains a list of synoptic worksheets associated with an Anatomic Pathology case.

**Description:** Anatomic Pathology Case Synoptic Worksheet  
**Table type:** ACTIVITY  
**Primary key:** `CASE_WORKSHEET_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAP_CHECKLIST_CKI` | VARCHAR(255) |  |  | The CAP checklist concept the story results are for. This is a Version CKey. |
| 2 | `CASE_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | This field links the worksheet to a specific specimen (CASE_SPECIMEN). |
| 3 | `CASE_WORKSHEET_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a case worksheet. |
| 4 | `FOREIGN_WS_IDENT` | VARCHAR(50) |  |  | Uniquely identifies a worksheet in a third party synoptic reporting system(e.g. mTuitive). This column will only be valued for foreign worksheets. |
| 5 | `FOREIGN_WS_RESULT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long_text table id for the worksheet result from a third party synopticreporting system (e.g. mTuitive). This column will only be valued for foreign worksheets. |
| 6 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | The specific report on the case (CASE_REPORT) that the worksheet is tied to. |
| 7 | `SCD_STORY_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the actual worksheet data in the SCD_STORY table |
| 8 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the SCD pattern to use for data entry on this worksheet. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field is used to sort the worksheets for any one specimen. |
| 10 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Identifies status of worksheet: 0 - Not started 1 - Incomplete 2 - Completed 3 - Orphaned |
| 11 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The report section this worksheet is linked to. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_SPECIMEN_ID` | [CASE_SPECIMEN](CASE_SPECIMEN.md) | `CASE_SPECIMEN_ID` |
| `FOREIGN_WS_RESULT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REPORT_ID` | [CASE_REPORT](CASE_REPORT.md) | `REPORT_ID` |
| `SCD_STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AP_CASE_SYNOPTIC_WS_DATA](AP_CASE_SYNOPTIC_WS_DATA.md) | `CASE_WORKSHEET_ID` |

