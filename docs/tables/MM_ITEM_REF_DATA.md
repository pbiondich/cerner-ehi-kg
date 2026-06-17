# MM_ITEM_REF_DATA

> Contains the reference database information of item

**Description:** Item Reference Data  
**Table type:** REFERENCE  
**Primary key:** `MM_ITEM_REF_DATA_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_NAME` | VARCHAR(255) |  |  | Proprietary/trade name of the medical device as used inthe labeing or catalog. Received from Reference Database |
| 2 | `COMPANY_NAME_TXT` | VARCHAR(255) |  |  | Manufacturer Company Name from Reference Database |
| 3 | `DEVICE_DESCRIPTION_TXT` | VARCHAR(4000) |  |  | Device Description of Item from Reference Database |
| 4 | `DEVICE_ID_TXT` | VARCHAR(255) |  |  | Primary device identifier number from Reference Database. An identifier that is the primary lookup for a medical device. The primary DI will be located on label of the base package (the lowest package level of a medical device containing a full UDI). For medical devices without packaging, the primary DI number and full UDI may be on the device itself. |
| 5 | `LATEX_TXT` | VARCHAR(255) |  |  | Whether the device or packaging contains natural rubber that contacts humans. "Natural rubber" includes natural rubber latex, dry natural rubber, and synthetic latex or rubber that contains natural rubber. Information from Reference Database |
| 6 | `MFR_CATALOG_NBR_TXT` | VARCHAR(255) |  |  | Manufacturer Catalog number of Item from Reference Database |
| 7 | `MM_ITEM_REF_DATA_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_ITEM_REF_DATA table. |
| 8 | `MODEL_NUMBER_TXT` | VARCHAR(255) |  |  | Identifies a category or design of devices that have specifications, performance, size, and composition within limits set by the company. Provided from Reference Database. |
| 9 | `MRI_SAFETY_INFO_TXT` | VARCHAR(255) |  |  | The information the labeling contains about whether a device is compatible with magnetic resonance imaging (MRI) procedures. |
| 10 | `REFERENCE_DATABASE_NAME_TXT` | VARCHAR(255) | NOT NULL |  | Name of the reference database |
| 11 | `REFERENCE_DATA_TXT` | LONGTEXT |  |  | Complete Reference Data information of the item from Reference Database in JSON format |
| 12 | `SNOMED_CT_DESC_TXT` | VARCHAR(255) |  |  | SNOMED CT Description from Reference Database |
| 13 | `SNOMED_CT_IDENTIFIER_TXT` | VARCHAR(255) |  |  | SNOMED CT Identifier from Reference Database |
| 14 | `SOURCE_UPDT_DT_TM` | DATETIME |  |  | Update date time by the backend process |
| 15 | `UNIQUE_PRODUCT_KEY_TXT` | VARCHAR(255) | NOT NULL |  | Column to store the Unique Product Identifier to resolve the item. This column should be populated irrespective of different reference database. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_ITEM_REF_ADDL_ATTR](MM_ITEM_REF_ADDL_ATTR.md) | `MM_ITEM_REF_DATA_ID` |

