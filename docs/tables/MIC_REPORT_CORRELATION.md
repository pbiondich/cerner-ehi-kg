# MIC_REPORT_CORRELATION

> This reference table contains a single record for every correlation check for a report at a serviceresource that needs to occur.

**Description:** Microbiology Report Correlation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the procedure to which the correlation is assigned. This could be used to join to the order_catalog table. |
| 2 | `FAILURE_REASON_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code assigned to the type of failure the correlation rule is checking. |
| 3 | `FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code assigned to display format of the correlation message. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the service resource to which the stain correlation rule is assigned. This could be used to join to the service_resource table. |
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

