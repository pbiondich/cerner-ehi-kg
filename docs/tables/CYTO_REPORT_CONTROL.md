# CYTO_REPORT_CONTROL

> This reference table contains the classification of the report component procedures included within a cytology report. Inclusion on this table is required for a report to be resulted or verified using the result entry application specific for cytology.

**Description:** Cytology Report Control  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code associated with the discrete task within the cytology report which represents the follow-upaction report component. |
| 2 | `ADEQUACY_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the statement of microscopic adequacy coded response report component. |
| 3 | `ADEQ_REASON_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the limited/unsatisfactory reason coded response report component. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL | PK FK→ | The field contains the internal identification code associated with the cytology report for which cytology report parameters are defined. This field uniquely defines a row included n the CYTO_REPORT_CONTROL reference table. |
| 5 | `CLIN_INFO_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the clinical information report component. |
| 6 | `DIAGNOSIS_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the diagnosis coded response report component. |
| 7 | `ENDOCERV_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal ID code associated with the discrete task within the cytology report which represents the evaluation of collection technique based on the presence/absence of endocervical cells coded response report component. |
| 8 | `REPORT_TYPE_FLAG` | DOUBLE |  |  | This field contains a flag value indicating if the report represents a gynecologic cytology report or a non-gynecologic cytology report. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `ADEQUACY_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `ADEQ_REASON_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `CLIN_INFO_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `DIAGNOSIS_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `ENDOCERV_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CYTO_ADEQUACY_ALPHA_R](CYTO_ADEQUACY_ALPHA_R.md) | `CATALOG_CD` |
| [CYTO_ENDOCERV_ALPHA_R](CYTO_ENDOCERV_ALPHA_R.md) | `CATALOG_CD` |

