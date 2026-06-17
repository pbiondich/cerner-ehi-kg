# PCS_KIT_INFORMATION

> This table stores the individual kit information for all kits received into inventory.

**Description:** PathNet Common Services Kit Information  
**Table type:** ACTIVITY  
**Primary key:** `KIT_INFORMATION_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the LONG_TEXT row that contains the kit comment text. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | This field contains the date/time that a kit is scheduled to expire. |
| 5 | `KIT_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the associated PCS_KIT_DEFINITION row. |
| 6 | `KIT_IDENT` | VARCHAR(40) | NOT NULL |  | This field contains the user-defined kit "number" as defined by the supplier. |
| 7 | `KIT_INFORMATION_ID` | DOUBLE | NOT NULL | PK | This field contains the unique identifier of the specific kit information. |
| 8 | `KIT_SOURCE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the original PCS_KIT_INFORMATION row associated with the kit. This allows history to be tracked for a given kit. |
| 9 | `RECEIVED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date/time that a kit is scheduled to expire. |
| 10 | `RECEIVED_PERSONNEL_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the personnel that received the kit. |
| 11 | `RECEIVED_QTY_NBR` | DOUBLE | NOT NULL |  | This field contains the number of items received in the associated kit. |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the status associated with the lot. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `KIT_DEFINITION_ID` | [PCS_KIT_DEFINITION](PCS_KIT_DEFINITION.md) | `KIT_DEFINITION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `KIT_INFORMATION_ID` |

