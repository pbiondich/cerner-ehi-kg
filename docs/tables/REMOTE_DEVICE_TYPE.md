# REMOTE_DEVICE_TYPE

> Defines the type of device at the remote site.

**Description:** REMOTE DEVICE TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BAUD_RATE` | DOUBLE |  |  | Baud RateColumn |
| 2 | `DATA_BITS` | DOUBLE |  |  | Data BitsColumn |
| 3 | `DATA_TYPE_CD` | DOUBLE |  |  | The type of device.Column |
| 4 | `DEVICE_MODE` | CHAR(1) |  |  | Device ModeColumn |
| 5 | `DEVICE_TYPE_CD` | DOUBLE |  |  | Device TypeColumn |
| 6 | `LINE_SPEED` | DOUBLE |  |  | Line speedColumn |
| 7 | `NAME` | VARCHAR(20) |  |  | Name of Remote DeviceColumn |
| 8 | `OUTPUT_FORMAT_CD` | DOUBLE |  |  | Printer Driver NameColumn |
| 9 | `PARITY` | CHAR(1) |  |  | ParityColumn |
| 10 | `PRINTER_SETUP_INFO` | VARCHAR(50) |  |  | Printer SetupColumn |
| 11 | `REMOTE_DEV_TYPE_ID` | DOUBLE | NOT NULL |  | Unique numeric identifierColumn |
| 12 | `RESOLUTION` | VARCHAR(25) |  |  | ResolutionColumn |
| 13 | `STOP_BIT` | DOUBLE |  |  | Stop bitColumn |
| 14 | `TRANS_CPI` | DOUBLE |  |  | Trans cpiColumn |
| 15 | `TRANS_LPI` | DOUBLE |  |  | Trans lpiColumn |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

