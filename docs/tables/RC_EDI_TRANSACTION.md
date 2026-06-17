# RC_EDI_TRANSACTION

> Stores all the EDI transaction details related to pricing.

**Description:** Revenue Cycle EDI Transaction  
**Table type:** ACTIVITY  
**Primary key:** `RC_EDI_TRANSACTION_ID`  
**Columns:** 28  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 3 | `CALL_BACK_HANDLER_IDENT` | DOUBLE |  |  | To persist the call back handler identifier corresponding to each transaction request, for handling response. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXT_BATCH_IDENT` | VARCHAR(250) |  |  | External batch identifier used to identify a group of related transactions. |
| 7 | `EXT_GROUP_IDENT` | VARCHAR(250) |  |  | The Ticket number (EDI number) provided by the cloud service. |
| 8 | `EXT_PARTNER_IDENT` | VARCHAR(250) |  |  | The 3rd party identification number provided by cloud service. |
| 9 | `HTTP_STATUS_CODE` | DOUBLE | NOT NULL |  | Contains the HTTP status code for a given request. |
| 10 | `HTTP_STATUS_DESC` | VARCHAR(250) |  |  | Contains the corresponding HTTP status description. |
| 11 | `MAX_RETRY_CNT` | DOUBLE | NOT NULL |  | The maximum number of retries allowed for this corresponding transaction. |
| 12 | `ORIG_RC_EDI_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | FK from the original RC_EDI_TRANSACTION_ID value. Used for versioning. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary data source corresponding to this EDI transaction. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The entity name (ex: PFT_ENCNTR, CHARGE, BILLING_ENTITY) describing the primary source entity data corresponding to that EDI transaction. |
| 15 | `RC_EDI_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the PFT_EDI_TRANSACTION table. |
| 16 | `REPLY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Reply Long Text ID |
| 17 | `REQUEST_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Request Long Text ID |
| 18 | `RESOURCE_URL` | VARCHAR(3200) | NOT NULL |  | Contains the endpoint resource URL. |
| 19 | `RETRIEVE_DT_TM` | DATETIME |  |  | The EDI Transaction reply(response) received date and time(timestamp). |
| 20 | `RETRY_CNT` | DOUBLE | NOT NULL |  | The count indicating the number of retry on edi transmission performed for that particular ticket id. |
| 21 | `SERVICE_CD` | DOUBLE | NOT NULL |  | The service code indicating the service using this EDI transaction record. |
| 22 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status code representing the current status of this EDI transaction. |
| 23 | `TRANSMIT_DT_TM` | DATETIME | NOT NULL |  | The EDI Transaction request transmit date and time(timestamp). |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_RC_EDI_TRANSACTION_ID` | [RC_EDI_TRANSACTION](RC_EDI_TRANSACTION.md) | `RC_EDI_TRANSACTION_ID` |
| `REPLY_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REQUEST_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_EDI_TRANSACTION](RC_EDI_TRANSACTION.md) | `ORIG_RC_EDI_TRANSACTION_ID` |

