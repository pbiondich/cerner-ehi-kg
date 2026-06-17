# PROCEDURE_CODE_TIER

> Stores "rules" to define relationships between CPT-4, HCPCS, and revenue codes.

**Description:** PROCEDURE CODE TIER  
**Table type:** REFERENCE  
**Primary key:** `PROCEDURE_CODE_TIER_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type |
| 6 | `BEGIN_CPT4` | VARCHAR(200) |  |  | The beginning cpt4 value for range |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Reference to the billing entity |
| 9 | `BILL_ITEM_ID` | DOUBLE | NOT NULL |  | Bill_item_id that the charge was ordered from |
| 10 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type from code_set 71 |
| 11 | `END_CPT4` | VARCHAR(200) |  |  | The ending cpt4 value for range |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `HCPCS` | VARCHAR(200) |  |  | The HCPCS value (source_code from nomenclature) |
| 14 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Reference to Health_plan table |
| 15 | `PROCEDURE_CODE_TIER_ID` | DOUBLE | NOT NULL | PK | Primary key into procedure_code tier using new sequence pft_procedure_code_tier_seq |
| 16 | `ROW_NUM` | DOUBLE | NOT NULL |  | This stores the row number of where they belong in the spreadsheet |
| 17 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Service resource from code set 220 |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TIER_REV_CODE_RELTN](TIER_REV_CODE_RELTN.md) | `PROCEDURE_CODE_TIER_ID` |

