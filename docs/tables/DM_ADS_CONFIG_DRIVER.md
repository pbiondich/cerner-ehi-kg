# DM_ADS_CONFIG_DRIVER

> Stores the driver keys for a client sample configuration. These driver keys control what data is replicated for the driver tables. All other activity tables will build on top of the driver table sample.

**Description:** DM_ACTIVITY_DATA_SAMPLER_CONFIGURATION_DRIVER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CUSTOM_IND` | DOUBLE |  |  | Indicates the driver key was manually loaded by a client (vs. being auto-generated) |
| 2 | `DM_ADS_CONFIG_DRIVER_ID` | DOUBLE | NOT NULL |  | Unique Identifier. Sequence based unique identifier for table. |
| 3 | `DM_ADS_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | Config_id the driver key belongs to. |
| 4 | `DM_ADS_EXTRACT_ID` | DOUBLE | NOT NULL | FK→ | The extract_id (driver_table) the driver_key belongs to |
| 5 | `DRIVER_KEY_ID` | DOUBLE | NOT NULL |  | The key for the driver table (e.g. person_id for person, product_id for product). dm_ads_extract_id (back to dm_ads_extract) gives a mapping back to what type of driver_key_id it is. (e.g. dm_ads_extract, extract_id=5, table_name = PERSON, driver_keycol_name = PERSON_ID). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_ADS_CONFIG_ID` | [DM_ADS_CONFIG](DM_ADS_CONFIG.md) | `DM_ADS_CONFIG_ID` |
| `DM_ADS_EXTRACT_ID` | [DM_ADS_EXTRACT](DM_ADS_EXTRACT.md) | `DM_ADS_EXTRACT_ID` |

