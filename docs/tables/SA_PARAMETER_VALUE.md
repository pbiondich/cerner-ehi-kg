# SA_PARAMETER_VALUE

> Contains individual values for the given SA_PARAMETER record contained on an anesthesia record. Based on the frequency they want to capture data and the length of case. For 1-minute intervals, 60 minute case it would be a 60:1 with SA_PARAMETER. For 5-minute intervals, 60 minute case it would be a 12:1 with SA_PARAMETER. Estimate max/year = 93,960,000

**Description:** SA Parameter Values  
**Table type:** ACTIVITY  
**Primary key:** `SA_PARAMETER_VALUE_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_IND` | DOUBLE |  |  | Indicates whether or not this value should be added to the persons chart, 1=Add to persons chart |
| 6 | `COPIED_FROM_VALUE_ID` | DOUBLE | NOT NULL | FK→ | The SA_PARAMETER_VALUE_ID this value was copied from. Will = 0 if not copied. |
| 7 | `DEVICE_ALIAS` | VARCHAR(40) |  |  | Alias of the BMDI monitor that feeds the result. |
| 8 | `EVENT_ID` | DOUBLE | NOT NULL |  | Clinical Event row for this parameter value |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The id to the long_text record for the comment associated to this value |
| 10 | `MONITORED_VALUE_IND` | DOUBLE |  |  | Monitor value indicator |
| 11 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | nomenclature_id for the parameter value |
| 12 | `NUMERIC_VALUE` | DOUBLE |  |  | Parameter Value |
| 13 | `PREVIOUS_PARAMETER_VALUE_ID` | DOUBLE | NOT NULL | FK→ | The id to the value record before the record was changed. If 0, this is the original unchanged value |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who added the value |
| 15 | `SA_PARAMETER_ID` | DOUBLE | NOT NULL | FK→ | The parent SA_PARAMETER record that this value is for |
| 16 | `SA_PARAMETER_VALUE_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the parameter value |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VALUE_DT_TM` | DATETIME |  |  | The date/time that the value applies to |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPIED_FROM_VALUE_ID` | [SA_PARAMETER_VALUE](SA_PARAMETER_VALUE.md) | `SA_PARAMETER_VALUE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PREVIOUS_PARAMETER_VALUE_ID` | [SA_PARAMETER_VALUE](SA_PARAMETER_VALUE.md) | `SA_PARAMETER_VALUE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_PARAMETER_ID` | [SA_PARAMETER](SA_PARAMETER.md) | `SA_PARAMETER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_PARAMETER_VALUE](SA_PARAMETER_VALUE.md) | `COPIED_FROM_VALUE_ID` |
| [SA_PARAMETER_VALUE](SA_PARAMETER_VALUE.md) | `PREVIOUS_PARAMETER_VALUE_ID` |

