# DM_ADS_EXTRACT_STG

> Stores unscrambled data from DM_ADS_EXTRACT for purposes of troubleshooting and manually modifying data back into DM_ADS_EXTRACT.

**Description:** DM_ACTIVITY_DATA_SAMPLER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLY_WHERE_IND` | DOUBLE |  |  | Indicates if the where_clause will be performed during an ADS replicate. Should be set to 1 when: Extract_method in 'BYCONFIG','STATIC' |
| 3 | `DATA_CLASS_TYPE` | VARCHAR(30) |  |  | Indicates the type of extract, values: ACTIVITY, ACTIVITY-MIXED, MIXED, REFERENCE, REFERENCE-MIXED |
| 4 | `DM_ADS_EXTRACT_STG_ID` | DOUBLE | NOT NULL |  | Sequence based unique identifier for table. |
| 5 | `DRIVER_KEYCOL_NAME` | VARCHAR(30) |  |  | There driver column name used to retrieve the sample keys. |
| 6 | `DRIVER_RANKCOL_NAME` | VARCHAR(30) |  |  | The column by which columns should be ranked. Future use, in case the config_method of CURRENT is chosen and we want to rank on a column that is not the unique key for the table. (e.g. Get Current person_ids by highest updt_dt_tm vs. by highest person_id). |
| 7 | `DRIVER_TABLE_IND` | DOUBLE |  |  | Indicates if the table is an Activity driver table. |
| 8 | `DRIVER_TABLE_NAME` | VARCHAR(30) |  |  | The Ultimate driver parent table name for the extract. For activity data, it will be a table in this table where driver_table_ind =1. For reference data, this field will be null. For Activity extracts where the extract_method = ALL, the driver table may be also be blank (if increasing driver keys cannot impact the data for the extract). |
| 9 | `DUPDEL_SKIP_IND` | DOUBLE |  |  | Dupe Delete. - Indicate where we may not want to perform a duplicate row cleanup for tables with multiple extracts. |
| 10 | `EXPIMP_LEVEL_NBR` | DOUBLE |  |  | The logical order/level/priority in which the extract should be performed, such that any and all parent tables are extracted to ensure data is properly extracted. |
| 11 | `EXPIMP_PARENT_TABLE_NAME` | VARCHAR(30) |  |  | The table's immediate parent table on which the extract is driven. |
| 12 | `EXTRACT_METHOD` | VARCHAR(30) |  |  | Indicates the method of extraction during replicates:ALL: The entire table is moved. BYCONFIG: The table is moved by the clients specified configuration method and pct values (Clients will have METHODs of RECENT, EVERYNTH) and can specify how much activity data to move by pct (10%, 20% etc.). Typically, this means the where clause for this will reference the immediate parent table. EVERYNTHPCT: The table will sample every nth row based on the client's configuration pct. These are typicall |
| 13 | `OWNER_NAME` | VARCHAR(30) | NOT NULL |  | Owner of the table being extracted |
| 14 | `TABLE_COMMENT` | VARCHAR(2000) |  |  | Any information useful to describe / document how the extract is related to the Millennium data model. May be used by Cerner support organizations to better understand, use the data for clients. |
| 15 | `TABLE_EXTRACT_INSTANCE_NBR` | DOUBLE | NOT NULL |  | Instance/Version of the extract for a table (in case we want to ship multiple versions that can be active). |
| 16 | `TABLE_EXTRACT_NBR` | DOUBLE | NOT NULL |  | Extract number for a table |
| 17 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Table being extracted |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `WHERE_CLAUSE` | VARCHAR(4000) |  |  | The where_clause the extract will use to get the intended data, either for an activity based sample, referenced-mixed data,etc.. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

