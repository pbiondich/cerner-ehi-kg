# EXPEDITE_MANUAL

> Used to store manual expedite requests to be sent out when result is processed.

**Description:** EXPEDITE MANUAL  
**Table type:** ACTIVITY  
**Primary key:** `EXPEDITE_MANUAL_ID`  
**Columns:** 31  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) | NOT NULL |  | Foreign key to accession on the accession table.Column |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | Begin date for manual expediteColumn |
| 3 | `CHART_CONTENT_FLAG` | DOUBLE |  |  | Used to indicate the amount of results to include on a chart.Column |
| 4 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | chart formatColumn |
| 5 | `COPIES_NBR` | DOUBLE | NOT NULL |  | Stores the number of copies to print for this chart |
| 6 | `DATE_RANGE_IND` | DOUBLE |  |  | If dates were specificedColumn |
| 7 | `DEVICE_NAME` | VARCHAR(50) |  |  | name column from the device table - used for logging and troubleshooting.Column |
| 8 | `DMS_SERVICE_IDENTIFIER` | VARCHAR(110) |  |  | Identifies the DMS Service |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `END_DT_TM` | DATETIME |  |  | End date for manual expediteColumn |
| 11 | `EVENT_IND` | DOUBLE |  |  | Identifies whether to chart specific events that are stored in the sub table chart_request_event |
| 12 | `EXPEDITE_MANUAL_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to orders table.Column |
| 14 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Printer or fax idColumn |
| 15 | `OUTPUT_DEST_NAME` | VARCHAR(20) |  |  | name column from the output_dest table - used for logging and troubleshooting.Column |
| 16 | `OUTPUT_DEVICE_CD` | DOUBLE | NOT NULL |  | The device typeColumn |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to prsnl table.Column |
| 19 | `PROVIDER_ROLE_CD` | DOUBLE | NOT NULL |  | Type of provider such as admitting, attending, ordering, etc.Column |
| 20 | `PRSNL_ROLE_PROFILE_UID` | VARCHAR(150) |  |  | The current RoleProfile UID of the user in context when the request was submitted (only used with SMR) |
| 21 | `RRD_DELIVER_DT_TM` | DATETIME |  |  | Date of faxColumn |
| 22 | `RRD_PHONE_SUFFIX` | VARCHAR(50) |  |  | Fax numberColumn |
| 23 | `SCOPE_FLAG` | DOUBLE |  |  | defines the level of the chartColumn |
| 24 | `SENDING_ORG_ID` | DOUBLE | NOT NULL | FK→ | Indicates the sending organization for the expedite trigger; |
| 25 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The template ID of a report Template used to produce expedite reports. Foreign Key from CR_REPORT_TEMPLATE table. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `USER_ROLE_PROFILE` | VARCHAR(255) |  |  | User role profile to be used during the processing of the requested chart |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SENDING_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXPEDITE_MANUAL_EVENT](EXPEDITE_MANUAL_EVENT.md) | `EXPEDITE_MANUAL_ID` |

