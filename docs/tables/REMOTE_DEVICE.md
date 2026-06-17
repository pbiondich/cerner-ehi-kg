# REMOTE_DEVICE

> THE Remote Device Table

**Description:** Remote Device Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_CD` | DOUBLE | NOT NULL |  | Unique numberColumn |
| 2 | `AREA_CODE` | CHAR(25) |  |  | Area code for the remote device |
| 3 | `COUNTRY_ACCESS` | CHAR(25) |  |  | Country access number for the remote deviceColumn |
| 4 | `DEVICE_ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | Unique number for the Device Address TypeColumn |
| 5 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Unique number for the DeviceColumn |
| 6 | `EXCHANGE` | CHAR(25) |  |  | Exchange portion of the phone numberColumn |
| 7 | `LOCAL_FLAG` | DOUBLE |  |  | Local FlagColumn |
| 8 | `PHONE_MASK_ID` | DOUBLE | NOT NULL |  | Identifies the phone mask used for this deviceColumn |
| 9 | `PHONE_SUFFIX` | CHAR(50) |  |  | Phone suffix portion of the phone numberColumn |
| 10 | `REMOTE_DEV_TYPE_ID` | DOUBLE | NOT NULL |  | Unique number that identifies the remote device type attached to this remote device. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

