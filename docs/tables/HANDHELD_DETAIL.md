# HANDHELD_DETAIL

> This table will be used to store the detailed information regarding each handheld collection upload event. This table is used for reporting purposes only.

**Description:** Handheld Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | The accession number for this collection detail. |
| 2 | `ALIAS1` | VARCHAR(200) |  |  | One of the person aliases entered to identify the patient. If known based on the barcode format, this will be the patients identifier on the patient wristband. |
| 3 | `ALIAS2` | VARCHAR(200) |  |  | One of the person aliases entered to identify the patient. If known based on the barcode format, this will be the patients identifier on the collection label. |
| 4 | `BARCODE_ALIAS1` | VARCHAR(200) |  |  | One of the bar-coded values entered to identify the patient. If known based on the barcode format, this will be the patients identifier on the patient wristband. |
| 5 | `BARCODE_ALIAS2` | VARCHAR(200) |  |  | One of the bar-coded values entered to identify the patient. If known based on the barcode format, this will be the patients identifier on the collection label. |
| 6 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | If a collection is cancelled, this is the reason for the cancel. |
| 7 | `COLLECTION_COMMENT` | VARCHAR(200) |  |  | A comment entered that will be tied to the container. |
| 8 | `COLLECTION_DT_TM` | DATETIME |  |  | The collection date and time gathered by the device. |
| 9 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | The method used to collect the specimen. Only populated if changed on the device. |
| 10 | `COLLECTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user who performed the collection specified. |
| 11 | `COLLECTION_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the collection. |
| 12 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the CONTAINER table. Only populated if the container ID was specified on the device. |
| 13 | `CONTAINER_NBR` | DOUBLE |  |  | The container suffix used to uniquely identify each container for an accession number. Only populated when it was specified on the device. |
| 14 | `ENCNTR1_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID related to the first patient alias given. |
| 15 | `ENCNTR2_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID related to the second patient alias given. |
| 16 | `ERROR_CD` | DOUBLE | NOT NULL |  | Indicates if an error occurred for this collection. |
| 17 | `HANDHELD_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique identifier for each occurrence of detail for a handheld session. |
| 18 | `HANDHELD_UPLOAD_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the HANDHELD_UPLOAD table which stores information about each upload event. |
| 19 | `MISSED_REASON_CD` | DOUBLE | NOT NULL |  | If a collection is missed, this is the reason entered. |
| 20 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the ORDERS table. Only populated if the collection status was different for orders in the same container. |
| 21 | `OVERRIDE_IND` | DOUBLE |  |  | Indicates if Positive Patient Identification was overridden. |
| 22 | `PERSON1_ID` | DOUBLE | NOT NULL | FK→ | The person ID related to the first patient alias given. |
| 23 | `PERSON2_ID` | DOUBLE | NOT NULL | FK→ | The person ID related to the second patient alias given. |
| 24 | `RECEIVED_DT_TM` | DATETIME |  |  | The date/time the specimen was marked as received. |
| 25 | `RECEIVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user who received the specimen specified. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `ENCNTR1_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR2_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HANDHELD_UPLOAD_ID` | [HANDHELD_UPLOAD](HANDHELD_UPLOAD.md) | `HANDHELD_UPLOAD_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON1_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON2_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RECEIVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

