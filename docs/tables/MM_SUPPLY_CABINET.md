# MM_SUPPLY_CABINET

> Stores data received from an external supply cabinet

**Description:** MM SUPPLY CABINET  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUS_DOMAIN_NAME` | VARCHAR(30) |  |  | The bus domain that is the source of this information. |
| 2 | `DEVICE_IDENT` | VARCHAR(150) |  |  | The identifier of the device as supplied by the Bus. |
| 3 | `ITEM_CLASS_ID` | DOUBLE | NOT NULL | FK→ | The supply cabinet inventory item's class. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The resolved Millennium item in ITEM_DEFINITION. |
| 5 | `LATEX_CD` | DOUBLE | NOT NULL |  | The resolved Millennium latex indicator. |
| 6 | `LOC_CD` | DOUBLE | NOT NULL | FK→ | The location of the supply cabinet. |
| 7 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Resolved Millennium lot number. |
| 8 | `MFR_CD` | DOUBLE | NOT NULL |  | Resolved Millennium manufacturer code |
| 9 | `MFR_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Resolved Millennium manufacturer item id |
| 10 | `MM_SUPPLY_CABINET_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_SUPPLY_CABINET table. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Resolved Millennium patient that this supply is for. |
| 12 | `PROCESSED_BY_APP_ID` | DOUBLE | NOT NULL |  | Indicates the primary key from the application/table that consumed this data. |
| 13 | `PROCESSED_BY_APP_NAME` | VARCHAR(30) |  |  | Indicates the table that consumed this dataInitially this will be "PERIOPERATIVE_DOCUMENT" |
| 14 | `PROCESSED_BY_DOC_IND` | DOUBLE | NOT NULL |  | Indicates whether this row has been defaulted into Surgical documentation yet. |
| 15 | `PROCESSED_BY_PL_IND` | DOUBLE | NOT NULL |  | Indicates whether this row has been defaulted onto the Surgical pick list yet. |
| 16 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of reconciling item received to Millennium item. |
| 17 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that performed the action (remove, return, waste) that triggered this transaction |
| 18 | `SC_EXP_DT_TM` | DATETIME |  |  | Expiration date and time for lot received from supply cabinet |
| 19 | `SC_ITEM_QTY` | DOUBLE |  |  | Quantity of item(s) removed/returned/wasted from supply cabinet |
| 20 | `SC_ITEM_TXT` | VARCHAR(255) | NOT NULL |  | Description of item received from supply cabinet |
| 21 | `SC_LATEX_CD` | DOUBLE | NOT NULL |  | Indication from supply cabinet whether the item contains latex. |
| 22 | `SC_LOT_NBR_TXT` | VARCHAR(40) |  |  | Lot number received from supply cabinet |
| 23 | `SC_MFR_CAT_NBR_TXT` | VARCHAR(255) |  |  | Catalog number received from supply cabinet |
| 24 | `SC_MFR_NAME` | VARCHAR(60) |  |  | Item manufacturer received from supply cabinet |
| 25 | `SC_REASON_TXT` | VARCHAR(255) |  |  | Reason for the transaction. (Ex: Item was wasted, returned.) |
| 26 | `SC_SERIAL_NBR_TXT` | VARCHAR(255) |  |  | Item serial number received from supply cabinet |
| 27 | `SC_SIZE_TXT` | VARCHAR(50) |  |  | Item size and units (alphanumeric) received from supply cabinet |
| 28 | `SC_SURG_CASE_NBR_TXT` | VARCHAR(25) |  |  | The surgical case number received from a supply cabinet. |
| 29 | `SC_TRANS_DT_TM` | DATETIME |  |  | Date/time the transaction occurred on the supply cabinet. |
| 30 | `SC_TRANS_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of transaction.1 |
| 31 | `SC_TRANS_IDENT` | VARCHAR(150) | NOT NULL |  | The foreign system's internal identifier for the transaction. |
| 32 | `SEG_CD` | DOUBLE | NOT NULL |  | The surgical segment a supply cabinet inventory item defaulted on. |
| 33 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The resolved surgical case resulting from the sc_surg_case_nbr_txt received from the supply cabinet. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_CLASS_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MFR_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

