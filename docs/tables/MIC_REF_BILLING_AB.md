# MIC_REF_BILLING_AB

> This reference table contains a single record for every susceptibility antibiotic that needs a charge sent to billing. Charges can be sent over every time they are ordered or once per organism.

**Description:** Microbiology Reference Billing Antibiotic  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | FK→ | If an antibiotic was entered for billing, this field contains the internal identification code assigned to the antibiotic. Antibiotics are stored on code_set 1011. |
| 2 | `ONCE_PER_ORG_IND` | DOUBLE | NOT NULL |  | This field includes an indicator documenting whether or not the antibiotic should be billed every time or once per organism. |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the service resource to which the susceptibility antibiotic bill item is assigned. This could be used to join to the service_resource table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANTIBIOTIC_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

