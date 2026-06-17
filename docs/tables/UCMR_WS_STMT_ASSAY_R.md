# UCMR_WS_STMT_ASSAY_R

> Stores worksheet statement to assay mappings.

**Description:** Unified Case Manager Reference - Worksheet Statement Assay Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CASE_STEP_CAT_CD` | DOUBLE | NOT NULL |  | The case type workup where the mapped relationship exists. |
| 5 | `CONVERT_TO_TEXT_IND` | DOUBLE | NOT NULL |  | The system can auto-convert result when loaded if it doesn't fit an assay's defined parameters. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task assay to which the worksheet statement is mapped. |
| 8 | `UCMR_CASE_WORKUP_ID` | DOUBLE | NOT NULL | FK→ | The case type workup where the mapped relationship exists. |
| 9 | `UCMR_WORKSHEET_STATEMENT_R_ID` | DOUBLE | NOT NULL | FK→ | The specific Worksheet Statement Identifier that is mapped |
| 10 | `UCMR_WS_STMT_ASSAY_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between a worksheet statement and an assay. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_CASE_WORKUP_ID` | [UCMR_CASE_WORKUP](UCMR_CASE_WORKUP.md) | `UCMR_CASE_WORKUP_ID` |
| `UCMR_WORKSHEET_STATEMENT_R_ID` | [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |

