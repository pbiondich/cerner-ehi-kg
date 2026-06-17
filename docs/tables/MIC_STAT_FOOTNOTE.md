# MIC_STAT_FOOTNOTE

> This summary table is comprised of records extracted from the MIC_RESULT_FOOTNOTE_R table. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Footnote  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the antibiotic being tested within a susceptibility task. |
| 2 | `CHARTABLE_IND` | DOUBLE |  |  | This field indicates whether or not the susceptibility footnote is to be included on patient reports and displayed in inquiry applications. Valid values include: 0 = Not chartable 1= Chartable |
| 3 | `EKM_IND` | DOUBLE |  |  | This field indicates whether or not the susceptibility footnote has been generated from an expert knowledge module. Valid values include: 0 = Not expert knowledge module generated 1= Expert knowledge module generated |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the LONG_TEXT row, which contains a textual value for susceptibility footnote text. |
| 5 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the susceptibility task from the MIC_STAT_TASK table thus associating the susceptibility footnote with the appropriate susceptibility task. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |

