# ESI_LOG

> External System Interface Inbound Log Table

**Description:** ESI LOG  
**Table type:** ACTIVITY  
**Primary key:** `ESI_LOG_ID`  
**Columns:** 59  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | Accession id from the inbound HL7 messageColumn |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BATCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This is the primary key from the SI_BATCH_EVENT table.Column |
| 7 | `BINDING` | VARCHAR(32) |  |  | This is the server"s binding parameter in SCP. |
| 8 | `CARE_SET_FLAG` | DOUBLE |  |  | This determines whether the order is a parent or a member of a CareSet. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time the row was created. |
| 11 | `CREATE_TIME` | DOUBLE | NOT NULL |  | The time in Milliseconds when the record was written |
| 12 | `DOMAIN_ERROR_STAT_CD` | DOUBLE | NOT NULL |  | This is the error code from an asynchronous domain server or script during the processing of a transaction. Its purpose is to track the status of a transaction after its release from ESI. |
| 13 | `DOMAIN_ERROR_TEXT` | VARCHAR(500) |  |  | This is the error(s) encountered during the domain"s transaction processing. |
| 14 | `ENCNTR_ALIAS` | VARCHAR(255) |  |  | Encounter Aliases related to the incoming message |
| 15 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `END_DT_TM` | DATETIME |  |  | This is the date and time the transaction was completed. |
| 17 | `END_TIME` | VARCHAR(16) |  |  | This is the time when ESI finished processing. |
| 18 | `ENTITY_COUNT` | DOUBLE |  |  | This is the number of identifiers created for an Entity Name. For example, if the Entity Name is 'ORDERS' and the entity count is 8, then eight orders where placed for the transaction. |
| 19 | `ENTITY_LIST` | VARCHAR(128) |  |  | This is a list of identifiers if more than one identifier was generated for this transaction. For example, if the Entity Name is 'ORDERS' and the Entity List is '1000, 10001, 10002,' then three additional orders with order_ids of 1000, 10001, and 10002 were created (in addition to the order in theorder_id column). |
| 20 | `ENTITY_NAME` | VARCHAR(32) |  |  | This is the Entity Name for the primary table that was added for the transaction, e.g., 'ORDERS', 'CLINICAL_EVENT,' 'SCH_SCHEDULE.' |
| 21 | `ERROR_STAT` | VARCHAR(32) |  |  | This is a string describing the transaction's status. Examples are SUCCESS, WARNING, RETRY, FAILURE, TERMINAL, TERMINATE. |
| 22 | `ERROR_TEXT` | VARCHAR(500) |  |  | This is the error(s) encountered during transaction processing. |
| 23 | `ESI_INSTANCE` | DOUBLE |  |  | This is the instance number of the ESI Server. |
| 24 | `ESI_LOG_ID` | DOUBLE | NOT NULL | PK | This is the Primary Key for the Esi_Log table. |
| 25 | `ESI_LOG_ORIG_ID` | DOUBLE | NOT NULL |  | This is the original ESI_LOG_ID value. When the row is updated, a new row will actually be added with a new key. This field will associate the new row to the original row. This field, in conjunction with the ACTIVE family columns, will be used to track changes to a row. |
| 26 | `ESI_TX_KEY` | VARCHAR(27) |  |  | This is the transaction key from the oen_txlog table that the esi comserver logged. |
| 27 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for an event. |
| 28 | `HL7_ACCESSION_NBR` | VARCHAR(20) |  |  | Accession number from inbound HL7 messageColumn |
| 29 | `HL7_ENTITY_ALIAS` | VARCHAR(255) |  |  | This is the unique identifier the sending system uses to identify the entity processed. |
| 30 | `HL7_ENTITY_CODE` | VARCHAR(128) |  |  | This is the alias to the code to identify a specific order, result, schedule, etc. For example, for orders this is the code to identify a particular order catalog, e.g., 122200, if 122200 is an alias to a catalog code such as CBC. |
| 31 | `HOLD_ALIAS_FLAG` | DOUBLE |  |  | This field identifies the alias type that was received and configured to release items from hold. Examples are 1 for person_alias, 2 for encntr_alias, and 4 for order_alias. Each is the binary representation, so multiple release items can be identified. |
| 32 | `HOLD_RELEASE_STAT` | DOUBLE |  |  | This field identifies the error status returned from the Hold Release Server. |
| 33 | `INTERNAL_MESSAGE_IDENT` | VARCHAR(40) |  |  | System generated message identifier |
| 34 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Associated row onthe LONG_BLOB table which contains additional status information |
| 35 | `MESSAGE_TRIGGER_CD` | DOUBLE |  |  | UI message trigger codeColumn |
| 36 | `MSGID` | VARCHAR(16) |  |  | This is the unique transaction identifier used by the Open Port Com Client. This identifier will reference a raw HL7 transaction on the oen_txlog table. |
| 37 | `MSH_CTRL_IDENT` | VARCHAR(100) |  |  | This is the MSH Control Identifier. |
| 38 | `MSH_DATE` | VARCHAR(32) |  |  | This is the MSH Date and Time. |
| 39 | `MSH_MSG_TRIG` | VARCHAR(8) |  |  | This is the MSH Message Event Trigger, e.g., A01, A02. |
| 40 | `MSH_MSG_TYPE` | VARCHAR(8) |  |  | This is the MSH Message Type |
| 41 | `MSH_SENDING_APP` | VARCHAR(32) |  |  | This is the MSH Sending Application. |
| 42 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | This is the Person"s full formatted name. |
| 43 | `ORDER_CTRL` | VARCHAR(8) |  |  | This is the ORC Order Control Field, e.g., NW, CA. |
| 44 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is the Order identifier. |
| 45 | `PERSON_ALIAS` | VARCHAR(255) |  |  | Person Aliases related to the incoming message. |
| 46 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 47 | `PROCD_RESTORE_FLAG` | DOUBLE | NOT NULL |  | Describes the restore action of the ESI transaction. 0 = no restore; 1 = restore on matched person; 2 = restore on merged person; 3 = restore on matched and merge persons; 4 = restore on reconciled persons; 5 = restore on matched and reconciled persons; 6 = restore on merged and reconciled persons; 7 = restore on matched, merged, and reconciled persons |
| 48 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | This is the primary key from the CQM_OENINTERFACE_QUE tableColumn |
| 49 | `REFERRAL_ID` | DOUBLE |  | FK→ | Uniquely identifies the related referral documents. |
| 50 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This is the unique schedule identifier. |
| 51 | `START_DT_TM` | DATETIME |  |  | This is the date and time the transaction entered the ESI Server. |
| 52 | `START_TIME` | VARCHAR(16) |  |  | This is the time when ESI received a transaction. |
| 53 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | This is the primary key from the TASK_ACTIVITY table.Column |
| 54 | `TX_KEY` | VARCHAR(27) |  |  | This is the transaction key from the oen_txlog table that the inbound comserver logged. |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `BATCH_EVENT_ID` | [SI_BATCH_EVENT](SI_BATCH_EVENT.md) | `BATCH_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ESI_SCRIPT_USAGE](ESI_SCRIPT_USAGE.md) | `ESI_LOG_ID` |
| [RX_PENDING_REFILL](RX_PENDING_REFILL.md) | `ESI_LOG_ID` |
| [RX_REFILL_HX](RX_REFILL_HX.md) | `ESI_LOG_ID` |

