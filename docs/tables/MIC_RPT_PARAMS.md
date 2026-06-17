# MIC_RPT_PARAMS

> This table identifies a unique value for each procedure/source and service resource combination forwhich required and pending report parameters are defined.

**Description:** Microbiology Report Parameters  
**Table type:** REFERENCE  
**Primary key:** `CRITERIA_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 2 | `CRITERIA_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each set of required and pending reports defined for each procedure/source and service resource combination. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which report parameters are defined. Service resources are defined on code set 221. |
| 4 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define report parameters. All three levels of source hierarchy (source, section, and category) can be used to define interpretations. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_REQ_RPT](MIC_REQ_RPT.md) | `CRITERIA_ID` |
| [MIC_RPT_LIMIT](MIC_RPT_LIMIT.md) | `CRITERIA_ID` |

