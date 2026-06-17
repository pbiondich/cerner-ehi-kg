# AP_DIGITAL_SLIDE

> This table contains information about the cases or slides for which digital images are available in a foreign imaging system.

**Description:** AP Digital Slide Table  
**Table type:** ACTIVITY  
**Primary key:** `AP_DIGITAL_SLIDE_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `AP_DIGITAL_SLIDE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the AP_DIGITAL_SLIDE table. |
| 4 | `CASE_ID` | DOUBLE |  | FK→ | This field uniquely identifies a row included on the PATHOLOGY_CASE table. This field is used to represent a pathology case |
| 5 | `SLIDE_ID` | DOUBLE |  | FK→ | This field uniquely identifies a row (a slide) included in the SLIDE table. |
| 6 | `SOURCE_CD` | DOUBLE |  |  | The field contains reference to code_value table. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `SLIDE_ID` | [SLIDE](SLIDE.md) | `SLIDE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AP_DIGITAL_SLIDE_INFO](AP_DIGITAL_SLIDE_INFO.md) | `AP_DIGITAL_SLIDE_ID` |

