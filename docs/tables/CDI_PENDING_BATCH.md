# CDI_PENDING_BATCH

> This table represents a CPDI Batch within the batch capture process and contains information about the batch.

**Description:** CDI Pending Batch  
**Table type:** ACTIVITY  
**Primary key:** `CDI_PENDING_BATCH_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_CREATE_DT_TM` | DATETIME | NOT NULL |  | Date the CDI Batch was created. |
| 2 | `BATCH_NAME` | VARCHAR(255) | NOT NULL |  | The name of the CDI Batch. |
| 3 | `BATCH_PRIORITY_NBR` | DOUBLE | NOT NULL |  | Specifies the priority of the batch. Batches are sorted and processed in priority order. Suggested values are 1 = High, 5 = Medium and 10 = Low. |
| 4 | `CDI_AC_BATCHCLASS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the CDI_AC_BATCHCLASS table. |
| 5 | `CDI_PENDING_BATCH_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. |
| 6 | `EXTERNAL_BATCH_IDENT` | DOUBLE | NOT NULL |  | Batch identifier from the external system. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Used for filtering in cer_batchindexing at the user level. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_AC_BATCHCLASS_ID` | [CDI_AC_BATCHCLASS](CDI_AC_BATCHCLASS.md) | `CDI_AC_BATCHCLASS_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_PENDING_DOCUMENT](CDI_PENDING_DOCUMENT.md) | `CDI_PENDING_BATCH_ID` |

