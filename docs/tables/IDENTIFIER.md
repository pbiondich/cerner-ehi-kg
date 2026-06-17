# IDENTIFIER

> This table contains identifiers (Item Number, Description,...).

**Description:** Identifier  
**Table type:** REFERENCE  
**Primary key:** `IDENTIFIER_ID`  
**Columns:** 31  
**Referenced by:** 26 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 10 | `IDENTIFIER_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 11 | `IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Code value for the type of identifier. |
| 12 | `IDENTIFIER_UPDT_CNT` | DOUBLE | NOT NULL |  | Indicates the number of changes that have been made to Identifier that have not been updated in bill_item_modifier. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the package type table. Indicates the unit-of-measure for a specific UPN or NDC. |
| 15 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 16 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the parent entity table |
| 17 | `REPLACED_UPN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the identifier table. Indicates the UPN identifier that was replaced by the current UPN. |
| 18 | `REPLACEMENT_UPN_ID` | DOUBLE | NOT NULL |  | Foreign key to the identifier table. Indicates the UPN identifier that was replaces the current UPN. |
| 19 | `SALABLE_BY_MFR_IND` | DOUBLE |  |  | Indicates whether or not this UPN specific item & package is salable by the manufacturer. |
| 20 | `SALABLE_BY_VENDOR_IND` | DOUBLE |  |  | Indicates whether or not this UPN specific item & package is salable by the vendor. |
| 21 | `SPCL_CHAR_VALUE` | VARCHAR(255) | NOT NULL |  | Stores the data except * + / and space characters in uppercase mode. |
| 22 | `SPCL_CHAR_VALUE_A_NLS` | VARCHAR(1020) | NOT NULL |  | Stores the corresponding non-English character set values for the SPCL_CHAR_VALUE column. Used to sort correctly internationally. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VALUE` | VARCHAR(255) | NOT NULL |  | The string displayed to the user. |
| 29 | `VALUE_KEY` | VARCHAR(255) | NOT NULL |  | Same as Value except in all uppercase. |
| 30 | `VALUE_KEY_A_NLS` | VARCHAR(1020) |  |  | VALUE_KEY_A_NLS column |
| 31 | `VALUE_KEY_NLS` | VARCHAR(512) |  |  | Used in queries for locales other than English. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `REPLACED_UPN_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |

## Referenced by (26)

| From table | Column |
|------------|--------|
| [IDENTIFIER](IDENTIFIER.md) | `REPLACED_UPN_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `ITEM_DESC_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `ITEM_NBR_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MFR_CATALOG_NBR_ID` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `INSTANCE_IDENT_ID` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `SERIAL_NBR_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `CHARGE_NUMBER_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_ALIAS_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_CLINICAL_DESC_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_DESC_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_NBR_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `ITEM_SHORT_DESC_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `MFR_ITEM_BRAND_NAME_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `MFR_ITEM_DESC_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `MFR_ITEM_NBR_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `MFR_ITEM_TRADE_NAME_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `REPLACEMENT_UPN_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `UPN_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `VENDOR_ITEM_DESC_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `VENDOR_ITEM_NBR_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `MFR_ITEM_BRAND_NAME_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `MFR_ITEM_DESC_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `MFR_ITEM_NBR_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `MFR_ITEM_TRADE_NAME_ID` |
| [MM_XFI_MFR_ITEM](MM_XFI_MFR_ITEM.md) | `UPN_ID` |
| [OBJECT_IDENTIFIER_INDEX](OBJECT_IDENTIFIER_INDEX.md) | `IDENTIFIER_ID` |

