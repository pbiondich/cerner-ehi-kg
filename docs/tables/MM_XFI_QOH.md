# MM_XFI_QOH

> Inbound interface table for Quantity On Hand. Data is moved from this table to QUANTITY_ON_HAND.

**Description:** MM XFI QOH  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 46

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_LOT_EXP_DT_TM` | DATETIME |  |  | Expiration Date as determined at place of origin. |
| 2 | `ABS_LOT_EXP_TZ` | DOUBLE |  |  | Time zone associated with the ABS_LOT_EXP_DT_TM column. |
| 3 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Determines what action to take -- Add / Change / Delete. |
| 4 | `BATCH_REF` | VARCHAR(100) |  |  | This is a user defined field; allows a reference number/string to be passed in as part of an interface/upload. |
| 5 | `CONTRIBUTOR` | VARCHAR(40) |  |  | This indicates the Contributor Source to be used for code value aliasing. |
| 6 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | The code value for the contributor that was passed in. |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting the row. |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date/time the row was created. |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | Person responsible for inserting the row |
| 10 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for creating the row. |
| 11 | `ITEM_ID` | DOUBLE | NOT NULL |  | The internal item key for the item to be uploaded. |
| 12 | `ITEM_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | The value passed through the interface to identify an item. |
| 13 | `ITEM_IDENTIFIER_TYPE` | VARCHAR(40) |  |  | The type of identifier that was passed in through the ITEM_IDENTIFIER field. Should be a valid display value from codeset 11000. |
| 14 | `ITEM_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the identifier type. |
| 15 | `LOCATION` | VARCHAR(100) | NOT NULL |  | The display/alias value for the location. |
| 16 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The code value for the location. |
| 17 | `LOCATOR` | VARCHAR(60) |  |  | The display/alias for the locator. |
| 18 | `LOCATOR_CD` | DOUBLE | NOT NULL |  | The code value for the locator. |
| 19 | `LOC_VIEW` | VARCHAR(100) |  |  | Refers to the HNAM Materials Mgmt location view to be used when validating locator names. |
| 20 | `LOC_VIEW_CD` | DOUBLE | NOT NULL |  | Location View CD |
| 21 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 22 | `LOT_EXP_DT_TM` | DATETIME |  |  | The date/time a lot will expire. |
| 23 | `LOT_MANUF_DT_TM` | DATETIME |  |  | The date/time an item in the lot was manufactured. |
| 24 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | The lot this row relates to. |
| 25 | `LOT_NUMBER_TXT` | VARCHAR(40) |  |  | Character description of the lot number as defined by the manufacturer of the lot. |
| 26 | `MANUF_CD` | DOUBLE | NOT NULL | FK→ | The manufacturer of the item. |
| 27 | `MANUF_NAME` | VARCHAR(255) |  |  | The manufacturer Name. |
| 28 | `ORGANIZATION` | VARCHAR(100) |  |  | The name of the organization. |
| 29 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The primary key for the organization. |
| 30 | `PKG_TYPE_CONV` | DOUBLE |  |  | The conversion factor for the package type. |
| 31 | `PKG_TYPE_ID` | DOUBLE | NOT NULL |  | The primary key for the package type. |
| 32 | `PKG_TYPE_UOM` | VARCHAR(40) |  |  | The unit-of-measure for the package type. |
| 33 | `PKG_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The code value for the unit-of-measure. |
| 34 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the status of the current row. |
| 35 | `QOH_QTY` | DOUBLE |  |  | The amount of quantity on-hand to upload. |
| 36 | `QOH_TYPE` | VARCHAR(40) |  |  | Defaults to UNRESTRICTED |
| 37 | `QOH_TYPE_CD` | DOUBLE | NOT NULL |  | Defaults to UNRESTRICTED |
| 38 | `SEGMENT_IDENTIFIER` | VARCHAR(10) | NOT NULL |  | Identifies the type of upload. For QOH, it is ILQ. |
| 39 | `SEGMENT_VERSION` | VARCHAR(10) | NOT NULL |  | Identifies the version of the upload interface |
| 40 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 41 | `UPDATE_RULE_FLAG` | DOUBLE |  |  | Future Functionality |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MANUF_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

