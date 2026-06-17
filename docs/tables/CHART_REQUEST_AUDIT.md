# CHART_REQUEST_AUDIT

> chart_request_audit

**Description:** This is an audit table for MRP requests.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL |  | Primary key to the chart_request table |
| 6 | `COMMENTS` | VARCHAR(255) |  |  | It stores the comments entered through MRP.dll. |
| 7 | `DEST_PE_ID` | DOUBLE | NOT NULL |  | Id of the dest. Can be "PERSON", "ORGANIZATION", "FREETEXT", or "LOCATION". |
| 8 | `DEST_PE_NAME` | VARCHAR(32) |  |  | Parent entity name of the dest_pe_id. Can be "PERSON", "ORGANIZATION", "FREETEXT", or "LOCATION". |
| 9 | `DEST_TXT` | VARCHAR(32) |  |  | The free text for destination. If dest_pe_name is "FREETEXT", the field will be populated. |
| 10 | `INPUT_DEVICE` | VARCHAR(16) |  |  | The IP address for input device. |
| 11 | `PATCONOBT_IND` | DOUBLE |  |  | Patient consent obtained Indicator |
| 12 | `REASON_CD` | DOUBLE | NOT NULL |  | code value for reason |
| 13 | `REQUESTOR_PE_ID` | DOUBLE | NOT NULL |  | Id of the requestor. Can be "PERSON", "ORGANIZATION", "FREETEXT", or "LOCATION". |
| 14 | `REQUESTOR_PE_NAME` | VARCHAR(32) |  |  | Parent entity name of the requestor_pe_id. Can be "PERSON", "ORGANIZATION", "FREETEXT", or "LOCATION". |
| 15 | `REQUESTOR_TXT` | VARCHAR(32) |  |  | free text for requestor. If requestor_pe_name is "FREETEXT", the field will be populated. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

