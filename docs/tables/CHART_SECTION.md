# CHART_SECTION

> chart section

**Description:** This table defines the chart section  
**Table type:** REFERENCE  
**Primary key:** `CHART_SECTION_ID`  
**Columns:** 14  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHART_SECTION_DESC` | VARCHAR(64) |  |  | This is a free text description given to the chart section |
| 6 | `CHART_SECTION_ID` | DOUBLE | NOT NULL | PK | This is the number that uniquely identifies a chart section |
| 7 | `SECTION_TYPE_FLAG` | DOUBLE |  |  | This field identifies the type of section (i.e. horizontal, vertical etc.) |
| 8 | `SECT_PAGE_BRK_IND` | DOUBLE | NOT NULL |  | Specifies whether a page break should be appended to the section during processing |
| 9 | `UNIQUE_IDENT` | VARCHAR(60) |  |  | Text form of Unique Identifier |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [CHART_FORMAT_CODES](CHART_FORMAT_CODES.md) | `CHART_SECTION_ID` |
| [CHART_FORM_SECTS](CHART_FORM_SECTS.md) | `CHART_SECTION_ID` |
| [CHART_GROUP](CHART_GROUP.md) | `CHART_SECTION_ID` |
| [CHART_PRINTED_SECTIONS](CHART_PRINTED_SECTIONS.md) | `CHART_SECTION_ID` |
| [CHART_REQUEST_SECTION](CHART_REQUEST_SECTION.md) | `CHART_SECTION_ID` |
| [CHART_SECT_FLDS](CHART_SECT_FLDS.md) | `CHART_SECTION_ID` |

