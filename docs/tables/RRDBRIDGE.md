# RRDBRIDGE

> This table is used to track documents that are to be sent to the Cerner Interchange server

**Description:** RRD BRIDGE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILE_NAME` | VARCHAR(200) | NOT NULL |  | Path and name of file to be sent |
| 2 | `MESSAGE_ID_HEADER` | VARCHAR(255) |  |  | Once the Secure Email is transmitted, Mime Message ID will be assigned to it. This ID is Unique. |
| 3 | `ORIGINAL_DT_TM` | DATETIME |  |  | The time the original report was requested |
| 4 | `OUTPUT_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | Value that identifies a specific report. Foreign Key from the OUTPUTCTX table (HANDLE_ID). |
| 5 | `RRDBRIDGE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `STATION_DEST_CD` | DOUBLE | NOT NULL | FK→ | Relates to STATION row containing fax number. It is NOT a code value, but really an ID value which originates from the OUTPUT_DEST table. |
| 7 | `SUBSTATUS` | VARCHAR(20) | NOT NULL |  | Descriptive text for reason of an ERROR status in TRANSMISSION_STATUS_CD |
| 8 | `TRANSMISSION_ATTEMPTS` | DOUBLE | NOT NULL |  | Number of times the document tried to send to Cerner Interchange. |
| 9 | `TRANSMISSION_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the transmission. |
| 10 | `TRANSMIT_DT_TM` | DATETIME | NOT NULL |  | Date and time of the transmission. Blank until successfully sent. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `STATION_DEST_CD` | [STATION](STATION.md) | `OUTPUT_DEST_CD` |

