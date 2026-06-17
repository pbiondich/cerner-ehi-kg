# MIC_ABN_ORG_RESPONSE_CODE

> This table takes the combination of procedure/source/service resource and creates a unique identifier which is used to define abnormal result parameters.

**Description:** Microbiology Abnormal Organism Criteria  
**Table type:** REFERENCE  
**Primary key:** `CRITERIA_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_GROUP_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 3 | `CRITERIA_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each set of abnormal results defined for a procedure/source/service resource combination. |
| 4 | `DIAGNOSIS_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 5 | `ETHNIC_GROUP_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 6 | `INCLUDE_EXCLUDE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which abnormal results are defined. Service resources are defined on code set 221. |
| 8 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define abnormal results. All three levels of source hierarchy (source, section, category) can be used to define interpretations. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_ABNORMAL_LIST](MIC_ABNORMAL_LIST.md) | `CRITERIA_ID` |

