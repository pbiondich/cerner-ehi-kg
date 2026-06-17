# PDM_DATA_POINT

> Table used to store each group of PDM results

**Description:** Patient Data Monitoring Data Point  
**Table type:** ACTIVITY  
**Primary key:** `PDM_DP_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PDM_DP_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific patient data monitoring data point. |
| 5 | `PDM_PARAM_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific patient data monitoring parameters associated with the data point. Creates a relationship to the patient data monitoring parameters table. |
| 6 | `PDM_RANGE_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific patient data monitoring range associated with the data point. Creates a relationship to the patient data monitoring ranges table. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Defines the sequence of the next result in line. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [QC_RESULT](QC_RESULT.md) | `PDM_DP_ID` |

