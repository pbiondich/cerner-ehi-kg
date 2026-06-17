# MM_INSTANCE

> Stores item and equipment instance information for Supply Chain.

**Description:** Item Instance  
**Table type:** REFERENCE  
**Primary key:** `MM_INSTANCE_ID`  
**Columns:** 21  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_EXP_DT_TM` | DATETIME |  |  | Expiration Date as determined at place of origin. |
| 2 | `ABS_EXP_TZ` | DOUBLE |  |  | Time zone associated with the ABS_EXP_DT_TM column. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `CONTROL_IDENT` | VARCHAR(400) | NOT NULL |  | Identifier assigned to an individual occurrence of an Item. |
| 5 | `EXP_DT_TM` | DATETIME |  |  | Stores the expiration date for the serial number |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | This column represents the item that this occurrence is a part of. |
| 7 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relevant lot number for a serial number. |
| 8 | `MFR_CD` | DOUBLE | NOT NULL | FK→ | The manufacturer of the item. From the MANUFACTURER_ITEM table. |
| 9 | `MFR_DT_TM` | DATETIME |  |  | Stores the manufacturer date for the serial number |
| 10 | `MM_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MM_INSTANCE table. |
| 11 | `MODEL_NBR_TXT` | VARCHAR(60) | NOT NULL |  | %occurrent |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization that owns this item instance. |
| 13 | `PART_NBR_TXT` | VARCHAR(60) | NOT NULL |  | The part number for this instance of an item. |
| 14 | `STATUS_CD` | DOUBLE | NOT NULL |  | The codified value that indicates the current status of the instance. Examples would be: Available, In Use, Out of Service. |
| 15 | `STORAGE_LOCATION_CD` | DOUBLE | NOT NULL |  | An instance has a location where it is kept when not in use. This location represents that storage location. |
| 16 | `TRANS_INSTANCE_IND` | DOUBLE | NOT NULL |  | Indicates whether the instance was created manually or was created by a transaction. If an instance was created manually the indicator will be set to "0". If an instance was created by a transaction then the indicator will be set to "1". |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `MFR_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MM_INSTANCE_TRANS_LINE_R](MM_INSTANCE_TRANS_LINE_R.md) | `MM_INSTANCE_ID` |
| [MM_XFI_INSTANCE](MM_XFI_INSTANCE.md) | `MM_INSTANCE_ID` |
| [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `MM_INSTANCE_ID` |

