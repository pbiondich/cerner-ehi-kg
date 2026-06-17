# CHART_TRIGGER

> The chart_trigger table is used to store the general information about a given trigger

**Description:** Chart Trigger  
**Table type:** REFERENCE  
**Primary key:** `CHART_TRIGGER_ID`  
**Columns:** 31  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDITIONAL_COPY_NBR` | DOUBLE | NOT NULL |  | number of additional copies |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The chart format unique identifier |
| 5 | `CHART_TRIGGER_ID` | DOUBLE | NOT NULL | PK | Primary key for a given trigger |
| 6 | `COMPLETE_FLAG` | DOUBLE | NOT NULL |  | The complete flag denotes whether to trigger on complete accessions, complete orders, etc. |
| 7 | `DATE_DT_TM` | DATETIME |  |  | Stores the start date of printed chart to be requested. |
| 8 | `DAYS_NBR` | DOUBLE | NOT NULL |  | The number of days used for a request window. |
| 9 | `DEFAULT_OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | The default output destination |
| 10 | `DISCHARGE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Discharge type flat denote whether to qualify discharged, non-discharged or both type of patients |
| 11 | `DMS_SERVICE_NAME` | VARCHAR(64) |  |  | The dms service name |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EXPIRED_RELTN_IND` | DOUBLE | NOT NULL |  | The expired relationship indicator notes to include or exclude expired relationships when determining the recipients of the charts. |
| 14 | `FILE_STORAGE_CD` | DOUBLE | NOT NULL |  | The file storage code notes the type of files to be produced |
| 15 | `FILE_STORAGE_LOCATION` | VARCHAR(225) |  |  | The location in which to place electronic copies of a given request |
| 16 | `NAME_IDENT` | VARCHAR(167) | NOT NULL |  | Unique Identifier used for merge processes. A concatenation of the name key and date column. MUI. |
| 17 | `PENDING_FLAG` | DOUBLE | NOT NULL |  | Selection in which to print verified events only, verified and pending, etc. |
| 18 | `PREV_CHART_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Trigger Identifier. Required for RDDS type-2 versioning. |
| 19 | `PRINT_RANGE_FLAG` | DOUBLE | NOT NULL |  | The print range flag denotes whether to produce a chart for the specific result, cumulative, etc. |
| 20 | `REPORT_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The report template unique identifier from CR_REPORT_TEMPLATE |
| 21 | `ROUTE_LOCATION_BIT_MAP` | DOUBLE | NOT NULL |  | The route location bitmap denotes the locations in which a chart should be produced (assigned device, patient location order location, etc.) |
| 22 | `SCOPE_FLAG` | DOUBLE | NOT NULL |  | The scope of the request to be made |
| 23 | `SENDING_ORG_ID` | DOUBLE | NOT NULL | FK→ | Indicates the sending organization for the trigger |
| 24 | `TRIGGER_NAME` | VARCHAR(150) | NOT NULL |  | The name of the trigger |
| 25 | `TRIGGER_NAME_KEY` | VARCHAR(150) | NOT NULL |  | The name key of the trigger |
| 26 | `TRIGGER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Trigger type flag defines if a given trigger is to trigger now or trigger later |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `PREV_CHART_TRIGGER_ID` | [CHART_TRIGGER](CHART_TRIGGER.md) | `CHART_TRIGGER_ID` |
| `REPORT_TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |
| `SENDING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CHART_REQUEST](CHART_REQUEST.md) | `CHART_TRIGGER_ID` |
| [CHART_TRIGGER](CHART_TRIGGER.md) | `PREV_CHART_TRIGGER_ID` |
| [CHART_TRIGGER_PARAM](CHART_TRIGGER_PARAM.md) | `CHART_TRIGGER_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `CHART_TRIGGER_ID` |

