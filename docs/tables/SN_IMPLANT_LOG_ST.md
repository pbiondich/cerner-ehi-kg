# SN_IMPLANT_LOG_ST

> Table used to store implant log data to be used in Surgery Management Reporting's Implant Log Analysis view.

**Description:** SurgiNet Implant Log Summary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_NUMBER` | VARCHAR(50) |  |  | Indicates the implants Batch Number, as entered on the Prosthetic Devices form in PDM |
| 2 | `CATALOG_NUMBER` | VARCHAR(50) |  |  | Indicates the implant's Catalog Number, as entered on the Prosthetic Devices form in PDM |
| 3 | `CULTURED_IND` | DOUBLE |  |  | Indicates whether this impalnt has been cultured, as entered in the Prosthetic Devices form in PDM |
| 4 | `DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Indicates the sequence in which this implant entry was made in the Prosthetic Devices form in PDM |
| 5 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the document type associated with this PDM entry |
| 6 | `ECRI_DEVICE_CODE` | VARCHAR(50) |  |  | Indicates the implant's ECRI Device Code, as entered in the Prosthetic Devices form in PDM |
| 7 | `EXP_DATE` | DATETIME |  |  | Indicates the implant's expiration date, as entered in the Prosthetic Devices form in PDM |
| 8 | `FREE_TEXT_ITEM_DESC` | VARCHAR(200) |  |  | The free-text description associated with this implant item. This column is only populated if a free-text inventory item was entered in the inventory control in the Prosthetic Devices form in Perioperative Document Manager. |
| 9 | `IMPLANTED_BY_ID` | DOUBLE | NOT NULL |  | The person responsible for implanting this device |
| 10 | `IMPLANT_ACTION_CD` | DOUBLE | NOT NULL |  | Indicates whether the implant action value is "Implant", "Explant" or "Not-Implanted". |
| 11 | `IMPLANT_LOG_ST_ID` | DOUBLE | NOT NULL |  | A unique sequence number used as the primary key to the table |
| 12 | `IMPLANT_PROCESSED_FLAG` | DOUBLE | NOT NULL |  | Indicates whether data has been copied from this table to the IMPLANT_HISTORY table (1) or whether data has not yet been copied (0) |
| 13 | `IMPLANT_SITE` | VARCHAR(100) |  |  | The site where this device was implanted |
| 14 | `IMPLANT_SIZE` | VARCHAR(50) |  |  | The size of this prosthetic device |
| 15 | `ITEM_ID` | DOUBLE | NOT NULL |  | The item associated with this prosthetic device |
| 16 | `LOT_NUMBER` | VARCHAR(50) |  |  | The lot number associated with this prosthetic device |
| 17 | `MANUFACTURER` | VARCHAR(100) |  |  | The manufacturer associated with this prosthetic device |
| 18 | `MANUF_ECRI_CODE` | VARCHAR(50) |  |  | The manufacturer's ECRI Code for this prosthetic device |
| 19 | `MODEL_NUMBER` | VARCHAR(50) |  |  | The model number associated with this prosthetic device |
| 20 | `OTHER_IDENTIFIER` | VARCHAR(50) |  |  | A miscellaneous identifier associated with this prosthetic device |
| 21 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | FK→ | A reference to the perioperative document associated with this prosthetic device entry in PDM |
| 22 | `QUANTITY` | VARCHAR(50) |  |  | The quantity associated with this prosthetic device |
| 23 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | A reference to the segment header associated with this Prosthetic Device entry in PDM |
| 24 | `SERIAL_NUMBER` | VARCHAR(50) |  |  | The serial number associated with this prosthetic device |
| 25 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | A reference to the surgical_case table, identifying the surgical case associated with this prosthetic device entry in PDM |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERIOP_DOC_ID` | [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `PERIOP_DOC_ID` |
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

