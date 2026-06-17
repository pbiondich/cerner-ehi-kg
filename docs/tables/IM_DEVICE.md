# IM_DEVICE

> IM Device

**Description:** This table contains DICOM and non-DICOM information about the device.  
**Table type:** REFERENCE  
**Primary key:** `IM_DEVICE_ID`  
**Columns:** 19  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_QC_IND` | DOUBLE |  |  | This column indicates if the device/modality should support auto QC. |
| 2 | `DEVICE_NAME` | VARCHAR(25) |  |  | Unique name of device or display of a digital exam room |
| 3 | `DEVICE_NAME_KEY` | VARCHAR(25) |  |  | This is the device name in upper case. This is used for indexing and searching for a device based on device name. |
| 4 | `DEVICE_NAME_KEY_A_NLS` | VARCHAR(100) |  |  | DEVICE_NAME_KEY_A_NLS column |
| 5 | `DEVICE_NAME_KEY_NLS` | VARCHAR(52) |  |  | This is the device name in upper case for NLS sites. This is used for indexing and searching for a device based on device name. |
| 6 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | PK | This column contains a unique meaningless number that only serves the purpose of identifying a row. |
| 7 | `IP_ADDRESS` | VARCHAR(64) |  |  | This column contains the network IP address of the device. |
| 8 | `MODEL_NAME` | VARCHAR(64) |  |  | The model name. |
| 9 | `MODEL_NAME_KEY` | VARCHAR(64) |  |  | This is the model name in upper case. This is used for indexing and searching for a device based on model name. |
| 10 | `MODEL_NAME_KEY_A_NLS` | VARCHAR(256) |  |  | MODEL_NAME_KEY_A_NLS column |
| 11 | `MODEL_NAME_KEY_NLS` | VARCHAR(130) |  |  | This is the model name in upper case for NLS sites. This is used for indexing and searching for a device based on model name. |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the Service Resource table. For radiology it would be at the exam room level. |
| 13 | `TIMEZONE` | DOUBLE | NOT NULL |  | Time zone for the device |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VENDOR_CD` | DOUBLE | NOT NULL |  | This column identifies the vendor of the device. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [AUTO_MATCH_DEFINITION](AUTO_MATCH_DEFINITION.md) | `IM_DEVICE_ID` |
| [IM_ACQUIRED_STUDY](IM_ACQUIRED_STUDY.md) | `IM_DEVICE_ID` |
| [IM_ACQUIRED_STUDY](IM_ACQUIRED_STUDY.md) | `SENDING_DEVICE_ID` |
| [IM_DEVICE_ACTIVITY](IM_DEVICE_ACTIVITY.md) | `IM_DEVICE_ID` |
| [IM_DEVICE_DISCIPLINE_R](IM_DEVICE_DISCIPLINE_R.md) | `IM_DEVICE_ID` |
| [IM_DEVICE_MWL_RULE_R](IM_DEVICE_MWL_RULE_R.md) | `IM_DEVICE_ID` |
| [IM_DEVICE_ORG_R](IM_DEVICE_ORG_R.md) | `IM_DEVICE_ID` |
| [IM_DEVICE_RESOURCE_R](IM_DEVICE_RESOURCE_R.md) | `IM_DEVICE_ID` |
| [IM_STUDY_LOCATION](IM_STUDY_LOCATION.md) | `IM_DEVICE_ID` |
| [IM_U_NOTIFY](IM_U_NOTIFY.md) | `IM_DEVICE_ID` |
| [UPD_IMAGE_HDR_DEF](UPD_IMAGE_HDR_DEF.md) | `IM_DEVICE_ID` |

