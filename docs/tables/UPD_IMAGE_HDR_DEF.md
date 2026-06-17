# UPD_IMAGE_HDR_DEF

> Update Image Header Definition

**Description:** This table contains the DICOM tags that should be sent to the archive as an upd  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCIPLINE_CD` | DOUBLE | NOT NULL |  | The discipline, such as radiology or cardiology, for which the update image header definition data applies. |
| 2 | `FALLBACK_VALUE_TYPE` | VARCHAR(16) |  |  | The field that determines which fallback type source should be used when primary id is unavailable. |
| 3 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | The specific device for which the update image header definition data applies. |
| 4 | `TAG` | VARCHAR(11) | NOT NULL | FK→ | This column contains a foreign key to the IMAGE_MATCH_TAG table. It identifies the DICOM tag. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `VALUE_TYPE` | VARCHAR(16) | NOT NULL |  | The definable type of value contained in the flag. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |
| `TAG` | [IMAGE_MATCH_TAG](IMAGE_MATCH_TAG.md) | `TAG` |

