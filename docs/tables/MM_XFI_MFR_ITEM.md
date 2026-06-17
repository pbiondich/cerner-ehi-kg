# MM_XFI_MFR_ITEM

> This table contains manufacturer items and their identifying information, including UPNs data which is imported from the external ERP system.

**Description:** Materials Management Foreign Integration Manufacturer Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_CD` | DOUBLE |  |  | The code value for the contributor that was passed in. |
| 2 | `CONTRIBUTOR_TXT` | VARCHAR(40) |  |  | This indicates the Contributor Source to be used for code value aliasing. |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block responsible for creation. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time the row was created. |
| 5 | `CREATE_ID` | DOUBLE |  | FK→ | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 7 | `EXTERNAL_REF_IDENT` | VARCHAR(15) |  |  | The external reference identifier of the event triggering the process. |
| 8 | `ITEM_ID` | DOUBLE |  | FK→ | Item Master ID. |
| 9 | `ITEM_IDENTIFIER_TXT` | VARCHAR(255) |  |  | A string value that will be resolved to an Item in Millennium. |
| 10 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE |  |  | Item Identifier Type Code Value. |
| 11 | `ITEM_IDENTIFIER_TYPE_TXT` | VARCHAR(40) |  |  | This is a string that will be converted to a corresponding code value. For example, if "Item Number" is entered, then item_identifier_type_cd will be resolved to a code value with CDF meaning = "Item Number". |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `MFR_CD` | DOUBLE |  |  | The manufacturer of the item. From the MANUFACTURER_ITEM table. |
| 14 | `MFR_ITEM_ACTION_TFLG` | VARCHAR(20) |  |  | MFR_ITEM_ACTION_FLAG defines what action to take with the incoming manufacturing item data |
| 15 | `MFR_ITEM_BRAND_NAME` | VARCHAR(255) |  |  | Value provided to lookup/create Manufacturer Item Brand Name Identifier. |
| 16 | `MFR_ITEM_BRAND_NAME_ID` | DOUBLE |  | FK→ | Identifier ID for the Manufacturer Item Brand Name. |
| 17 | `MFR_ITEM_DESC` | VARCHAR(255) |  |  | Value provided to lookup/create Manufacturer Item Description Identifier. |
| 18 | `MFR_ITEM_DESC_ID` | DOUBLE |  | FK→ | Identifier ID for the Manufacturer Item Description Identifier. |
| 19 | `MFR_ITEM_ID` | DOUBLE |  | FK→ | The manufacturer item ID from the Identifier table |
| 20 | `MFR_ITEM_NBR_ID` | DOUBLE |  | FK→ | Identifier ID for the Manufacturer Item Number Identifier. |
| 21 | `MFR_ITEM_NBR_TXT` | VARCHAR(40) |  |  | Value provided to lookup/create Manufacturer Item Number Identifier. |
| 22 | `MFR_ITEM_TRADE_NAME` | VARCHAR(255) |  |  | Value provided to lookup/create Manufacturer Item Trade Name Identifier. |
| 23 | `MFR_ITEM_TRADE_NAME_ID` | DOUBLE |  | FK→ | Identifier ID for the Manufacturer Item Trade Name Identifier. |
| 24 | `MFR_NAME` | VARCHAR(60) |  |  | Name of the Manufacturer |
| 25 | `MM_XFI_MFR_ITEM_ID` | DOUBLE | NOT NULL |  | A system generated number used to uniquely identify a row on the MM_XFI_MFR_ITEM table |
| 26 | `PROCESS_FLAG` | DOUBLE |  |  | Defines the state of the row in the upload process. |
| 27 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPN_ACTION_TFLG` | VARCHAR(20) |  |  | Flag that defines the type of action to take for the UPN. |
| 33 | `UPN_ID` | DOUBLE |  | FK→ | Identifier ID for the UPN. |
| 34 | `UPN_TXT` | VARCHAR(40) |  |  | Value provided to lookup/create UPN Identifier. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MFR_ITEM_BRAND_NAME_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_DESC_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `MFR_ITEM_NBR_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `MFR_ITEM_TRADE_NAME_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `UPN_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |

