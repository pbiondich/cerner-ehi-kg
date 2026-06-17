# CHART_IMAGE_MM_FLDS

> This table is used to store the mail merge fields to be used by all image pages for a single chart format.

**Description:** Chart format image mail merge fields  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CDF_MEANING` | VARCHAR(12) | NOT NULL |  | This is the CDF Meaning from code set 14005 for the data elements defined to print in thne chart header/footer. |
| 6 | `CHART_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | This is the FK value from table CHART_FORMAT and is a number assigned to each unique chart format. It is used here, in conjunction with a Field Sequence, to uniquely identify rows in this table. |
| 7 | `FIELD_SEQ` | DOUBLE | NOT NULL |  | The field sequence. Used with the CHART_FORMAT_ID to uniquely identify rows in this table. |
| 8 | `LOCATION_IND` | DOUBLE | NOT NULL |  | Indicates if header or footer. Header = 0 and footer = 1 |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_FORMAT_ID` | [CHART_FORMAT](CHART_FORMAT.md) | `CHART_FORMAT_ID` |

