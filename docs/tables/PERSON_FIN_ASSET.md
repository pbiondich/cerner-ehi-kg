# PERSON_FIN_ASSET

> Records a person's financial assets (examples include bank accounts, vehicles, real estate etc.)

**Description:** Person Financial Asset  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_FIN_ASSET_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ASSET_DETAIL_TXT` | VARCHAR(255) |  |  | The freetext description which gives additional information about the person's financial asset. |
| 6 | `ASSET_TYPE_CD` | DOUBLE | NOT NULL |  | The financial asset type code defines the tyep of asset (for example: bank accounts, vehicles, re estate properties, etc.) |
| 7 | `ASSET_VALUE` | DOUBLE |  |  | The monetary value of the financial asset as defined by the person's financial asset type code. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the parent table to which the person's financial asset row is related. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The upper case name of the table to which this person's financial asset is related (for example: person, financial_case, etc.) |
| 10 | `PERSON_FIN_ASSET_ID` | DOUBLE | NOT NULL | PK | Uniquely generated number to identify a row on the PERSON_FIN_ASSET table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the financial asset was last verified. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_FIN_ASSET_HIST](PERSON_FIN_ASSET_HIST.md) | `PERSON_FIN_ASSET_ID` |

