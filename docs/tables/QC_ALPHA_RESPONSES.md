# QC_ALPHA_RESPONSES

> Defines the alpha response selection for a control and assay that will be allowed for QC result entry.

**Description:** Quality Control Alpha Responses  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific control material associated with a quality control alpha response. |
| 2 | `DEFAULT_IND` | DOUBLE |  |  | Indicates whether the quality control alpha response is the default result value. A value of 0 indicates the response is not a default response. A value of 1 indicates the response is a default response. |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific alpha response nomenclature. Creates a relationship to the nomenclature table. |
| 4 | `RESULT_PROCESS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether the alpha response is a normal or abnormal response. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific service resource (i.e. instrument, bench) associated to the quality control alpha response. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the specific discrete task assay that will be resulted with the quality control alpha response. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

