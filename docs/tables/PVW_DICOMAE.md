# PVW_DICOMAE

> This table holds DICOM information regarding AE title, host and address.

**Description:** PVW_DICOMApplicationEntity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AE_HOST_ADDR` | VARCHAR(64) | NOT NULL |  | This field contains the IP host address of the location where the DICOM software is located. |
| 2 | `AE_HOST_NAME` | VARCHAR(64) | NOT NULL |  | This field contains the IP host name of the location where the DICOM software is located. |
| 3 | `AE_ID` | DOUBLE | NOT NULL |  | Unique identifier representing a row in the table. |
| 4 | `AE_TITLE` | VARCHAR(12) | NOT NULL |  | Application Entity Title |
| 5 | `ARCHIVE_LOCATION_CD` | DOUBLE | NOT NULL |  | Identifies the AE title that is responsible for the storage. |
| 6 | `PORT_NUMBER` | DOUBLE |  |  | Socket port number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Image viewer vendor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

