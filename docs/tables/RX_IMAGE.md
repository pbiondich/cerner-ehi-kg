# RX_IMAGE

> Stores the unique key for an image to CDI as well as the corresponding image attributes.

**Description:** Pharmacy Order Image  
**Table type:** ACTIVITY  
**Primary key:** `IMAGE_ID`  
**Columns:** 23  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANNOTATE_IND` | DOUBLE | NOT NULL |  | Indicates if annotations exist on the image. |
| 2 | `CLARIFY_REASON_CD` | DOUBLE | NOT NULL |  | The code value for the reason the image was put in a clarify status. |
| 3 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The link to LONG_TEXT which includes comments associated to the image. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The time the image was added into the system. |
| 5 | `CREATE_TZ` | DOUBLE | NOT NULL |  | The time zone associated with CREATE_DT_TM. |
| 6 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | The device that was responsible for sending the image. |
| 7 | `DEVICE_FAC_CD` | DOUBLE | NOT NULL | FK→ | The facility the device is located in. |
| 8 | `DEVICE_LOC_CD` | DOUBLE | NOT NULL | FK→ | The location the device was located at at the time the image was sent. |
| 9 | `DOC_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of order stored within the image. |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter associated with the image. |
| 11 | `IMAGE_HANDLE_IDENTIFIER` | VARCHAR(255) | NOT NULL |  | The unique identifier for images within the CDI data model. |
| 12 | `IMAGE_ID` | DOUBLE | NOT NULL | PK | The unique, generated identifier for images within the Pharmacy Order Imaging data model. |
| 13 | `LAST_ACCESS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The User ID associated to the user who has last accessed the image. |
| 14 | `PARENT_IMAGE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the parent image if this image has been merged into. |
| 15 | `PATIENT_FAC_CD` | DOUBLE | NOT NULL |  | The patient's facility at the time that patient was assigned to an image. |
| 16 | `PATIENT_LOC_CD` | DOUBLE | NOT NULL |  | The patient's location at the time the patient was assigned to an image. |
| 17 | `RX_PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the order stored within the image. |
| 18 | `STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the image. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DEVICE_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `DEVICE_FAC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `DEVICE_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_ACCESS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_IMAGE_ID` | [RX_IMAGE](RX_IMAGE.md) | `IMAGE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RX_IMAGE](RX_IMAGE.md) | `PARENT_IMAGE_ID` |
| [RX_IMAGE_HX](RX_IMAGE_HX.md) | `IMAGE_ID` |
| [RX_IMG_IMGQUE_RELTN](RX_IMG_IMGQUE_RELTN.md) | `IMAGE_ID` |
| [RX_IMG_IMGQUE_RELTN_HX](RX_IMG_IMGQUE_RELTN_HX.md) | `IMAGE_ID` |

