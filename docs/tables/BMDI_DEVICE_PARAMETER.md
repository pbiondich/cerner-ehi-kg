# BMDI_DEVICE_PARAMETER

> Identifies the parameters that can be monitored for a given device.

**Description:** BMDI Device Parameter  
**Table type:** REFERENCE  
**Primary key:** `DEVICE_PARAMETER_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALARM_HIGH` | VARCHAR(20) |  |  | High Alarm Limit passed back to the application |
| 3 | `ALARM_LOW` | VARCHAR(20) |  |  | Low Alarm Limit passed back to the application |
| 4 | `DECIMAL_PRECISION` | DOUBLE |  |  | Specifies the number of significant decimal places for numeric types |
| 5 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Used to identify parameters across service resources. |
| 6 | `DEVICE_PARAMETER_ID` | DOUBLE | NOT NULL | PK | Provide a unique primary key |
| 7 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event Code Value |
| 8 | `PARAMETER_ALIAS` | VARCHAR(60) | NOT NULL |  | Parameter Alias sent by device. |
| 9 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Result Type Code identifier |
| 10 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Controls the order in which the parameter displays relative to other parameters for a particular device and relative to other parameters. |
| 11 | `STRT_MODEL_PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a parameter. From STRT_BMDI_MODEL_PARAMETER TABLE |
| 12 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code Value |
| 13 | `UNITS_CD` | DOUBLE | NOT NULL |  | Identifies UnitsColumn |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `STRT_MODEL_PARAMETER_ID` | [STRT_BMDI_MODEL_PARAMETER](STRT_BMDI_MODEL_PARAMETER.md) | `STRT_MODEL_PARAMETER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BMDI_ACQUIRED_RESULTS](BMDI_ACQUIRED_RESULTS.md) | `DEVICE_PARAMETER_ID` |
| [BMDI_DEVICE_NOMENCLATURE](BMDI_DEVICE_NOMENCLATURE.md) | `DEVICE_PARAMETER_ID` |

