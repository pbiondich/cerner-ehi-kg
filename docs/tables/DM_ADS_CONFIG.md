# DM_ADS_CONFIG

> Stores a client specific sampling configuration by name.

**Description:** DM_ACTIVITY_DATA_SAMPLER_CONFIGURATION  
**Table type:** ACTIVITY  
**Primary key:** `DM_ADS_CONFIG_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_NAME` | VARCHAR(120) | NOT NULL |  | Client supplied name (AK1) |
| 2 | `CONFIG_STATUS` | VARCHAR(30) |  |  | The status of the Client's sample configuration. Valid values = COMPLETE, NEEDSBUILD, FAILED, INCOMPLETE, EXECUTING |
| 3 | `DM_ADS_CONFIG_ID` | DOUBLE | NOT NULL | PK | Unique Identifier. Sequence based unique identifier for table. |
| 4 | `SAMPLE_METHOD` | VARCHAR(30) |  |  | The sampling method for the Clients sample configuration. Valid values are: RECENT, EVERYNTH, CUSTOM |
| 5 | `SAMPLE_PERCENT_NBR` | DOUBLE |  |  | The sampling percent for the client's sample configuration. Valid values are (.01 - 100). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_ADS_CONFIG_DRIVER](DM_ADS_CONFIG_DRIVER.md) | `DM_ADS_CONFIG_ID` |
| [DM_ADS_CONFIG_EXTRACT](DM_ADS_CONFIG_EXTRACT.md) | `DM_ADS_CONFIG_ID` |

