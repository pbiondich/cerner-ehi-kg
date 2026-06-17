# AUTO_MATCH_DEFINITION

> Auto Match Definition

**Description:** This table contains the DICOM tags that should be used during auto matching  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | This column is used to flex the definitions by modality |
| 2 | `AUTO_MATCH_DEF_ID` | DOUBLE | NOT NULL |  | This column is the primary key and is set using the clin_image_seq number. |
| 3 | `DISCIPLINE_CD` | DOUBLE | NOT NULL |  | The discipline, such as radiology or cardiology, for which the auto match definition data applies. |
| 4 | `HISTORICAL_IND` | DOUBLE |  |  | Indicator is used to tell whether or not the row is for a historical auto match definition |
| 5 | `IMAGE_TAG` | VARCHAR(11) | NOT NULL | FK→ | this column is a foreign key to the IMAGE_MATCH_TAG table. It identifies the DICOM tag from the image that should be compared. |
| 6 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_DEVICE table. It allows for flexing the definition by a specific exam room. |
| 7 | `RIS_TAG` | VARCHAR(11) | NOT NULL | FK→ | This column is a foreign key to the IMAGE_MATCH_TAG table. It identifies the tag from the RIS that should be used to compare. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_TYPE` | VARCHAR(16) | NOT NULL |  | The definable type of value contained in the flag. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_TAG` | [IMAGE_MATCH_TAG](IMAGE_MATCH_TAG.md) | `TAG` |
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |
| `RIS_TAG` | [IMAGE_MATCH_TAG](IMAGE_MATCH_TAG.md) | `TAG` |

