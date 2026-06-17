# ORM_ERROR_LOG

> Stores clinical and system admin information for failed asynch orm transactions.

**Description:** Order Management Error Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The dt/tm the action was received by the system. |
| 2 | `ACTION_STATUS_FLAG` | DOUBLE |  |  | Describes the action. 0 - None 1 - Success 2 - Action Error 3 - Group Error |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The code representing the action that was attempted. |
| 4 | `APPLICATION_NUMBER` | DOUBLE |  |  | The number of the application used to initiate the transaction. |
| 5 | `CLIENT_NODE_NAME` | VARCHAR(255) | NOT NULL |  | The name of the node the program was when it initiated the transaction. |
| 6 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The code representing the way the requesting personnel communicated that the action be taken to the personnel that submitted the action. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter that the order was associated with when the action occurred. |
| 8 | `ERROR_NBR` | DOUBLE |  |  | The numeric representation of the generic error that occurred. |
| 9 | `ERROR_SPECIFIC_NBR` | DOUBLE |  |  | The numeric representation of the specific error that occurred. |
| 10 | `ERROR_SPECIFIC_STRING` | VARCHAR(1000) |  |  | The system administrator interpretation of the error that occurred. |
| 11 | `ERROR_STRING` | VARCHAR(1000) |  |  | The functional interpretation of the error that occurred. |
| 12 | `INGREDIENT_MNEMONICS` | VARCHAR(2000) |  |  | The mnemonics of the ingredients sent on the order. |
| 13 | `LONG_BLOB` | LONGBLOB |  |  | Stores the request sent to the Order Write Server when the error item is processed. |
| 14 | `ORDERED_AS_MNEMONIC` | VARCHAR(255) |  |  | The mnemonic used to place the order the action was applied to. |
| 15 | `ORDER_CONVERSATION_ID` | DOUBLE | NOT NULL |  | The identifier of the transaction that contained the action. While this column is populated from sequence ORDER_SEQ, it is not related to a primary key column. |
| 16 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order the action was applied to. |
| 17 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that requested the action be submitted. |
| 18 | `ORM_ERROR_LOG_ID` | DOUBLE | NOT NULL |  | Unique identifier to this table. |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person that is the subject of the order. |
| 20 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel that submitted the action. |
| 21 | `REQUESTED_START_DT_TM` | DATETIME |  |  | The dt/tm the order was requested to start. |
| 22 | `REQUESTED_START_TZ` | DOUBLE |  |  | Time zone associated with the requested_start_dt_tm column. |
| 23 | `REQUEST_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the row on the long_blob table that is storing the transaction. |
| 24 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | The name of the request used to initiate the transaction. |
| 25 | `REQ_INDEX` | DOUBLE |  |  | The item in the request that points to the failed action. |
| 26 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the synonym representing the orderable the action was applied to. |
| 27 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | The name of the task used to initiate the transaction. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `USERNAME` | VARCHAR(50) | NOT NULL |  | The username of the person logged into the program that initiated the transaction. |
| 34 | `USER_TYPE_FLAG` | DOUBLE |  |  | Describes the user that placed the transaction with the failed action. 0 - Normal 1 - System |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUEST_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

