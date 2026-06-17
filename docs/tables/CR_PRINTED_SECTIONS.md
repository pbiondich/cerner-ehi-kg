# CR_PRINTED_SECTIONS

> Stores the sections of a report that actually printed from a specific report request.

**Description:** Clinical Report Printed Sections  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | The content type of this section such as allergy, immunization, etc. |
| 2 | `PRINTED_SECTION_ID` | DOUBLE | NOT NULL |  | A number that uniquely identifies a row in this table |
| 3 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the related report request |
| 4 | `SECTION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the report section that was printed |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |
| `SECTION_ID` | [CR_REPORT_SECTION](CR_REPORT_SECTION.md) | `REPORT_SECTION_ID` |

