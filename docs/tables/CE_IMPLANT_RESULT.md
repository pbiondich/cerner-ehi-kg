# CE_IMPLANT_RESULT

> Track the devices implanted or extracted from a person.

**Description:** CE IMPLANT RESULT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_NBR` | VARCHAR(15) |  |  | Batch number of the implant/explant. |
| 2 | `CULTURE_IND` | DOUBLE |  |  | Is the implant cultured? |
| 3 | `ECRI_CODE` | VARCHAR(20) |  |  | Electronic tracking code for the implant/explant. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical_event table. |
| 5 | `EXPIRATION_DT_TM` | DATETIME |  |  | Time at which the implant expires. |
| 6 | `EXPLANT_DISPOSITION_CD` | DOUBLE | NOT NULL |  | Indicates where the explant was sent. |
| 7 | `EXPLANT_REASON_CD` | DOUBLE | NOT NULL |  | Reason for explant. |
| 8 | `HARVEST_SITE` | VARCHAR(50) |  |  | Site of the explant. |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to the item_definition table. |
| 10 | `ITEM_SIZE` | VARCHAR(25) |  |  | The size of the implant/explant. |
| 11 | `LOT_NBR` | VARCHAR(15) |  |  | Lot number of the implant/explant. |
| 12 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | Manufacturer code for the implant/explant. |
| 13 | `MANUFACTURER_FT` | VARCHAR(50) |  |  | Free-text manufacturer name. |
| 14 | `MODEL_NBR` | VARCHAR(15) |  |  | Model number of the implant/explant. |
| 15 | `OTHER_IDENTIFIER` | VARCHAR(30) |  |  | An additional identifier for the implant/explant. Site defined. |
| 16 | `REFERENCE_ENTITY_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** An foreign key to another table specified in reference_name. |
| 17 | `REFERENCE_ENTITY_NAME` | VARCHAR(32) |  |  | *** OBSOLETE *** Context field for the reference_entity_id. |
| 18 | `TISSUE_GRAFT_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the graft type. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Time at which the event became valid. |
| 25 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Time at which the event ceased to be valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

