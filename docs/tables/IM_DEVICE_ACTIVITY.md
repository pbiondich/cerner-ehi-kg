# IM_DEVICE_ACTIVITY

> IM Device Activity

**Description:** This table contains information specific to the DICOM services supported.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AE_TITLE` | VARCHAR(16) |  |  | This column contains the Application Entity Title for the specific DICOM service. |
| 2 | `IM_ACTIVITY_CD` | DOUBLE | NOT NULL |  | This column contains identifies the activity/service that is associated with a device. |
| 3 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_DEVICE table. It indicates the device with which the activities are associated. |
| 4 | `PORT` | DOUBLE |  |  | This column identifies the network port used for this specific device/activity. |
| 5 | `PRIMARY_IND` | DOUBLE |  |  | This column indicates if this device is the primary device used for this activity. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |

