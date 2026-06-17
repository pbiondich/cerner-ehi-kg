# EA_APPLICATION_TYPE

> This table will store the application type reference data.

**Description:** EA Application Type  
**Table type:** REFERENCE  
**Primary key:** `EA_APPLICATION_TYPE_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_TYPE_DESC` | VARCHAR(200) | NOT NULL |  | Description of the application type |
| 3 | `APPLICATION_TYPE_NAME` | VARCHAR(50) | NOT NULL |  | Unique name for the application type |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Timestamp when the record was created. |
| 5 | `CREATE_USER_NAME` | VARCHAR(50) | NOT NULL |  | Identifier of the user or system which created the record. |
| 6 | `EA_APPLICATION_TYPE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY. Database generated sequence number |
| 7 | `UPDATE_USER_NAME` | VARCHAR(50) | NOT NULL |  | Identifier of the user or system which updated the record. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EA_TRANSACTION_HIST](EA_TRANSACTION_HIST.md) | `EA_APPLICATION_TYPE_ID` |
| [EA_TRANSACTION_MAIN](EA_TRANSACTION_MAIN.md) | `EA_APPLICATION_TYPE_ID` |

