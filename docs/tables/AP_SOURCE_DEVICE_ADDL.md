# AP_SOURCE_DEVICE_ADDL

> This table contains parameters defined of an imaging source device. The include parameters required to connect to a foreign imaging system.

**Description:** AP Source Device Additional Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_SOURCE_DEVICE_ADDL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies additional information related to a given source device. |
| 2 | `DEVICE_PASSWORD` | VARCHAR(100) |  |  | Contains the password required to access an imaging device/system. |
| 3 | `DEVICE_USERNAME` | VARCHAR(100) |  |  | Contains the username required to access an imaging device/system. |
| 4 | `IMAGE_SERVER_URL` | VARCHAR(1000) |  |  | Applications can access image server to check if slide images are available for a given pathology case. |
| 5 | `NETWORK_SHARE_PATH` | VARCHAR(1000) |  |  | Contains the path of a network file share that could be used to acquire images from an imaging device/system. |
| 6 | `SOURCE_DEVICE_CD` | DOUBLE | NOT NULL |  | Contains the code_value of the device to which the additional information relates. |
| 7 | `SOURCE_DEVICE_URL` | VARCHAR(1000) |  |  | Contains the URL address used to access an imaging device/system. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

