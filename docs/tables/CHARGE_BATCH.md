# CHARGE_BATCH

> Contains user and system generated batches with associated batch information for all batches created in the RCA Charge Entry framework.

**Description:** Charge Batch  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_BATCH_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSED_DT_TM` | DATETIME |  |  | The date and time this batch was last accessed. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the personnel who is assigned to the batch. |
| 4 | `BATCH_ALIAS` | VARCHAR(50) | NOT NULL |  | Stores an alias to a batch. The possible aliases are pulled from an alias pool. |
| 5 | `BATCH_DT_TM` | DATETIME |  |  | Store a batch level date and time. |
| 6 | `CHARGE_BATCH_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a user batch or system generated batch and related batch information for every batch in the RCA Charge Entry framework. |
| 7 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 8 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | Stores the status of the batch. |
| 10 | `STATUS_DT_TM` | DATETIME |  |  | The date and time of the last status change. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `USER_DEFINED_IND` | DOUBLE | NOT NULL |  | Indicates whether a user or system created the batch1 - user created the batch2 - system created the batch |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CHARGE_BATCH_DETAIL](CHARGE_BATCH_DETAIL.md) | `CHARGE_BATCH_ID` |

