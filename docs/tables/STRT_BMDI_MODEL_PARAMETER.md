# STRT_BMDI_MODEL_PARAMETER

> Identifies the parameters that can be monitored for a given strt_model.

**Description:** Starter BMDI Model Parameter  
**Table type:** REFERENCE  
**Primary key:** `STRT_MODEL_PARAMETER_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALARM_HIGH` | VARCHAR(20) |  |  | High Alarm Limit passed back to the application |
| 2 | `ALARM_LOW` | VARCHAR(20) |  |  | Low Alarm Limit passed back to the application |
| 3 | `DECIMAL_PRECISION` | DOUBLE |  |  | Specifies the number of significant decimal places for numeric types |
| 4 | `DEFAULT_ALIAS` | VARCHAR(50) |  |  | Parameter Alias sent by strt_model |
| 5 | `PARAMETER_CD` | DOUBLE | NOT NULL |  | Unique identifier for a parameter. |
| 6 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Result Type identifier code |
| 7 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | This value is used to standardize Model information across systems. |
| 8 | `STRT_MODEL_PARAMETER_ID` | DOUBLE | NOT NULL | PK | Unique identifier to be used as a primary key for this table. |
| 9 | `UNITS_CD` | DOUBLE | NOT NULL |  | Identifies Units code |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BMDI_DEVICE_PARAMETER](BMDI_DEVICE_PARAMETER.md) | `STRT_MODEL_PARAMETER_ID` |
| [STRT_BMDI_MODEL_NOMENCLATURE](STRT_BMDI_MODEL_NOMENCLATURE.md) | `STRT_MODEL_PARAMETER_ID` |

