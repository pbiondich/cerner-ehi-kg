# CHART_REQUEST

> This table defines the chart requests that are to be processed by the chart server.

**Description:** Chart Request  
**Table type:** ACTIVITY  
**Primary key:** `CHART_REQUEST_ID`  
**Columns:** 73  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) |  |  | This is the accession number for the results that will print on the accession level chart |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ADDL_COPIES` | DOUBLE |  |  | This defines whether additional copies of the chart should be printed |
| 7 | `BEGIN_DT_TM` | DATETIME |  |  | This is the date and time that is used to determine how far back the system should look when searching for results to be printed on the chart |
| 8 | `BEGIN_PAGE` | DOUBLE |  |  | The is the page number that the system begins printing at when a page range is specified for a chart |
| 9 | `CHART_BATCH_ID` | DOUBLE | NOT NULL |  | Stores a grouping batch ID for requests. The grouper value will be the PK value of the first Chart Request in the Batch. |
| 10 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This is the number that uniquely identifies the chart format |
| 11 | `CHART_PENDING_FLAG` | DOUBLE |  |  | This flag determines whether pending or verified or both types of procedures are printed on the chart |
| 12 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL | PK | This a unique number assigned to the chart request which allows that chart request to be resubmitted or skipped if needed |
| 13 | `CHART_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | Stores the unique identifier to the Chart Route |
| 14 | `CHART_STATUS_CD` | DOUBLE | NOT NULL |  | Used to store the status of the request. Replaces status_flag. |
| 15 | `CHART_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | TRIGGER ID VALUE FROM CHART_TRIGGER |
| 16 | `CR_MASK_ID` | DOUBLE | NOT NULL | FK→ | This is a number which uniquely identifies a chart mask |
| 17 | `DATE_RANGE_IND` | DOUBLE |  |  | This field indicates whether a date range is being used when printing the chart |
| 18 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | This is a number which uniquely identifies a chart distribution |
| 19 | `DIST_INITIATOR_IND` | DOUBLE |  |  | An indicator for the distribution initiator |
| 20 | `DIST_RUN_DT_TM` | DATETIME |  |  | This is the date and time that the distribution was started |
| 21 | `DIST_RUN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This is the code from the code set 22550 which determines what type of chart will be produced (i.e. interim, cummulative) |
| 22 | `DIST_TERMINATOR_IND` | DOUBLE |  |  | An indicator for the distribution terminator |
| 23 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 24 | `END_DT_TM` | DATETIME |  |  | This is the date and time when identifies the end of a date range that the system uses when looking for results |
| 25 | `END_PAGE` | DOUBLE |  |  | This is the page number that is the end of the range when a page range is requested to be printed |
| 26 | `EVENT_IND` | DOUBLE |  |  | Identifies whether to chart specific events that are stored in the sub table chart_request_event |
| 27 | `FILE_STORAGE_CD` | DOUBLE | NOT NULL |  | Specifies printer, prn, or rtf |
| 28 | `FILE_STORAGE_LOCATION` | VARCHAR(100) |  |  | Location to write the file out to |
| 29 | `GROUP_ORDER_ID` | DOUBLE | NOT NULL |  | The order id for the parent of the group of orders. The group_order_id will relate to the cs_order_id. The cs_order_id will not always be filled out and can be zero on orders table. |
| 30 | `HANDLE_ID` | DOUBLE | NOT NULL | FK→ | foreign key for the output_ctx table |
| 31 | `MCIS_IND` | DOUBLE |  |  | This field indicates whether a request was an MCIS distribution request (when this field is = 1) or this is a regular expedite request (all other cases). Both times request_type = 2 |
| 32 | `NON_CE_BEGIN_DT_TM` | DATETIME |  |  | This is the date/time used to determine how far back the system should look when searching for clinical insignificant data to include on the chart. |
| 33 | `NON_CE_END_DT_TM` | DATETIME |  |  | This is the date/time that marks the end of the date range for clinical insignificant data to be included on the chart. |
| 34 | `ORDER_GROUP_FLAG` | DOUBLE | NOT NULL |  | The type of Orders grouping. 1 = component2 = supergroup3 = parent/child4 = linked0 = not defined |
| 35 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is the number that is uniquely associated with an order |
| 36 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | This is the code that defines the output destination |
| 37 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | This is the code that identifies the type of device a chart is being printed to |
| 38 | `PAGE_RANGE_IND` | DOUBLE |  |  | This field indicates whether a page range is being used when printing the chart |
| 39 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 40 | `PRINT_COMPLETE_FLAG` | DOUBLE |  |  | This field is not used at this time |
| 41 | `PROCESS_TIME` | DOUBLE |  |  | Number of seconds it took to process this request |
| 42 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Prnsl who is recieving the chart. |
| 43 | `PRSNL_PERSON_R_CD` | DOUBLE | NOT NULL |  | Role of the prsnl recieving the chart |
| 44 | `PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Prsnl_reltn_id of prsnl_reltn table for a provider |
| 45 | `READER_GROUP` | VARCHAR(15) |  |  | This field when defined is used to link one distribution with another |
| 46 | `RECOVER_CNT` | DOUBLE |  |  | Number of times the request went through recovery |
| 47 | `RECOVER_DT_TM` | DATETIME |  |  | Date/Time of last time the request went through recovery |
| 48 | `REQUEST_DT_TM` | DATETIME |  |  | This identifies the date and time when the request was submitted |
| 49 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the id of the person submitting the request |
| 50 | `REQUEST_TYPE` | DOUBLE |  |  | This identifies the type of request that has been submitted (i.e. ad hoc, distribution, expedite) |
| 51 | `RESUBMIT_CNT` | DOUBLE |  |  | This field keeps count of the number of times a request has been resubmitted |
| 52 | `RESUBMIT_DT_TM` | DATETIME |  |  | This is the date and time that the request was last resubmitted |
| 53 | `RESULT_LOOKUP_IND` | DOUBLE |  |  | Result Lookup indicator to look up results by either clinical range or posting range. |
| 54 | `RRD_AREA_CODE` | VARCHAR(10) |  |  | This is the area code for the destination of a remote chart |
| 55 | `RRD_COUNTRY_ACCESS` | VARCHAR(3) |  |  | This is the country access number of a destination for a remote chart |
| 56 | `RRD_DELIVER_DT_TM` | DATETIME |  |  | This is the date and time that a remote chart was sent |
| 57 | `RRD_EXCHANGE` | VARCHAR(10) |  |  | This is the exchange number of a destination for a remote chart |
| 58 | `RRD_PHONE_SUFFIX` | VARCHAR(50) |  |  | This is the phone suffix number of a destination for a remote chart |
| 59 | `SCOPE_FLAG` | DOUBLE |  |  | This is the scope of the chart format (i.e. accession, order, encounter) |
| 60 | `SEQUENCE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Stores the unique identifier to the Chart Sequence Group (route stop) |
| 61 | `SERVER_NAME` | VARCHAR(20) |  |  | The name of the server that last processed the request |
| 62 | `STATUS_FLAG` | DOUBLE |  |  | This is the status of the chart print |
| 63 | `SUPPRESS_MRPNODATA_IND` | DOUBLE | NOT NULL |  | If this indicator is set to 1, then MRP no datas will not print to the printer. |
| 64 | `TOTAL_PAGES` | DOUBLE |  |  | Total pages of chart, replaces outputctx page count |
| 65 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Trigger_id for ESO |
| 66 | `TRIGGER_NAME` | VARCHAR(100) |  |  | Stores the trigger name that fired the chart request. |
| 67 | `TRIGGER_TYPE` | VARCHAR(15) |  |  | Activity type of the event being charted |
| 68 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 69 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 70 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 71 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 72 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 73 | `USER_ROLE_PROFILE` | VARCHAR(255) |  |  | User role profile to be used during the processing of the requested chart |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `CHART_ROUTE_ID` | [CHART_ROUTE](CHART_ROUTE.md) | `CHART_ROUTE_ID` |
| `CHART_TRIGGER_ID` | [CHART_TRIGGER](CHART_TRIGGER.md) | `CHART_TRIGGER_ID` |
| `CR_MASK_ID` | [CR_MASK](CR_MASK.md) | `CR_MASK_ID` |
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `DIST_RUN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_RELTN_ID` | [PRSNL_RELTN](PRSNL_RELTN.md) | `PRSNL_RELTN_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEQUENCE_GROUP_ID` | [CHART_SEQUENCE_GROUP](CHART_SEQUENCE_GROUP.md) | `SEQUENCE_GROUP_ID` |
| `TRIGGER_ID` | [ESO_TRIGGER](ESO_TRIGGER.md) | `TRIGGER_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [CHART_PRINTED_SECTIONS](CHART_PRINTED_SECTIONS.md) | `CHART_REQUEST_ID` |
| [CHART_PRINT_QUEUE](CHART_PRINT_QUEUE.md) | `REQUEST_ID` |
| [CHART_REQUEST_ENCNTR](CHART_REQUEST_ENCNTR.md) | `CHART_REQUEST_ID` |
| [CHART_REQUEST_EVENT](CHART_REQUEST_EVENT.md) | `CHART_REQUEST_ID` |
| [CHART_REQUEST_ORDER](CHART_REQUEST_ORDER.md) | `CHART_REQUEST_ID` |
| [CHART_REQUEST_SECTION](CHART_REQUEST_SECTION.md) | `CHART_REQUEST_ID` |
| [CHART_REQ_INERR_EVENT](CHART_REQ_INERR_EVENT.md) | `CHART_REQUEST_ID` |
| [CHART_SERV_LOG](CHART_SERV_LOG.md) | `CHART_REQUEST_ID` |

