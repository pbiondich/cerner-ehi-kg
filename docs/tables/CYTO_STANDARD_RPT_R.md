# CYTO_STANDARD_RPT_R

> This reference table contains the result value parameters associated with each standard report created for a specific cytology report order catalog item.

**Description:** Cytology Standard Report Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal ID code of the alpha response value associated with the report component procedure. This field includes a valid option only if the procedure result type is alpha, and if the result is included in the standard report. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | This column is obsolete. |
| 3 | `RESULT_TEXT` | LONGTEXT |  |  | This field contains the result text value associated with the report component procedure. This field includes text only if the procedure result type is textual, and if the result is included in the standard report. |
| 4 | `STANDARD_RPT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value identifying the standard report to which the report component procedure information is associated. This value could be used to join to the CYTO_STANDARD_REPORT table. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the report component (discrete task) for which result values are defined to be included within the standard report. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `STANDARD_RPT_ID` | [CYTO_STANDARD_RPT](CYTO_STANDARD_RPT.md) | `STANDARD_RPT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

