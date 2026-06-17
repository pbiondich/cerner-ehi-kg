# CHARGE_BATCH_DETAIL

> Stores all service item events for a given batch.

**Description:** Charge Batch Detail  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_BATCH_DETAIL_ID`  
**Columns:** 27  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the service item being ordered. |
| 3 | `CHARGE_BATCH_DETAIL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a service item event entered for a given batch. |
| 4 | `CHARGE_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the charge batch related to this service item event. |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted into the database. |
| 6 | `DIAGNOSIS_POINTER_NBR` | DOUBLE | NOT NULL |  | OBSOLETE - NO LONGER USED. Pointer value to the diagnosis code placement on the encounter. |
| 7 | `DIAGNOSIS_POINTER_TXT` | VARCHAR(50) |  |  | Pointer value to the diagnosis code placement on the encounter. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter related to this service item event. |
| 9 | `ITEM_COPAY_AMT` | DOUBLE | NOT NULL |  | Contains the Copay amount for the item. |
| 10 | `ITEM_DEDUCTIBLE_AMT` | DOUBLE | NOT NULL |  | Contains the deductible amount for the item. |
| 11 | `ORDERING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health care provider who ordered the service. |
| 12 | `PATIENT_RESPONSIBILITY_FLAG` | DOUBLE | NOT NULL |  | Flag used to Identify Patient Responsibility Check. 0 - Unknown; 1 - Patient Responsible; 2 - Patient Not Responsible |
| 13 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Represents the location at which the services were provided. |
| 14 | `RENDERING_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health care provider who rendered the service. |
| 15 | `SERVICE_DT_TM` | DATETIME |  |  | The date and time that the service was rendered. |
| 16 | `SERVICE_ITEM_DESC` | VARCHAR(200) | NOT NULL |  | The description of the service item being ordered. |
| 17 | `SERVICE_ITEM_IDENT` | VARCHAR(50) | NOT NULL |  | Contains the identifier used to look up the service item. |
| 18 | `SERVICE_ITEM_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the value that identifies the type of service item identifier used to look up the service item. |
| 19 | `SERVICE_ITEM_PRICE_AMT` | DOUBLE | NOT NULL |  | The price of the service item being ordered. |
| 20 | `SERVICE_ITEM_QTY` | DOUBLE | NOT NULL |  | The quantity of the service item being ordered. |
| 21 | `SERVICE_RESOURCE_CD` | DOUBLE |  |  | value from 221 that represents the service resource where the activity/event occurred |
| 22 | `STATUS_CD` | DOUBLE | NOT NULL |  | Designates the status of the service item within a batch. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `CHARGE_BATCH_ID` | [CHARGE_BATCH](CHARGE_BATCH.md) | `CHARGE_BATCH_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDERING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RENDERING_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CHARGE_BATCH_DETAIL_CODE](CHARGE_BATCH_DETAIL_CODE.md) | `CHARGE_BATCH_DETAIL_ID` |
| [CHARGE_BATCH_DETAIL_FIELD](CHARGE_BATCH_DETAIL_FIELD.md) | `CHARGE_BATCH_DETAIL_ID` |

