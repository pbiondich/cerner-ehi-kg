# STATION

> The station table defines the logical location of a destination. If multiple doctors are using one device, then they would each have a station pointing to the single device.

**Description:** Station  
**Table type:** REFERENCE  
**Primary key:** `OUTPUT_DEST_CD`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_CRITERIA` | DOUBLE |  |  | The number of minutes the report will stay on the delivery queue, with it's current priority before it is aged. |
| 2 | `AGING_PRIORITY_CHANGE` | DOUBLE |  |  | Value to be decremented from the scheduled_value or non_scheduled_value when Aging the priority |
| 3 | `BUNDLE_PAGE_LIMIT` | DOUBLE |  |  | The number of additional pages of a lower priority can be sent with the current transmission. If the value for page numbers is blank, then no bundling will occur. |
| 4 | `DELIVERY_CLASS_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Unique number identifying the Delivery Class QueueColumn |
| 5 | `DESCRIPTION` | CHAR(20) |  |  | Name of the Delivery Class QueueColumn |
| 6 | `DESCRIPTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from LONG_TEXT_REFERENCE table. |
| 7 | `DISABLED_IND` | DOUBLE |  |  | Status of station, either active or disabled. |
| 8 | `EOT_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from WP_TEMPLATE table |
| 9 | `NON_SCHEDULED_VALUE` | DOUBLE |  |  | Priority assigned for a manual requested transmission. |
| 10 | `NUMBER_OF_COPIES` | DOUBLE |  |  | Number of copies |
| 11 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | PK FK→ | This is really a Foreign key into the output_dest table. |
| 12 | `REPORT_LIST` | DOUBLE |  |  | Indication if a report listing should be printed, if so where it should print. |
| 13 | `REPORT_LIST_SIZE_CUTOFF` | DOUBLE |  |  | Number of reports that need to be in a session before a listing of the reports will be generated. |
| 14 | `SCHEDULED_VALUE` | DOUBLE |  |  | Priority assigned for a schedule transmission for the station. |
| 15 | `SEND_EOT_PAGE_IND` | DOUBLE |  |  | Indicates whether to send an "End Of Page" page. |
| 16 | `SEND_FLAG` | DOUBLE | NOT NULL |  | This flag will determine whether to send reports to RRD, Healthe or both. 0 = Send to RRD Fax 1 = Send to Healthe Exchange account 2 = Send to both RRD Fax and Healthe Exchange account |
| 17 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The numeric value for the cover page template that will be used for the specific station. Each station could have it's own Cover Page. |
| 18 | `TIME_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | number identifying what time scheme is attached to this station. Foreign Key into time_scheme_window |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DELIVERY_CLASS_QUEUE_ID` | [DELIVERY_CLASS_QUEUE](DELIVERY_CLASS_QUEUE.md) | `DELIVERY_CLASS_QUEUE_ID` |
| `DESCRIPTION_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `EOT_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `TIME_SCHEME_ID` | [TIME_SCHEME_WINDOW](TIME_SCHEME_WINDOW.md) | `TIME_SCHEME_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RRDBRIDGE](RRDBRIDGE.md) | `STATION_DEST_CD` |
| [VENDOR](VENDOR.md) | `OUTPUT_DEST_ID` |

