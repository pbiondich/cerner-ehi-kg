# RC_CLOUD_SYNC

> This table is created for the initial master file load sync between millenium and soarian.

**Description:** Revenue Cycle Cloud Sync  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_POOL_CD` | DOUBLE |  |  | Contains the code value related to the alias pool |
| 3 | `HEALTH_PLAN_ID` | DOUBLE |  | FK→ | Uniquely identifies the related Health Plan record. |
| 4 | `LOCATION_CD` | DOUBLE |  | FK→ | Uniquely identifies the related value in the Location table. |
| 5 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | Uniquely identifies the related Organization row. |
| 6 | `PAYLOAD_BLOB` | LONGBLOB |  |  | Contains the serialized non millennium object |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date and time the row was processed. |
| 8 | `PRSNL_ID` | DOUBLE |  | FK→ | Uniquely identifies the related PRSNL row. |
| 9 | `RC_CLOUD_SYNC_ID` | DOUBLE | NOT NULL |  | A system generated number used to uniquely identify a row on the RC_CLOUD_SYNC table. |
| 10 | `REFERENCE_NAME` | VARCHAR(255) |  |  | The name of the master file to be synced |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

