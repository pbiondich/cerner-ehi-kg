# DM_ADS_CONFIG_EXTRACT

> Stores the result of a driver key generation process initiated for an ADS config (client defined method/pct).

**Description:** DM_ACTIVITY_DATA_SAMPLER_CONFIGURATION_EXTRACT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME |  |  | The date/time the driver key generation process started for the driver table. |
| 2 | `DM_ADS_CONFIG_EXTRACT_ID` | DOUBLE | NOT NULL |  | Unique Identifier. Sequence based unique identifier for table. |
| 3 | `DM_ADS_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | Config_id for the driver_table |
| 4 | `DM_ADS_EXTRACT_ID` | DOUBLE | NOT NULL | FK→ | Extract_id for the driver table |
| 5 | `DM_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The related id from DM_PROCESS_QUEUE row that the driver key generation process also generated for the driver table. |
| 6 | `END_DT_TM` | DATETIME |  |  | The date/time the driver key generation process ended for the driver table. |
| 7 | `MESSAGE_TXT` | VARCHAR(4000) |  |  | Holds any error messages that may have occurred from the driver key generation process. |
| 8 | `ROW_SAMPLE_NBR` | DOUBLE |  |  | The number of sample keys generated. |
| 9 | `STATUS_TXT` | VARCHAR(15) |  |  | The status of the driver key generation process for the driver key extract. |
| 10 | `TARGET_SAMPLE_METHOD` | VARCHAR(30) |  |  | The client requested sample method for the driver table (RECENT \| EVERYNTH \| CUSTOM) |
| 11 | `TARGET_SAMPLE_PERCENT_NBR` | DOUBLE |  |  | The client requested sample percent when the driver table keys were last generated. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_ADS_CONFIG_ID` | [DM_ADS_CONFIG](DM_ADS_CONFIG.md) | `DM_ADS_CONFIG_ID` |
| `DM_ADS_EXTRACT_ID` | [DM_ADS_EXTRACT](DM_ADS_EXTRACT.md) | `DM_ADS_EXTRACT_ID` |
| `DM_PROCESS_QUEUE_ID` | [DM_PROCESS_QUEUE](DM_PROCESS_QUEUE.md) | `DM_PROCESS_QUEUE_ID` |

