# LH_CNT_NHSN_EVENT_METRIC

> This table will store event metric mapped for facility and nurse unit through NHSN Location mapping utility

**Description:** LH_CNT_NHSN_EVENT_METRIC  
**Table type:** REFERENCE  
**Primary key:** `LH_CNT_NHSN_EVENT_METRIC_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CNT_NHSN_EVENT_METRIC_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_NHSN_EVENT_METRIC table. |
| 5 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This is field is the facility location for the event metric |
| 6 | `LOC_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This is field is the unit location within a facility for the event metric |
| 7 | `NHSN_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | This is the NHSN event type |
| 8 | `NHSN_METRIC_CD` | DOUBLE | NOT NULL |  | This is the NHSN HAI Metric Type |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CNT_NHSN_BENCHMARK](LH_CNT_NHSN_BENCHMARK.md) | `LH_CNT_NHSN_EVENT_METRIC_ID` |

