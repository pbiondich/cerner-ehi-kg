# MM_XFI_LOCATOR

> Interface Item Locator table. Data is moved from this table to the LOCATOR_ROLLUP table.

**Description:** Interface Item Locator  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 37  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Action flag for the action |
| 2 | `BATCH_GROUP_ID` | DOUBLE |  | FK→ | Grouper TRANSACTION_ID for a set of MM_XFI_LOCATOR rows in order to perform batch processing on a subset of rows. |
| 3 | `BATCH_REF` | VARCHAR(100) |  |  | Batch Reference |
| 4 | `CONTRIBUTOR` | VARCHAR(40) |  |  | Contributor value |
| 5 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor CD |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was last inserted |
| 8 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert of the row in the table. |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row |
| 10 | `EXTERNAL_REF_IDENT` | VARCHAR(15) |  |  | Stores the external ERP's batch identification; |
| 11 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID value of the Item |
| 12 | `ITEM_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | Item Identifier |
| 13 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | Item Identifier Type |
| 14 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Item Identifier Type CD |
| 15 | `LOCATION` | VARCHAR(100) | NOT NULL |  | Location where the item exists. |
| 16 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location CD |
| 17 | `LOCATOR` | VARCHAR(60) | NOT NULL |  | Locator |
| 18 | `LOCATOR_CD` | DOUBLE | NOT NULL |  | Locator CD |
| 19 | `LOC_VIEW` | VARCHAR(100) |  |  | Location View |
| 20 | `LOC_VIEW_CD` | DOUBLE | NOT NULL |  | Location View CD |
| 21 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 22 | `ORGANIZATION` | VARCHAR(100) |  |  | Organization |
| 23 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 24 | `PKG_TYPE_CONV` | DOUBLE |  |  | Package type Conversion |
| 25 | `PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Package Type ID |
| 26 | `PKG_TYPE_UOM` | VARCHAR(40) |  |  | Package type Unit of Measure |
| 27 | `PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | Package type Unit of Measure CD |
| 28 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Process Flag |
| 29 | `SEGMENT_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | Segment Identifier |
| 30 | `SEGMENT_VERSION` | VARCHAR(10) | NOT NULL |  | Segment Version |
| 31 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 32 | `UPDATE_RULE_FLAG` | DOUBLE |  |  | Update Rule Flag |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_GROUP_ID` | [MM_XFI_LOCATOR](MM_XFI_LOCATOR.md) | `TRANSACTION_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_XFI_LOCATOR](MM_XFI_LOCATOR.md) | `BATCH_GROUP_ID` |
| [MM_XFI_LOCATOR_BATCH](MM_XFI_LOCATOR_BATCH.md) | `BATCH_GROUP_ID` |

