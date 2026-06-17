# DEVICE

> THE Device Table

**Description:** Device Table  
**Table type:** REFERENCE  
**Primary key:** `DEVICE_CD`  
**Columns:** 17  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_FOLDER_PATH` | VARCHAR(255) |  |  | The base folder for the specified device |
| 2 | `DESCRIPTION` | VARCHAR(110) |  |  | The description of the device. |
| 3 | `DEVICE_CD` | DOUBLE | NOT NULL | PK | The unique primary key of the Device table. It does not have a code set associated with it. |
| 4 | `DEVICE_FUNCTION_CD` | DOUBLE | NOT NULL |  | The device_function_cd is mainly to help distinguish a fax from a remote printer from a local printer. Basically how the device will distribute (i.e. remotely, network, local, fax, etc.) |
| 5 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the type of device. Some examples are printer, IV pump, monitor, fax, etc.) |
| 6 | `DISTRIBUTION_FLAG` | DOUBLE | NOT NULL |  | Determines the type of distribution that this device is configured for:0 = CCL1 = WINDOWS |
| 7 | `DMS_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the DMS_SERVICE table to represent which Digital Media Service that this DEVICE row maps to. If there is no corresponding mapping then this column will be left blank. |
| 8 | `LOCAL_ADDRESS` | VARCHAR(20) |  |  | The local address name for the device. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location of the device. |
| 10 | `MEDIA_TYPE_ENUM` | DOUBLE | NOT NULL |  | The media type supported by the specified divide. Will hold a numeric value corresponding to the types supported. |
| 11 | `NAME` | VARCHAR(50) |  |  | The name of the device. |
| 12 | `PHYSICAL_DEVICE_NAME` | VARCHAR(50) |  |  | The physical printer name of the specified device. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DMS_SERVICE_ID` | [DMS_SERVICE](DMS_SERVICE.md) | `DMS_SERVICE_ID` |

## Referenced by (11)

| From table | Column |
|------------|--------|
| [CR_DESTINATION_XREF](CR_DESTINATION_XREF.md) | `DEVICE_CD` |
| [DEVICE_OUTPUT_RELTN](DEVICE_OUTPUT_RELTN.md) | `DEVICE_CD` |
| [FILL_BATCH](FILL_BATCH.md) | `DEFAULT_PRINTER_CD` |
| [FORM_LIBRARY_MAPPING](FORM_LIBRARY_MAPPING.md) | `PRINTER_ID` |
| [FORM_LIBRARY_MAPPING](FORM_LIBRARY_MAPPING.md) | `REDIRECT_PRINTER_ID` |
| [PC_ATTRIBUTE_VALUE](PC_ATTRIBUTE_VALUE.md) | `DEVICE_CD` |
| [RXS_WORKLIST](RXS_WORKLIST.md) | `LABEL_PRINTER_CD` |
| [RXS_WORKLIST](RXS_WORKLIST.md) | `REPORT_PRINTER_CD` |
| [RX_IMAGE](RX_IMAGE.md) | `DEVICE_CD` |
| [RX_PRINTER_LOCATION_R](RX_PRINTER_LOCATION_R.md) | `DENIAL_REPORT_DEVICE_CD` |
| [RX_PRINTER_LOCATION_R](RX_PRINTER_LOCATION_R.md) | `DEVICE_CD` |

