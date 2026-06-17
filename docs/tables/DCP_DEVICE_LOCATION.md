# DCP_DEVICE_LOCATION

> Specifies the Device that is installed in a given location

**Description:** DCP DEVICE LOCATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DCP_DEVICE_LOCATION_ID` | DOUBLE | NOT NULL |  | Device Location ID. Primary Key from CareNet_seq |
| 4 | `DNS_NAME` | VARCHAR(255) |  |  | Specifies the DNS name of the deviceColumn |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `IP_ADDRESS` | VARCHAR(255) |  |  | Specifies the IP address of the device |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Specifies the location the device is installed at |
| 8 | `PASSWORD_TXT` | VARCHAR(100) | NOT NULL |  | Specifies the password that should be used to gain access to the device. |
| 9 | `PORT_NUMBER` | DOUBLE |  |  | Specifies the port number for the IP Address |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `USERNAME_TXT` | VARCHAR(50) | NOT NULL |  | Specifies the user name that should be used to connect to the device |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

