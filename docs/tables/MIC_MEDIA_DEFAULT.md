# MIC_MEDIA_DEFAULT

> This table identifies the default media associated with each procedure/source/body site and serviceresource combination.

**Description:** Microbiology Default Inoculation Media  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the body site used to define default media. Body sites are defined on code set 1028, Body Sites. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 3 | `MEDIA_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the media for which defaults are defined.. Media is defined on code set 2051, Container. |
| 4 | `MEDIA_LABEL_CNT` | DOUBLE |  |  | This field identifies the number of media labels that should be printed for this piece of media. |
| 5 | `MEDIA_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the uniqueness of a row when more than one media is associated with the same service_resource_cd and catalog_cd. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which default media is defined. Service resources are defined on code set 221. |
| 7 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define default media. All three levels of source hierarchy (source, section, and category) can be used to define interpretations. |
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
| `MEDIA_CD` | [MIC_MEDIA](MIC_MEDIA.md) | `MEDIA_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

