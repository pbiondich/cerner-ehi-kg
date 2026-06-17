# CCL_REPORT_OBJECT

> CCL Report Object

**Description:** CCL Report Object  
**Table type:** REFERENCE  
**Primary key:** `OBJECT_ID`  
**Columns:** 18  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CCL_GROUP` | DOUBLE |  |  | Internal CCL group of object (0=DBA, 1-non-DBA, etc.) |
| 6 | `DRIVER_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | Linkage to an optional driver object also stored on CCL_REPORT_OBJECT. A driver object can be used to populate a record structure for use with a formatted report |
| 7 | `FILE_NAME` | VARCHAR(100) | NOT NULL |  | The source file name for the report object. |
| 8 | `OBJECT_DESCRIPTION` | VARCHAR(2000) |  |  | Description, comments and usage of the report object |
| 9 | `OBJECT_ID` | DOUBLE | NOT NULL | PK | object identifier |
| 10 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Internal Object name used by CCL. This name matches the OBJECT_NAME on the DPROTECT table |
| 11 | `OBJECT_TYPE` | VARCHAR(10) | NOT NULL |  | Text description of object type. Example: REPORT,QUERY,REPORTAPI,LABEL,DRIVER, etc. |
| 12 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | Optional application/product code for documentation purposes |
| 13 | `REPORT_NAME` | VARCHAR(100) | NOT NULL |  | The user-specified report name. This is directly related to Object_name but more descriptive. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRIVER_OBJECT_ID` | [CCL_REPORT_OBJECT](CCL_REPORT_OBJECT.md) | `OBJECT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CCL_LAYOUT_SECTION](CCL_LAYOUT_SECTION.md) | `DRIVER_OBJECT_ID` |
| [CCL_REPORT_OBJECT](CCL_REPORT_OBJECT.md) | `DRIVER_OBJECT_ID` |
| [CCL_REPORT_OBJECT_R](CCL_REPORT_OBJECT_R.md) | `OBJECT_ID` |

