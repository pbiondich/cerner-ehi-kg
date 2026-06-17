# EHI_QUEUE

> Holds the list of EHI Export requests

**Description:** EHI QUEUE  
**Table type:** ACTIVITY  
**Primary key:** `EHI_QUEUE_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORIZATION_RECEIVED_IND` | DOUBLE |  |  | Indicator that specifies if an authorization was given for the extract |
| 2 | `COMMENTS_TXT` | VARCHAR(100) |  |  | Comments associated with this extract |
| 3 | `DESTINATION_TXT` | VARCHAR(50) |  |  | The location of where the extract files will be stored |
| 4 | `EHI_GROUP_ID` | DOUBLE | NOT NULL |  | The CLI processes multi-patient extracts by splitting a CSV of patient IDs into batches, with each batch treated as a single EHI request. There is a need to group these batches. Column EHI_GROUP_ID will be identify each multi-patient extract, enabling users to restart or cancel all extracts in the group with a single action. |
| 5 | `EHI_QUEUE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY - Unique generated number that identifies a single row |
| 6 | `EXTRACT_STATUS_DETAIL_TXT` | VARCHAR(4000) |  |  | Expanded description of the status of the EHI Extract request |
| 7 | `EXTRACT_STATUS_TS` | DATETIME(6) |  |  | Date and time that the satus of the request for the EHI Extract was updated |
| 8 | `EXTRACT_STATUS_TXT` | VARCHAR(16) |  |  | Status of the EHI Extract request |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `PRSNL_ID` | DOUBLE |  | FK→ | Identifier for person that is being extracted |
| 11 | `PURPOSE_NBR` | DOUBLE |  |  | The reason for the extract |
| 12 | `REQUESTER_TXT` | VARCHAR(80) |  |  | Name of the person/orginzation that requested the extract |
| 13 | `REQUEST_DT_TM` | DATETIME |  |  | Date and time that the request for the EHI Extract was made |
| 14 | `REQUEST_TYPE_TFLG` | VARCHAR(50) |  |  | The type of EHI Export that has been requested |
| 15 | `RESULTS_TXT` | VARCHAR(500) |  |  | Text that indicates the final status of the request |
| 16 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EHI_PLAN](EHI_PLAN.md) | `EHI_QUEUE_ID` |
| [EHI_QUEUE_PERSON_RELTN](EHI_QUEUE_PERSON_RELTN.md) | `EHI_QUEUE_ID` |
| [EHI_REF_DATA_CACHE](EHI_REF_DATA_CACHE.md) | `EHI_QUEUE_ID` |

