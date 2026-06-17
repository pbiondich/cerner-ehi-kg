# MIC_REF_BIO_FORMAT

> This reference table contains formats for biochemical groups defined by test site.

**Description:** Microbiology reference biochmical format.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORMAT_ORDER_TYPE` | DOUBLE |  |  | This field stores the order type of the specified task_assay_cd at a service_resource_cd. There will be two values in this field. 0 = over, then down. 1 = down, then over. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This is the service resource where the biochemical format can be applied. |
| 3 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value assigned to each task defined on the mic_task table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WRAP` | DOUBLE |  |  | The wrap indicates the maximum number of column or rows (depending on biochemical format) before wrapping to a new column or row. A value of zero indicates no wrapping. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

