# CHART_FORMAT_CODES

> Used by chart server to find all event_codes and order_catalog codes contained in a Chart Format

**Description:** This table contains all event_codes or order catalog codes for a particular CF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AP_HISTORY_FLAG` | DOUBLE |  |  | Print or don't print history |
| 6 | `CF_CODE_ID` | DOUBLE | NOT NULL |  | This is the id that uniquely defines the chart_format_codes table |
| 7 | `CG_SEQUENCE_NUM` | DOUBLE |  |  | This is number that is assigned to the chart group that defines the order in which it will print within a section |
| 8 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This is the id that uniquely defines the chart format |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This is a unique number assigned to chart groups within a section |
| 10 | `CHART_SECTION_ID` | DOUBLE | NOT NULL | FK→ | This is the number that uniquely identifies a chart section |
| 11 | `CS_SEQUENCE_NUM` | DOUBLE |  |  | This is a sequence number assigned to a chart section which defines the order in which it will print on the chart |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event Code |
| 13 | `EVENT_SET_NAME` | VARCHAR(40) |  |  | This is the event set name for the event sets defined to print within the chart group |
| 14 | `EVENT_SET_SEQ` | DOUBLE |  |  | This is a sequence number to define the order in which the event sets should print within the chart group |
| 15 | `FLEX_TYPE_FLAG` | DOUBLE |  |  | This field identifies which Flex type (Transfusion or XMatch) |
| 16 | `HLA_TYPE_FLAG` | DOUBLE |  |  | This field identifies which HLA type (HLA Typing) |
| 17 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | Catalog Cd |
| 18 | `PROCEDURE_TYPE_FLAG` | DOUBLE |  |  | This flag specifies if the row is an event set or a catalog cd |
| 19 | `SECTION_TYPE_FLAG` | DOUBLE |  |  | This field identifies the type of section (i.e. horizontal, vertical etc.) |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `ZONE` | DOUBLE |  |  | zone value |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |
| `CHART_SECTION_ID` | [CHART_SECTION](CHART_SECTION.md) | `CHART_SECTION_ID` |

