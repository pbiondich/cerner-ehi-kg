# GUAR_FINANCIAL_RESP

> The Guarnator Financial Responsibility table defines financial responsibility of the guarantor.

**Description:** Guarantor Financial Responsibility  
**Table type:** ACTIVITY  
**Primary key:** `GUAR_FINANCIAL_RESP_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIN_RESP_QUAL_CD` | DOUBLE | NOT NULL |  | The financial qualifier code defines the type of value (i.e. monetary amount or percentage) for which the guarantor is responsible. |
| 8 | `FIN_RESP_VALUE` | DOUBLE | NOT NULL |  | The financial responsibility value as defined by the qualifier code for which the guarantor is responsible. |
| 9 | `GUAR_FINANCIAL_RESP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the GUAR_FINANCIAL_RESP table. |
| 10 | `GUAR_FINANCIAL_RESP_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the scope of the guarantor¿s financial responsibility. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [GUAR_FINANCIAL_RESP_HIST](GUAR_FINANCIAL_RESP_HIST.md) | `GUAR_FINANCIAL_RESP_ID` |
| [GUAR_FIN_RESP_RELTN](GUAR_FIN_RESP_RELTN.md) | `GUAR_FINANCIAL_RESP_ID` |
| [GUAR_FIN_RESP_RELTN_HIST](GUAR_FIN_RESP_RELTN_HIST.md) | `GUAR_FINANCIAL_RESP_ID` |

