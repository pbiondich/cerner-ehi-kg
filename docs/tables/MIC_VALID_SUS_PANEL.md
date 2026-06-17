# MIC_VALID_SUS_PANEL

> This table takes the combination of procedure/service resource/source and organism and creates a unique identifier that is used to define the valid susceptibility antibiotic or ID panels.

**Description:** Microbiology Valid Susceptibility Panel Criteria  
**Table type:** REFERENCE  
**Primary key:** `VALID_PANEL_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `METHOD_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the susceptibility method for which valid susceptibility panels are defined. Susceptibility methods are defined on code set 65. |
| 3 | `ORGANISM_GROUPING_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the organism for which valid susceptibility panels are defined. Organisms are defined on code set 1021, Organisms. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which valid panels are defined. Service resources are defined on code set 221. |
| 5 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define valid susceptibility panels. All three levels of source hierarchy (source, section, category) can be used in defining valid panels. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALID_PANEL_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each set of valid susceptibility panels defined for an orderable procedure/service resource/source and organism combination. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `METHOD_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |
| `ORGANISM_GROUPING_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_REF_BILLING_PANEL](MIC_REF_BILLING_PANEL.md) | `VALID_PANEL_ID` |
| [MIC_VALID_PANEL](MIC_VALID_PANEL.md) | `VALID_PANEL_ID` |

