# MIC_RPT_LIMIT

> This table associates a limit on the number of times a particular report can be issued for a procedure/report type.

**Description:** Microbiology Report Limits  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each set of required and pending reports defined for each procedure/source and service resource combination. |
| 2 | `REPORT_LIMIT` | DOUBLE |  |  | This field identifies the number of times the report can be issued for a procedure/accession. |
| 3 | `TASK_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the report defined as required or pending for this procedure. Reports are defined on code set 1000, Microbiology Reports. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITERIA_ID` | [MIC_RPT_PARAMS](MIC_RPT_PARAMS.md) | `CRITERIA_ID` |
| `TASK_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

