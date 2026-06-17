# MIC_REQ_RPT

> This table identifies the required and pending reports for each procedure/source and service resource combination.

**Description:** Microbiology Required Reports  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each set of required and pending reports defined for each procedure/source and service resource combination. |
| 2 | `REQUIRED_IND` | DOUBLE |  |  | This field indicates whether the report is required (mandatory) or pending (suggested) for the procedure. Valid values include: 0 = Pending 1 = Required |
| 3 | `TASK_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the report defined as required or pending for this procedure. Reports are defined on code set 1000, Microbiology Reports. |
| 4 | `TAT_MINUTES` | DOUBLE | NOT NULL |  | This field identifies the turnaround time value for the report. This time value is the expected turn around time for the report associated with the procedure. |
| 5 | `TAT_UNITS_CD` | DOUBLE | NOT NULL |  | This field identifies the unit of time associated with the tat_minutes field. Units are defined on code set 340, Age Units. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITERIA_ID` | [MIC_RPT_PARAMS](MIC_RPT_PARAMS.md) | `CRITERIA_ID` |
| `TASK_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

