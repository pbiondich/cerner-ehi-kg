# CYTO_ADEQUACY_ALPHA_R

> This reference table contains the classification of every alpha response code associated with the microscopic evaluation of specimen adequacy report component procedure for cytoloogy reports.

**Description:** Cytology Adequacy Alpha Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADEQUACY_FLAG` | DOUBLE | NOT NULL |  | This field contains a flag value documenting the general category of microscopic adequacy (satisfactory, limited, or unsatisfactory, for example) associated with the associated alpha response code value. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the cytology report for which adequacy parameters are defined. This value could be used to join to the order catalog tables, if desired. |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the nomenclature response documenting specimen adequacy. This value could be used to join to the NOMENCLATURE table. |
| 4 | `REASON_REQUIRED_IND` | DOUBLE |  |  | This field contains a flag value documenting whether or not the user should be forced to enter an inadequacy reason when the associated alpha response value is selected during the report entry process. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the statement of microscopic adequacy report component. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `CATALOG_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

