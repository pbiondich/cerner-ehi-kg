# MIC_ABN_SUS_RESULT

> This table takes the combination of procedure/source/organism/susceptibility type and service resource and creates a unique identifier that is used to define abnormal susceptibility result parameters.

**Description:** Microbiology Abnormal Susceptibility Results  
**Table type:** REFERENCE  
**Primary key:** `ABN_SUS_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_SUS_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each set of abnormal susceptibility results defined for a procedure/source/organism/susceptibility type and service resource combination. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 3 | `ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the organism for which susceptibility abnormal results are defined. Organisms are defined on code set 1021, Organisms. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which abnormal results are defined. Service resources are defined on code set 221. |
| 5 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define abnormal results. All three levels of source hierarchy (source, section, and category) can be used to define interpretations. |
| 6 | `SUS_DETAIL_CD` | DOUBLE | NOT NULL | FK→ | This field identifies of the susceptibility detail procedure for which susceptibility interpretations are defined. Susceptibility detail procedures are defined on code set 1004. |
| 7 | `SUS_METHOD_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the susceptibility method for which susceptibility abnormal results are defined. Susceptibility methods are defined on code set 65. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SUS_DETAIL_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `SUS_METHOD_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_MEDICATION_RANGE](MIC_MEDICATION_RANGE.md) | `ABN_SUS_ID` |

