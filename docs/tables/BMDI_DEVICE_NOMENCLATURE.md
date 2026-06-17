# BMDI_DEVICE_NOMENCLATURE

> Identifies the Alpha translations that can be performed for a given device.

**Description:** BMDI Device Nomenclature  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALPHA_TRANSLATION` | VARCHAR(50) | NOT NULL |  | Resulting translated value. |
| 3 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Used to identify translations across service resources. |
| 4 | `DEVICE_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Used as a primary key. |
| 5 | `DEVICE_PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a parameter. |
| 6 | `DEVICE_VALUE` | VARCHAR(50) | NOT NULL |  | Device value requiring translation |
| 7 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature id for the parameter value |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `DEVICE_PARAMETER_ID` | [BMDI_DEVICE_PARAMETER](BMDI_DEVICE_PARAMETER.md) | `DEVICE_PARAMETER_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

