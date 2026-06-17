# BB_PRINT_SERVER

> Contains Blood Bank print server information

**Description:** Blood Bank Print Server  
**Table type:** REFERENCE  
**Primary key:** `BB_PRINT_SERVER_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_PRINT_SERVER_ID` | DOUBLE | NOT NULL | PK | Contains an internal system assigned number that uniquely identifies a blood bank print server. |
| 6 | `IP_ADDR` | VARCHAR(50) | NOT NULL |  | Contains the network IP address of the blood bank print server. |
| 7 | `PORT_ADDR` | VARCHAR(50) | NOT NULL |  | Contains the address of the listening port of the blood bank print server. |
| 8 | `REDUN_PARENT_SERVER_ID` | DOUBLE | NOT NULL | FK→ | Contains the parent server identifier of the redundant server. |
| 9 | `SERVER_DESCRIPTION_TXT` | VARCHAR(100) | NOT NULL |  | The textual description of the blood bank print server. |
| 10 | `SERVER_NAME` | VARCHAR(50) | NOT NULL |  | The name of the blood bank print server. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REDUN_PARENT_SERVER_ID` | [BB_PRINT_SERVER](BB_PRINT_SERVER.md) | `BB_PRINT_SERVER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_PRINT_SERVER](BB_PRINT_SERVER.md) | `REDUN_PARENT_SERVER_ID` |
| [BB_SERVER_PRINTER_R](BB_SERVER_PRINTER_R.md) | `BB_PRINT_SERVER_ID` |

