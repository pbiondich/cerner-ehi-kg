# RC_CLOUD_TRANSACTION

> Used to store information about revenue cycle cloud transactions

**Description:** Revenue Cycle Cloud Transaction  
**Table type:** ACTIVITY  
**Primary key:** `RC_CLOUD_TRANSACTION_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORRELATION_UUID` | VARCHAR(50) | NOT NULL |  | The unique identifier of the revenue cycle cloud transaction (UUID) |
| 2 | `ENCNTR_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the ENCOUNTER table. |
| 3 | `HTTP_METHOD_FLAG` | DOUBLE | NOT NULL |  | The HTTP method used for the revenue cycle cloud transaction. |
| 4 | `HTTP_STATUS_CODE` | DOUBLE | NOT NULL |  | The HTTP status code for the revenue cycle cloud transaction. |
| 5 | `PARENT_CORRELATION_UUID` | VARCHAR(50) |  |  | The correlation universally unique identifier of the parent RevenueCycle cloud transaction associated with this RevenueCycle cloud transaction. |
| 6 | `RC_CLOUD_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | System Generated Identifer created to uniquely identify a row on the RC_CLOUD_TRANSACTION table. |
| 7 | `RESOURCE_URL` | LONGTEXT |  |  | The URL to which the revenue cycle cloud transaction was sent. |
| 8 | `RETRY_CNT` | DOUBLE | NOT NULL |  | The number of times the row has been sent for reprocessing. |
| 9 | `SERVICE_CD` | DOUBLE | NOT NULL |  | The service code used for the revenue cycle cloud transaction. |
| 10 | `STATUS_CD` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CLOUD_TRANSACTION_LT](RC_CLOUD_TRANSACTION_LT.md) | `RC_CLOUD_TRANSACTION_ID` |

