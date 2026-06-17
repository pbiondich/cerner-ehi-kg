# NETTING

> Short for container/accession/order netting. Processed by the netting server when it is time to net orders.

**Description:** Netting  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | An accession number identifies an order or a group of orders. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies an accession number. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (such as PathNet or RadNet) and/or what department (such as General Lab or Microbiology) an order belongs. |
| 4 | `ALIQUOT_PRINTER_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies an aliquot label printer. |
| 5 | `BED_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Bed Code. The nursing unit will determine the location where the label is printed. |
| 6 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Body Site Code. |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Catalog Code. |
| 8 | `COLLECTED_IND` | DOUBLE |  |  | The collection status of an order (0 - not collected, 1 - collected). |
| 9 | `COLLECTION_COMMENT` | VARCHAR(200) |  |  | The collection comment (label comment) for an order. |
| 10 | `COLLECTION_DT_TM` | DATETIME |  |  | The collection date and time for an order. |
| 11 | `COLLECTION_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies the collector of an order. |
| 12 | `COLLECTION_LIST_ID` | DOUBLE | NOT NULL |  | Unique system identifier for a collection list or transfer list. |
| 13 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Collection Method Code. |
| 14 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Collection Priority Code. |
| 15 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | Unique identifier for the container that was associated with the order. |
| 16 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies a group orders to be netted. |
| 17 | `LABEL_FILE_PREFIX` | VARCHAR(5) |  |  | The file prefix used to identify a label file. |
| 18 | `LABEL_PRINTER_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies a label printer. |
| 19 | `MEDIA_PRINTER_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies a media printer. |
| 20 | `NETTING_STATUS` | DOUBLE |  |  | The status of a netting. Status: 0 - Default. 1 - Active netting row. 4 - Inactive netting row. 5 - Cancelled netting row. 150 - Error In Netting. |
| 21 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Nursing Unit Code. The nursing unit will determine the location where the label is printed. |
| 22 | `ORDER_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies an order. |
| 23 | `ORDER_LOCATION_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Order Location Code. |
| 24 | `PRINT_QUEUE` | VARCHAR(250) |  |  | The description of the label printer queue. Currently Not Used. |
| 25 | `PROCESSING_FLAG` | DOUBLE |  |  | A flag indicating the source of a netting row. |
| 26 | `PROP_ID` | DOUBLE | NOT NULL |  | The identifier of the row in the prop_queue table. |
| 27 | `RECEIVED_DT_TM` | DATETIME |  |  | The received date and time of the order. |
| 28 | `RECEIVED_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies the collector of an order. |
| 29 | `RECEIVED_LOCATION_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Received Location code. |
| 30 | `REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Reporting Priority Code. |
| 31 | `ROOM_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Room Code. The nursing unit will determine the location where the label is printed. |
| 32 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system as a code value for the Specimen Type Code. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

