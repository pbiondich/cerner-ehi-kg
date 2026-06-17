# CYTO_ENDOCERV_ALPHA_R

> This reference table contains the classification of every alpha response code associated with the presence or absence of the endocervical component for gynecologic cytology reports.

**Description:** Cytology Endocervical Alpha Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the cytology report for which endocervical cell parameters are defined. This value could be used to join to the order catalog tables, if desired. |
| 2 | `ENDOCERV_IND` | DOUBLE | NOT NULL |  | This field contains a flag value documenting the collection technique evaluation (determined by the presence or absence of endocervical cells) associated with the associated alpha response code value. |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the nomenclature response documenting the collection technique evaluation (determined by the presence of endocervical cells). This value could be used to join to the NOMENCLATURE table. |
| 4 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the discrete task within the cytology report which represents the collection technique evaluation report component (determined by the presence or absence of endocervical cells). |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `CATALOG_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

