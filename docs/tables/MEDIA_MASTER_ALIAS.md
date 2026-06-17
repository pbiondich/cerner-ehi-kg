# MEDIA_MASTER_ALIAS

> Stores alias identifier to a Media Master record and alias type for that identifier

**Description:** Stores an identifier for a Media Master record  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | DOUBLE |  |  | The alias is an identifier (I.e., tracking id, container id) for a media master record. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Identifies a kind or type of alias (i.e., system defined number, etc.). They are Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 7 | `ALIAS_STR` | VARCHAR(200) |  |  | Alias field taking the place of "alias" (I4) to store the alpha-numeric alias for media. |
| 8 | `ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies a kind or type of alias (i.e., system defined number, etc.). They are Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `MEDIA_MASTER_ALIAS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media master alias table. It is an internal system assigned number. |
| 12 | `MEDIA_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MEDIA_MASTER_ID` | [MEDIA_MASTER](MEDIA_MASTER.md) | `MEDIA_MASTER_ID` |

