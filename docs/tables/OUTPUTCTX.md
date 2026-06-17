# OUTPUTCTX

> Table for tracking reprints

**Description:** OUTPUTCTX  
**Table type:** ACTIVITY  
**Primary key:** `HANDLE_ID`  
**Columns:** 37  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(256) |  |  | This field contains the ACCESSION number (alphanumeric) for the report. It is parsed from the REPORT_NAME field if available. |
| 2 | `ADHOC_AREA_CODE` | CHAR(10) |  |  | Area code to use if RRD |
| 3 | `ADHOC_COUNTRY_ACCESS` | CHAR(3) |  |  | Country access to use if RRD |
| 4 | `ADHOC_EXCHANGE` | CHAR(10) |  |  | Exchange number to use if this is RRD |
| 5 | `ADHOC_PHONE_SUFFIX` | VARCHAR(50) |  |  | Phone number suffix to use if this is RRD |
| 6 | `APPLCTX` | DOUBLE |  |  | Application context number of requesting app |
| 7 | `CHECKSUM` | DOUBLE |  |  | Used to store checksum of the reprinted file |
| 8 | `CHILD_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | Handle id for any child jobs associated with this handle |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 10 | `DELIVER_DT_TM` | DATETIME |  |  | When this reprint is to be distributed via RRD |
| 11 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Device id that was used for reprinting |
| 12 | `FILE_IDENTIFIER` | VARCHAR(64) |  |  | The media object identifier for the output context file. |
| 13 | `FILE_LOCATION` | VARCHAR(128) |  |  | This field contains the full file pathname or is blank if the pathname is specified in the FILE_NAME field. It may be a UNC path or a path specific to a particular node. It may contain logicals such as CER_PRINT. |
| 14 | `FILE_NAME` | VARCHAR(128) |  |  | This field contains the base filename. If FILE_LOCATION is blank, this field may contain the full path and filename. If there is a pathname, it may be a UNC path or a path specific to a particular node. It may contain logicals such as CER_PRINT. |
| 15 | `HANDLE_ID` | DOUBLE | NOT NULL | PK | This handle is the uniqueID used to track entries on this table, i.e. print jobs. It is the primary key of this table. |
| 16 | `MRN` | VARCHAR(256) |  |  | This field contains the MRN for the report. It is parsed from the REPORT_NAME field if available. |
| 17 | `NOTIFICATION_TYPE` | DOUBLE |  |  | This field specifies the type of notification that would be sent to the user identified by the NOTIFY_USER_ID field. Used by RRD. |
| 18 | `NOTIFY_USER_ID` | DOUBLE | NOT NULL |  | The user id for RRD to notify |
| 19 | `NUMBER_OF_PAGES` | DOUBLE |  |  | This field contains the number of pages in a file or 0 if pagination has not been performed. |
| 20 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | The output destination id that this reprint was sent to |
| 21 | `PARENT_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | The handle ID to any parent of this job |
| 22 | `PEER_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | The handle ID to any peer jobs that are part of this reprint |
| 23 | `PERSON_NAME` | VARCHAR(128) |  |  | This field contains the name of the person who is the subject of this report. It is parsed from the REPORT_NAME field if available. |
| 24 | `PHONE_NUMBER` | VARCHAR(73) |  |  | This field contains the entire phone number for ADHOC faxes. It is a composite of the fields ADHOC_COUNTRY_ACCESS, ADHOC_AREA_CODE, ADHOC_EXCHANGE, and ADHOC_PHONE_SUFFIX |
| 25 | `PRIORITY` | DOUBLE |  |  | Reprint priority |
| 26 | `PURGE_DT_TM` | DATETIME |  |  | The date and time this handle and file should be purge |
| 27 | `REPORT_NAME` | VARCHAR(255) |  |  | The name of the report |
| 28 | `REPRINT_HANDLE_ID` | DOUBLE | NOT NULL |  | The handle id of any reprints of this file |
| 29 | `REQUESTING_USER_ID` | DOUBLE | NOT NULL |  | The user id of the requester |
| 30 | `SECURITY` | DOUBLE |  |  | The security tag |
| 31 | `SERVER` | VARCHAR(128) |  |  | The server name |
| 32 | `STATUS_FLAG` | DOUBLE |  |  | The status flag is used in printing to track the state of a document. The field is not used for RRD reports in favor of the transmission_status_cd field on the REPORT_QUEUE table.The following values are supported: 0 = checked out 1 = checked in / ready to process 2 = processing 3 = completed 99 = generic error status |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `PARENT_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `PEER_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [CDI_WORK_ITEM_ACTION](CDI_WORK_ITEM_ACTION.md) | `OUTPUTCTX_HANDLE_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `HANDLE_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `RRD_HANDLE_ID` |
| [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `HANDLE_ID` |
| [OUTPUTCTX](OUTPUTCTX.md) | `CHILD_HANDLE_ID` |
| [OUTPUTCTX](OUTPUTCTX.md) | `PARENT_HANDLE_ID` |
| [OUTPUTCTX](OUTPUTCTX.md) | `PEER_HANDLE_ID` |
| [RRDBRIDGE](RRDBRIDGE.md) | `OUTPUT_HANDLE_ID` |

