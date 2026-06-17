# REPORT_QUEUE

> The report queue is the actual records that need to be processed, have been selected to be processed or have already been transmitted.

**Description:** Report Queue  
**Table type:** ACTIVITY  
**Primary key:** `OUTPUT_HANDLE_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONVERTED_FILE_CHECKSUM` | DOUBLE | NOT NULL |  | The checksum for the converted file |
| 2 | `CONVERTED_FILE_IDENTIFIER` | VARCHAR(64) |  |  | The media object identifier for the converted report file. |
| 3 | `CONVERTED_FILE_NAME` | VARCHAR(300) |  |  | This will be the full path name and report name for the report that needs to be converted to the correct device driver format. UNC paths are preferred |
| 4 | `CUTOFF_DT_TM` | DATETIME |  |  | The cutoff time which indicates the last possible time that the report can be transmitted in the current time scheme. Blank if not defined. |
| 5 | `NEXT_AGING_DT_TM` | DATETIME |  |  | If the report has waited past a certain time parameter then it's transmit date and time will be moved to an earlier time. This represents that time. |
| 6 | `NUM_OF_BUSY` | DOUBLE |  |  | How many times this report has attempted to transmit and received a busy signal. |
| 7 | `NUM_OF_DISCONNECT` | DOUBLE |  |  | How many times this report attempted to transmit and received a disconnect while transmitting. |
| 8 | `NUM_OF_NOCONNECT` | DOUBLE |  |  | How many time this report has attempted to transmit and received a noconnect signal. |
| 9 | `ORIGINAL_DT_TM` | DATETIME |  |  | The time the original report was requestedColumn |
| 10 | `OUTPUT_HANDLE_ID` | DOUBLE | NOT NULL | PK | Value that identifies a specific report. Foreign key into the outputctx table....Matches up with the Handle_id field. |
| 11 | `PRIORITY_VALUE` | DOUBLE |  |  | The current priority level of this report. If multiple reports were set to transmit at the same time, this priority would determine in what order they should be transmitted. |
| 12 | `TRANSMISSION_STATUS_CD` | DOUBLE | NOT NULL |  | The current transmission status of the report. |
| 13 | `TRANSMIT_DT_TM` | DATETIME |  |  | The next valid time that the report can be transmitted based on time scheme criteria. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRANS_ADMIT_NOTIFY_ALT](TRANS_ADMIT_NOTIFY_ALT.md) | `REPORT_QUEUE_ID` |

