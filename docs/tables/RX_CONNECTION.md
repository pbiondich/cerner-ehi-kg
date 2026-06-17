# RX_CONNECTION

> rx connection

**Description:** rx connection  
**Table type:** REFERENCE  
**Primary key:** `RX_CONNECTION_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONNECTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of internet connection a particular row represents. Examples would be a modem or VPN |
| 3 | `IP_ADDRESS` | VARCHAR(50) |  |  | Identifies IP_address that is connected |
| 4 | `MODEM` | DOUBLE |  |  | Identifies sequential modem number that is connected |
| 5 | `PORT` | VARCHAR(30) |  |  | Identifies Port logical that is connected |
| 6 | `RX_CONNECTION_ID` | DOUBLE | NOT NULL | PK | Unique key |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PHA_SWITCH_CONN_R](PHA_SWITCH_CONN_R.md) | `RX_CONNECTION_ID` |

