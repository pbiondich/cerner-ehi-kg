# AV_RES_CAT

> Defines the orderables for a resource that have specific autoverify requirements

**Description:** Automatic Verificaton Service Resource Code Catalog Code  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOC_CATALOG_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies an associated order catalog item. For an av_res_cat_flag of "3" the associated catalog code indicates the orderable that should not be verified because the other orderable was not verified. |
| 3 | `AV_RES_CAT_FLAG` | DOUBLE |  |  | Defines the values of how to use the order catalog item.1 - Autoverify within the orderable; 2 - Never autoverify the orderable; 3 - Don't autoverify this associated orderable;4 - Do not autoverify when order comment or note is present; 5 - Do not autoverify when order comment is present; 6 - Do not autoverify when order note is present.;7 - Hold result autoverification(av) until all required task assays with av criteria for the orderable qualify to be av regardless of the # of msg |
| 4 | `AV_RES_CAT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific autoverification resource catalog row. |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific order catalog item. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies a specific service resource. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

