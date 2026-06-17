# EXPEDITE_PARAMS

> The parameters used to produce an expedite once it is triggered. Contains info about the kind of expedite to produce and where to send it.

**Description:** Expedite Parameters  
**Table type:** REFERENCE  
**Primary key:** `EXPEDITE_PARAMS_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_CONTENT_FLAG` | DOUBLE |  |  | Indicates whether the expedite chart should contain all results or just new results since the last expedite. |
| 2 | `CHART_FORMAT_ID` | DOUBLE |  | FK→ | The chart format used to produce the expedite chart. |
| 3 | `COPIES_FLAG` | DOUBLE |  |  | Obsolete - This indicates who should receive additional copies of the expedite chart. |
| 4 | `COPIES_OUTPUT_FLAG` | DOUBLE |  |  | Obsolete - Indicates the method used to determine the output_dest for the additional copies. |
| 5 | `COPY_IND` | DOUBLE |  |  | Used to keep track of the provider types that should receive a copy of chart. |
| 6 | `EXPEDITE_PARAMS_ID` | DOUBLE | NOT NULL | PK | Primary key to uniquely identify row. Internal system generated identifier. |
| 7 | `EXP_PROV_IND` | DOUBLE | NOT NULL |  | 0 = Both expired and non-expired provider relations. 1 = Non-expired provider relations only. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `NAME` | VARCHAR(100) | NOT NULL |  | Description of the expedite parameters. |
| 10 | `NAME_KEY` | VARCHAR(100) | NOT NULL |  | Indexed and converted version of name column for searching. |
| 11 | `ORDER_DOC_FLAG` | DOUBLE | NOT NULL |  | This indicates which ordering provider should receive copies of the expedite chart. 0 = original ordering provider; 1 = current ordering provider; 2 = original and current ordering provider; 3 = all ordering providers |
| 12 | `OUTPUT_DEST_CD` | DOUBLE |  | FK→ | Indicates the destination (i.e. printer) at which to produce the expedite chart. |
| 13 | `OUTPUT_DEVICE_CD` | DOUBLE |  |  | This column is only used if the outputdestination is an rrd device. It indicates the type of device (i.e. printer or fax). |
| 14 | `OUTPUT_FLAG` | DOUBLE |  |  | Specifies the method to use to find the output_dest for the chart. |
| 15 | `PATHOLOGIST_DEFAULT_IND` | DOUBLE | NOT NULL |  | This indicates if the expedite chart is sent to responsible pathologist by default: 1 = the default chart is sent to responsible pathologist (only used for AP reports); 0 = the default chart is sent to admitting provider. |
| 16 | `SENDING_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifies the sending organization for the trigger |
| 17 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The template ID of a report Template used to produce expedite reports. Foreign Key from CR_REPORT_TEMPLATE table. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `SENDING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EXPEDITE_COPY](EXPEDITE_COPY.md) | `EXPEDITE_PARAMS_ID` |
| [EXPEDITE_PARAMS_R](EXPEDITE_PARAMS_R.md) | `EXPEDITE_PARAMS_ID` |

