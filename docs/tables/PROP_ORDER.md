# PROP_ORDER

> Order information for PROP orders.

**Description:** Contains the order infomation for PROP orders.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The accession for the order. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the accession for the order. |
| 3 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Indicates the processing the PathNet Result Order Posting Server will perform. |
| 4 | `APPLICATION_CD` | DOUBLE | NOT NULL |  | Identifies the application placing the order. |
| 5 | `APPLICATION_FLAG` | DOUBLE |  |  | Order application specific flag whose value is determined by the client application. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code of the orderable. |
| 7 | `COLLECTION_LIST_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the collection list, if the order is associated with one. |
| 8 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The collection method of the order. |
| 9 | `COMMENT_FLAG` | DOUBLE |  |  | Indicates that comments exist on the prop_comment table. |
| 10 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The code value identifying the communication type of the order. |
| 11 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 12 | `CS_FLAG` | DOUBLE |  |  | This flag indicates whether this order is a parent or member of a CareSet. |
| 13 | `CS_ITEMS` | DOUBLE |  |  | Indicates the number of CareSet child rows for a CareSet parent. |
| 14 | `CS_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Parent Order ID of a CareSet child. |
| 15 | `DEFAULT_DT_TM` | DATETIME |  |  | The date and time the PathNet Result Order Posting server defaults for order details. This is the date and time from the PC. |
| 16 | `DETAIL_FLAG` | DOUBLE |  |  | Indicates that order details exist on the prop_detail table. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 18 | `LABEL_FILE_PREFIX` | VARCHAR(5) |  |  | The file prefix used to identify a label file. |
| 19 | `LABEL_PRINTER_ID` | DOUBLE | NOT NULL | FK→ | The output destination for the labels. |
| 20 | `ORDER_DT_TM` | DATETIME |  |  | The date and time the order was placed. |
| 21 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Unique number that ties the order laboratory row to the orders tables. |
| 22 | `ORDER_LOCATION_CD` | DOUBLE | NOT NULL |  | The location where the order was placed. |
| 23 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | The primary or HNA order mnemonic for this orderable. |
| 24 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL |  | The ID of the ordering provider. |
| 25 | `PERSONNEL_ID` | DOUBLE | NOT NULL |  | The ID of the personnel that generated the action. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 27 | `PREVIOUS_ACTION_FLAG` | DOUBLE |  |  | The previous action that was performed for this order. |
| 28 | `PROP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the row in the table. |
| 29 | `RECEIVED_LOCATION_CD` | DOUBLE | NOT NULL |  | The received location of the specimen. |
| 30 | `RESULT_FLAG` | DOUBLE |  |  | Indicates the result exists on the prop_result table. |
| 31 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource to which the order loaded. |
| 32 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The specimen type of the order. |
| 33 | `START_DT_TM` | DATETIME |  |  | The start date and time for the order. |
| 34 | `STATUS_FLAG` | DOUBLE |  |  | The status of the action flag |
| 35 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Id of the synonym for this order. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 41 | `VERIFY_FLAG` | DOUBLE |  |  | Indicates that the order needs to verified before it is placed in the system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `COLLECTION_LIST_ID` | [COLLECTION_LIST](COLLECTION_LIST.md) | `COLLECTION_LIST_ID` |
| `CS_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LABEL_PRINTER_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROP_ID` | [PROP_ACTION](PROP_ACTION.md) | `PROP_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

