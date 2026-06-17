# RXS_WORKLIST

> Contains worklist parameters for generating pharmacy tasks automatically through an operations job.

**Description:** RxStation Worklist  
**Table type:** REFERENCE  
**Primary key:** `RXS_WORKLIST_ID`  
**Columns:** 22  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTO_PKG_DEST_FOLDER_NAME` | VARCHAR(255) | NOT NULL |  | The destination folder where the flat file generated for an auto-packaging machine will be placed. |
| 3 | `AUTO_PKG_IND` | DOUBLE | NOT NULL |  | Indicates if this worklist will generate a flat file to be read by an auto-packaging machine. |
| 4 | `AUTO_PKG_PROD_IDENT_TYPE_CD` | DOUBLE | NOT NULL |  | The product type code that the drugs in the auto-packaging machine are identified by. For example, NDC, HIN, etc. |
| 5 | `AUTO_PKG_SCRIPT_CD` | DOUBLE | NOT NULL |  | Identifies the script that generates the flat file for the auto-packaging machine. |
| 6 | `DYNAMIC_PAR_BUFFER_PCT` | DOUBLE | NOT NULL |  | Defines the percentage to increase or decrease the system calculated refill level. |
| 7 | `DYNAMIC_PAR_HRS` | DOUBLE | NOT NULL |  | Defines how many hours in the future to look for orders while calculating dynamic refill levels. |
| 8 | `DYNAMIC_PAR_IND` | DOUBLE | NOT NULL |  | Indicates whether the system will use the system-calculated refill level (1) or the user-entered refill level (0) when determining items. |
| 9 | `LABEL_CD` | DOUBLE | NOT NULL |  | The format used when the worklist is printed on a label. |
| 10 | `LABEL_PRINTER_CD` | DOUBLE | NOT NULL | FK→ | The printer that labels are spooled to. |
| 11 | `PRINT_CONSOLIDATED_RPT_IND` | DOUBLE | NOT NULL |  | Indicates if the consolidated report is to be printed. |
| 12 | `PRINT_DTL_RPT_IND` | DOUBLE | NOT NULL |  | Indicates if the unit detail report is to be printed. |
| 13 | `REPORT_CD` | DOUBLE | NOT NULL |  | The format used when the worksheet is printed on a report. |
| 14 | `REPORT_PRINTER_CD` | DOUBLE | NOT NULL | FK→ | The printer that reports are spooled to. |
| 15 | `RXS_WORKLIST_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_WORKLIST table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WORKLIST_NAME` | VARCHAR(255) | NOT NULL |  | The user-defined name for the worklist. |
| 22 | `WORKLIST_TYPE_CD` | DOUBLE | NOT NULL |  | Describes the type of worklist to be run. Examples: Scheduled, Ad hoc |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LABEL_PRINTER_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `REPORT_PRINTER_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [QUANTITY_REQUIREMENT_INFO](QUANTITY_REQUIREMENT_INFO.md) | `DEMAND_WORKLIST_ID` |
| [RXS_WORKLIST_DISP_CAT_R](RXS_WORKLIST_DISP_CAT_R.md) | `RXS_WORKLIST_ID` |
| [RXS_WORKLIST_EVENT](RXS_WORKLIST_EVENT.md) | `RXS_WORKLIST_ID` |
| [RXS_WORKLIST_LEGAL_STATUS](RXS_WORKLIST_LEGAL_STATUS.md) | `RXS_WORKLIST_ID` |
| [RXS_WORKLIST_LOCATION_R](RXS_WORKLIST_LOCATION_R.md) | `RXS_WORKLIST_ID` |

