# CR_TEMPLATE_SNAPSHOT

> Stores the report sections and static regions related to a specific template.

**Description:** Template Snapshot  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PAGE_BREAK_AFTER_IND` | DOUBLE | NOT NULL |  | Field indicating if the section is followed by a page break. |
| 5 | `SECTION_ID` | DOUBLE | NOT NULL | FK→ | Section ID column from CR_REPORT_SECTION. FK will be created on this column to its parent column in parent table. |
| 6 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Used when multiple sections are related to a given template. We we need to store the 'sequence' that they are displayed on the template. |
| 7 | `STATIC_REGION_ID` | DOUBLE | NOT NULL | FK→ | Static_Region ID column from CR_REPORT_STATIC_REGION table. FK will be created on this column to its parent column in parent table. |
| 8 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the REPORT_TEMPLATE table. Supports versioning. The row where the ID is equal to the TEMPLATE_SNAPSHOT_ID is the original row. |
| 9 | `TEMPLATE_SNAPSHOT_ID` | DOUBLE | NOT NULL |  | Primary key of the table |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SECTION_ID` | [CR_REPORT_SECTION](CR_REPORT_SECTION.md) | `REPORT_SECTION_ID` |
| `STATIC_REGION_ID` | [CR_REPORT_STATIC_REGION](CR_REPORT_STATIC_REGION.md) | `REPORT_STATIC_REGION_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

