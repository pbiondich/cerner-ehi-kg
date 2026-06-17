# CR_OUTPUT_DESTINATION

> Holds output destinations for a report request

**Description:** CR_OUTPUT_DESTINATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COPIES_NBR` | DOUBLE | NOT NULL |  | Number of copies to distribute |
| 2 | `CR_OUTPUT_DESTINATION_ID` | DOUBLE | NOT NULL |  | Primary key - A final location for a report request to be sent |
| 3 | `DISK_LABEL` | VARCHAR(128) |  |  | Label to be burnt to Disk |
| 4 | `DISK_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of disk (DVD = 2 or CD = 1) |
| 5 | `DISTRIBUTED_STATUS_IND` | DOUBLE | NOT NULL |  | STATUS INDICATOR for the Distributed Job 0 = ERRORED. 1 = SUCCESSFUL. |
| 6 | `DMS_ADHOC_FAX_NUMBER_TXT` | VARCHAR(40) |  |  | Ad hoc fax number |
| 7 | `DMS_FAX_DISTRIBUTE_DT_TM` | DATETIME |  |  | Date\Time to distribute fax |
| 8 | `DMS_SERVICE_IDENT` | VARCHAR(110) |  |  | Service Identifier of device |
| 9 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Output destination code for local printers. This is a value from the OUTPUT_DEST table (not a code set). |
| 10 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key - output destination for that report request |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |

