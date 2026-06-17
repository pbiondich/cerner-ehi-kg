# OUTPUT_DEST

> Output Destination Table

**Description:** Output Destination  
**Table type:** REFERENCE  
**Primary key:** `OUTPUT_DEST_CD`  
**Columns:** 18  
**Referenced by:** 21 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Output Destination Name |
| 2 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Unique Number identifying the Device |
| 3 | `JOB_FILE_PATH` | VARCHAR(1000) |  |  | This will allow teams who support label printing to specify custom locations for printer-specific file storage. |
| 4 | `LABEL_PREFIX` | VARCHAR(20) |  |  | Prefix for the label |
| 5 | `LABEL_PROGRAM_NAME` | VARCHAR(20) |  |  | Label Program Name |
| 6 | `LABEL_XPOS` | DOUBLE |  |  | Label XPos |
| 7 | `LABEL_YPOS` | DOUBLE |  |  | Label YPos |
| 8 | `NAME` | VARCHAR(20) |  |  | Output Destination Name |
| 9 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | PK | Unique number identifying the Output Destination |
| 10 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | Output Device |
| 11 | `OUTPUT_TO_FILE_IND` | DOUBLE |  |  | Indicator |
| 12 | `SCRIPT` | VARCHAR(100) |  |  | scrip |
| 13 | `TAMPERPROOF_IND` | DOUBLE | NOT NULL |  | Indicates wether an output dest is capable of tamperproof printing |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (21)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `OUTPUT_DEST_CD` |
| [CHART_SERVER_PRINTER](CHART_SERVER_PRINTER.md) | `OUTPUT_DEST_CD` |
| [CR_OUTPUT_DESTINATION](CR_OUTPUT_DESTINATION.md) | `OUTPUT_DEST_CD` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `OUTPUT_DEST_CD` |
| [EEM_ABN_FORM](EEM_ABN_FORM.md) | `OUTPUT_DEST_ID` |
| [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `OUTPUT_DEST_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `OUTPUT_DEST_CD` |
| [EXPEDITE_PARAMS](EXPEDITE_PARAMS.md) | `OUTPUT_DEST_CD` |
| [MIC_ANG_TIMES](MIC_ANG_TIMES.md) | `PRINTER_CD` |
| [MIC_SEQ_PRINTER](MIC_SEQ_PRINTER.md) | `OUTPUT_DEST_ID` |
| [ORD_FAVORITE_DEST](ORD_FAVORITE_DEST.md) | `OUTPUT_DEST_ID` |
| [OUTPUT_DEST_XREF](OUTPUT_DEST_XREF.md) | `OUTPUT_DEST_CD` |
| [PC_ATTRIBUTE_VALUE](PC_ATTRIBUTE_VALUE.md) | `ATTRIBUTE_VALUE_OUTPUT_DEST_CD` |
| [PM_DOC_PRINT_HIST](PM_DOC_PRINT_HIST.md) | `OUTPUT_DESTINATION_ID` |
| [PM_POST_DOC_REF](PM_POST_DOC_REF.md) | `OUTPUT_DEST_CD` |
| [PROP_ORDER](PROP_ORDER.md) | `LABEL_PRINTER_ID` |
| [SCH_ACTION_NOTIFY](SCH_ACTION_NOTIFY.md) | `OUTPUT_DEST_ID` |
| [SCH_NOTIFY](SCH_NOTIFY.md) | `OUTPUT_DEST_ID` |
| [SCH_ROUTE_LIST](SCH_ROUTE_LIST.md) | `OUTPUT_DEST_ID` |
| [SN_RPT_DEST](SN_RPT_DEST.md) | `OUTPUT_DEST_ID` |
| [STATION](STATION.md) | `OUTPUT_DEST_CD` |

