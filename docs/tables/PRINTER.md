# PRINTER

> This table lists printers and their attributes.

**Description:** PRINTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_CUSTOM_FORM_NAME` | VARCHAR(256) |  |  | The default custom form for printing for the specified output destination code. |
| 2 | `DEFAULT_ORIENTATION_FLAG` | DOUBLE | NOT NULL |  | The default paper orientation for the specified output destination code: 1 - portrait, 2 - landscape. |
| 3 | `DEFAULT_PAPER_HANDLING_FLAG` | DOUBLE | NOT NULL |  | The default paper handling for the specified output destination code: 1 - simplex, 2 - duplex (long-edge binding, vertical), 3 - tumble (short-edge binding, horizontal). |
| 4 | `DEFAULT_TRAY_NAME` | VARCHAR(20) |  |  | The default tray name for the specifed output destination code. |
| 5 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Number derived from Outputctx_seq or Reference_seq. Must match the device_cd of the device record that represents the printer. It is the unique primary key of the Printer table. |
| 6 | `DEVICE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `IPP_LEGACY_FLAG` | DOUBLE | NOT NULL |  | Controls if the IPP Legacy feature flag is forced on or off for this printer. |
| 8 | `PRINTER_TYPE_CD` | DOUBLE | NOT NULL |  | DIO printer type derived from the associated code set. |
| 9 | `TIMEZONE_CD` | DOUBLE | NOT NULL |  | This column is no longer used |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

