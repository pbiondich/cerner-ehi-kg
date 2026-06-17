# MIC_REF_BILLING_SUS

> This reference table contains a single record for every susceptibility method that needs a charge sent to billing. Charges can be sent over every time they are ordered or once per organism.

**Description:** Microbiology Reference Billing Susceptibility  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ONCE_PER_ORG_IND` | DOUBLE | NOT NULL |  | This field includes an indicator documenting whether or not the susceptibility method should be billed every time or once per organism. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the service resource to which the susceptibility method bill item is assigned. This could be used to join to the service_resource table. |
| 3 | `SUS_METHOD_CD` | DOUBLE | NOT NULL | FK→ | If a susceptibility method was entered for billing, this field contains the internal identificationcode assigned to the method. Susceptibility methods are stored on code_set 65. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SUS_METHOD_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

