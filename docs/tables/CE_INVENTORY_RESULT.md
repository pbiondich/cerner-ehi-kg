# CE_INVENTORY_RESULT

> Track information about any device or machine that was hooked up to a patient.

**Description:** CE INVENTORY RESULT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE` | VARCHAR(50) |  |  | Site of the that the item was used on. |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the item. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical_event table. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the item_definition table. This is the item's key back to the item_definition table in the materials management data model. If an item is free text then this will NOT be filled out. |
| 5 | `ITEM_NBR` | VARCHAR(255) |  |  | Item number for the item. It is user defined. |
| 6 | `QUANTITY` | DOUBLE |  |  | Quantity of the item. |
| 7 | `REFERENCE_ENTITY_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** Id into a table defined by the user. |
| 8 | `REFERENCE_ENTITY_NAME` | VARCHAR(32) |  |  | *** OBSOLETE *** Name of the table for which the reference_entity_id references. |
| 9 | `SERIAL_MNEMONIC` | VARCHAR(30) |  |  | The serial mnemonic of the item. |
| 10 | `SERIAL_NBR` | VARCHAR(30) |  |  | The serial number of the item. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the "Beginning Point" of when a row in the table is valid. |
| 17 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

