# SN_REPORT_TEMPLATE

> This is the table that will be used for dynamically generate customized reports.

**Description:** SN REPORT TEMPLATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 5 | `DISPLAY` | VARCHAR(50) |  |  | Display of the template. |
| 6 | `DISPLAY_KEY` | VARCHAR(50) |  |  | Key to associate the template to the Operations.This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 7 | `REPORT_TEMPLATE_ID` | DOUBLE | NOT NULL |  | Primary key of the table |
| 8 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Area for which the cases will be retrived from. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

