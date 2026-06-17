# SESSION_XREF

> The session_xref table is linked to the session log table. It will link the output handle to the session number.

**Description:** Session Cross Reference  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Unique number that identifies the Device. Foreign key into the device table. |
| 2 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | Unique number that identifies the Output Dest. Foreign key into the output dest table |
| 3 | `OUTPUT_HANDLE_ID` | DOUBLE | NOT NULL |  | value that identifies a specific report |
| 4 | `PHYSICAL_CHANNEL_NAME` | VARCHAR(40) |  |  | the name of the physical channel used in this session |
| 5 | `SESSION_NUM` | DOUBLE | NOT NULL |  | Sequential number assigned at time of transmission. |
| 6 | `SESSION_STATUS` | DOUBLE |  |  | The status of the session. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

