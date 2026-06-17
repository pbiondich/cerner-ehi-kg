# MM_XFI_COST

> Intermediate inbound interface table for importing item cost. Data is moved from this table to ITEM_LOCATION_COST.

**Description:** MM XFI COST  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 38  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Determines the action to be taken for this row. (1-Update/Insert,...) |
| 2 | `BATCH_GROUP_ID` | DOUBLE |  | FK→ | Grouper TRANSACTION_ID for a set of MM_XFI_COST rows in order to perform batch processing on a subset of rows. |
| 3 | `BATCH_REF` | VARCHAR(100) |  |  | User defined field to identify this particular upload batch. |
| 4 | `CONTRIBUTOR` | VARCHAR(40) |  |  | The contributor |
| 5 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | The contributor |
| 6 | `COST` | DOUBLE |  |  | The cost of the item. |
| 7 | `COST_TYPE` | VARCHAR(40) |  |  | The cost type (Average,Last,...) |
| 8 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The cost type. |
| 9 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting the row. |
| 10 | `CREATE_DT_TM` | DATETIME |  |  | The Date/Time this row was inserted. |
| 11 | `CREATE_ID` | DOUBLE | NOT NULL |  | The ID of the person responsible for inserting this row. |
| 12 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row. |
| 13 | `EXTERNAL_REF_IDENT` | VARCHAR(15) |  |  | Stores the external ERP's batch identifiecation; |
| 14 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The internal item identifier. Primary Key |
| 15 | `ITEM_IDENTIFIER` | VARCHAR(255) |  |  | The identifier that will be used to validate against (item number, upn, ndc,...) |
| 16 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | Identifies the type of identifier passed in. |
| 17 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of identifier passed in. |
| 18 | `LOCATION` | VARCHAR(100) |  |  | The location name to build the record for. |
| 19 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The codevalue for the location |
| 20 | `LOC_VIEW` | VARCHAR(100) |  |  | Currently not used. |
| 21 | `LOC_VIEW_CD` | DOUBLE | NOT NULL |  | Currently not used. |
| 22 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 23 | `ORGANIZATION` | VARCHAR(100) |  |  | The name of the organization in which the location resides. |
| 24 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Primary key for organization |
| 25 | `PKG_TYPE_CONV` | DOUBLE |  |  | The pack factor for the package type. |
| 26 | `PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Primary key for package type |
| 27 | `PKG_TYPE_UOM` | VARCHAR(40) |  |  | The package type unit-of-measure. |
| 28 | `PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the unit-of-measure. |
| 29 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates the import status of the row. |
| 30 | `SEGMENT_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | Identifies the type of interface -- ILC |
| 31 | `SEGMENT_VERSION` | VARCHAR(10) | NOT NULL |  | The interface version |
| 32 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 33 | `UPDATE_RULE_FLAG` | DOUBLE |  |  | Future use. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_GROUP_ID` | [MM_XFI_COST](MM_XFI_COST.md) | `TRANSACTION_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MM_XFI_COST](MM_XFI_COST.md) | `BATCH_GROUP_ID` |
| [MM_XFI_COST_BATCH](MM_XFI_COST_BATCH.md) | `BATCH_GROUP_ID` |

