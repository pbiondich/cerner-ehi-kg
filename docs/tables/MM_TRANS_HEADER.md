# MM_TRANS_HEADER

> mm trans header

**Description:** Transaction Header  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 34  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | batch identifier value |
| 2 | `BATCH_SUBMIT_DT_TM` | DATETIME |  |  | identifies the date and time that the batch was submitted to FSI |
| 3 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 6 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 7 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to distribution table |
| 8 | `DIST_NBR` | VARCHAR(40) |  |  | Distribution Number |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to the parent table that caused the inventory transaction |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Table name of the foreign key referenced in the parent_entity_id attribute. |
| 12 | `PARENT_ENTITY_REF` | VARCHAR(40) |  |  | A description of the type of data stored in the PARENT_ENTITY_ID/PARENT_ENTITY_NAME columns. |
| 13 | `PO_NBR` | VARCHAR(40) |  |  | PO Number |
| 14 | `PO_RECEIPT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to po_receipt table |
| 15 | `PO_RECEIPT_NBR` | VARCHAR(10) |  |  | The receipt sequence number. |
| 16 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Purchase Order ID |
| 17 | `REQUISITION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to requisition table |
| 18 | `REQ_NBR` | VARCHAR(40) |  |  | Requisition Number |
| 19 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Transaction ID |
| 20 | `TRANS_APP_NAME` | VARCHAR(60) |  |  | Application which created this transaction. |
| 21 | `TRANS_DT_TM` | DATETIME | NOT NULL |  | Date this transaction was created. |
| 22 | `TRANS_NUMBER` | VARCHAR(40) |  |  | Transaction Number. |
| 23 | `TRANS_PERSON_ID` | DOUBLE | NOT NULL | FK→ | User id of person who created this transaction |
| 24 | `TRANS_PERSON_NAME` | VARCHAR(100) |  |  | User name of person who created this transaction. |
| 25 | `TRANS_REQ_NAME` | VARCHAR(40) |  |  | Request which created this transaction. |
| 26 | `TRANS_TASK_NAME` | VARCHAR(60) |  |  | Task which created this transaction. |
| 27 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction type code value |
| 28 | `TRANS_TYPE_DESC` | VARCHAR(60) |  |  | Description of the Transaction Type. |
| 29 | `TRANS_TYPE_DISP` | VARCHAR(40) |  |  | Display of the Transaction Type. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [SI_BATCH](SI_BATCH.md) | `BATCH_ID` |
| `DISTRIBUTION_ID` | [DISTRIBUTION](DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PO_RECEIPT_ID` | [PO_RECEIPT](PO_RECEIPT.md) | `PO_RECEIPT_ID` |
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |
| `REQUISITION_ID` | [REQUISITION](REQUISITION.md) | `REQUISITION_ID` |
| `TRANS_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MM_LOT_RELTN](MM_LOT_RELTN.md) | `TRANSACTION_ID` |
| [MM_TRANS_ERROR_LOG](MM_TRANS_ERROR_LOG.md) | `TRANSACTION_ID` |
| [MM_TRANS_GL](MM_TRANS_GL.md) | `TRANSACTION_ID` |

