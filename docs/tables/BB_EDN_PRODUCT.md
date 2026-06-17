# BB_EDN_PRODUCT

> This table contains the product information from an Electronic Delivery Note message structure.

**Description:** Blood Bank Electronic Delivery Note Product  
**Table type:** ACTIVITY  
**Primary key:** `BB_EDN_PRODUCT_ID`  
**Columns:** 42  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | Contains the product's ABO value from the electronic delivery note file. |
| 2 | `ALIAS` | VARCHAR(100) |  |  | Alias used by FSI for person matching. Could be encounter or person alias. |
| 3 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool used by FSI for person matching. Can be person or encounter. |
| 4 | `BB_EDN_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the row on the Electronic Delivery Note related to this product. |
| 5 | `BB_EDN_PRODUCT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies product information from an Electronic Delivery Note message structure. |
| 6 | `CLINICAL_USE_IND` | DOUBLE | NOT NULL |  | Indicates if a product is suitable for clinical use. |
| 7 | `DATA_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Contains Source of Product Information. 0 - Unidentified Source; 1 - BloodNet GS1; 2 - BloodNet ISBT |
| 8 | `DELIVERY_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the product's type of delivery from the Electronic Delivery Note file. |
| 9 | `DEVICE_TXT` | VARCHAR(40) |  |  | This is the value passed in an interface storage location field. It should match to a description on the BB_INV_DEVICE table. |
| 10 | `DONATION_DT_TM` | DATETIME |  |  | Contains the date and time the product was donated from the Electronic Delivery Note file. |
| 11 | `EDN_PRODUCT_NBR_IDENT` | VARCHAR(20) | NOT NULL |  | Contains the product number from the Electronic Delivery Note file. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The encntr of the person to be associated to the product |
| 13 | `EVENT_DT_TM` | DATETIME |  |  | If the time the action was taken is significant (i.e. transfusion), this is the date and time. If it is not significant, the EDN_Admin/ Admin date and Time will be used. |
| 14 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the user that performed the action, or zero if not available. |
| 15 | `EXPIRATION_DT_TM` | DATETIME |  |  | Contains the product's expiration date and time from the Electronic Delivery Note file. |
| 16 | `FLAG_CHAR_TXT` | VARCHAR(2) |  |  | ISBT flag characters. Default to 00 for ISBT product numbers, no value for other formats. |
| 17 | `ISBT_BLOOD_TYPE_BARCODE` | VARCHAR(200) |  |  | contains abo/rh barcode. The format could be isbt or a format that matches the abo/rh tool. |
| 18 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Contains the ID of the product comment stored on the long text reference table. |
| 19 | `MANUFACTURER_ID` | DOUBLE | NOT NULL |  | the id of the organization which manufactured this derivative batch. |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person the product is associated to. For Transfused, this is the transfusion recipient. |
| 21 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Millennium product type, if the product_type_text for the bb_edn_product table was resolved to a Millennium product type. This is displayed on the problem exception report. |
| 22 | `PRODUCT_COMMENT_TXT` | VARCHAR(30) | NOT NULL |  | Contains the product comment from the Electronic Delivery Note file. |
| 23 | `PRODUCT_COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates that the product has been reconciled. |
| 24 | `PRODUCT_ID` | DOUBLE | NOT NULL |  | Contains the associated product identifier from the product table. |
| 25 | `PRODUCT_IDENT` | VARCHAR(40) |  |  | Identifies the product received from external service |
| 26 | `PRODUCT_SUB_NBR_TXT` | VARCHAR(5) |  |  | Indicates the division characters if the product is divided. will correspond to the product_sub_nbr on the product table if the transaction is successful. |
| 27 | `PRODUCT_TYPE_IDENT` | VARCHAR(40) |  |  | Identifies the product type identifier from an external service. |
| 28 | `PRODUCT_TYPE_TXT` | VARCHAR(50) | NOT NULL |  | Contains the product type from the Electronic Delivery Note file. |
| 29 | `RECEIVED_QTY` | DOUBLE |  |  | available quantity received through the interface |
| 30 | `RH_CD` | DOUBLE | NOT NULL |  | Contains the product's RH value from the Electronic Delivery Note file. |
| 31 | `SERIAL_NUMBER_TXT` | VARCHAR(22) |  |  | Contains GS1 serial number for derivative products when applicable. |
| 32 | `STATUS_CD` | DOUBLE | NOT NULL |  | Describes the status change occurring to the product. Note that this is from the process codeset, not the event_type code set. |
| 33 | `SUB_STATUS_CD` | DOUBLE | NOT NULL |  | If the status is transferred, this is the transfer reason. |
| 34 | `SUPPLIER_PRODUCT_ALIAS_NAME` | VARCHAR(40) |  |  | Product identifier unique to sending system. |
| 35 | `UNITS_PER_VIAL` | DOUBLE |  |  | number of international units per vial |
| 36 | `UNIT_CONDITION_CD` | DOUBLE | NOT NULL |  | This is the unit condition mapped to a quarantine reason on code set 1630. If there is not a value, either the condition was ok, or the condition is not aliased for inbound transaction. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `VOLUME_CNT` | DOUBLE | NOT NULL |  | Contains the product volume from the Electronic Delivery Note file. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_EDN_ADMIN_ID` | [BB_EDN_ADMIN](BB_EDN_ADMIN.md) | `BB_EDN_ADMIN_ID` |
| `EVENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BB_EDN_DSCRPNCY_OVRD](BB_EDN_DSCRPNCY_OVRD.md) | `BB_EDN_PRODUCT_ID` |
| [BB_EDN_PROBLEM](BB_EDN_PROBLEM.md) | `BB_EDN_PRODUCT_ID` |
| [BB_EDN_SPCL_TESTING](BB_EDN_SPCL_TESTING.md) | `BB_EDN_PRODUCT_ID` |

