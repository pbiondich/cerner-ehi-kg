# EA_TRANSACTION_MAIN

> This table will store transaction information for Millennium. This data will be used to drive a Java User Management GUI, CCL reports and the Lights on Network.

**Description:** EA Main Transaction  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NAME` | VARCHAR(100) | NOT NULL |  | Name of the solution |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Timestamp when the record was created. |
| 3 | `CREATE_USER_NAME` | VARCHAR(50) | NOT NULL |  | Identifier of the user or system which created the record. |
| 4 | `DEVICE_ADDRESS` | VARCHAR(50) | NOT NULL |  | Device identification being used |
| 5 | `DOMAIN_NAME` | VARCHAR(50) | NOT NULL |  | Name of the Millennium domain |
| 6 | `EA_APPLICATION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | APPLICATION TYPE value. Foreign key from EA_APPLICATION_TYPE table |
| 7 | `EA_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Status. Foreign Key value from EA_STATUS table. |
| 8 | `EA_TRANSACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. Database generated sequence number |
| 9 | `EA_TRANSACTION_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Transaction Type. Foreign key value from EA_TRANSACTION_TYPE table. |
| 10 | `LAST_ACTIVITY_DT_TM` | DATETIME |  |  | Timestamp of the last recorded activity for the user. |
| 11 | `NODE_NAME` | VARCHAR(50) | NOT NULL |  | Name of the Millennium node |
| 12 | `TRANSACTION_COMMENT` | VARCHAR(255) | NOT NULL |  | Comment field to be used for extra remarks required for certain transactions. |
| 13 | `UPDATE_USER_NAME` | VARCHAR(50) | NOT NULL |  | Identifier of the user or system which updated the record. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `USER_NAME` | VARCHAR(50) | NOT NULL |  | Username of the requesting user |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EA_APPLICATION_TYPE_ID` | [EA_APPLICATION_TYPE](EA_APPLICATION_TYPE.md) | `EA_APPLICATION_TYPE_ID` |
| `EA_STATUS_ID` | [EA_STATUS](EA_STATUS.md) | `EA_STATUS_ID` |
| `EA_TRANSACTION_TYPE_ID` | [EA_TRANSACTION_TYPE](EA_TRANSACTION_TYPE.md) | `EA_TRANSACTION_TYPE_ID` |

