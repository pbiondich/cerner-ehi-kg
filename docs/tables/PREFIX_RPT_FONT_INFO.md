# PREFIX_RPT_FONT_INFO

> This reference table contains the default text and heading attributes associated with a specific report order catalog item. The attributes stored include options such as font, size, color, and font style.

**Description:** Prefix Report Font Information  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the report order catalog item. This value could be used to join to information stored in the order catalog table. |
| 2 | `FONT_ATTRIBUTE_FLAG` | DOUBLE | NOT NULL |  | This field contains a numeric value representing the font style that has been defined for the report text or for the report heading (specified by the value included in the SECTION_TYPE_FLAG field). Font styles include options such as "0, normal", "1, underline", "2, italic", and "4, bold". |
| 3 | `FONT_COLOR` | DOUBLE | NOT NULL |  | This field contains the RGB (Red Green Blue) color value that has been defined for the report text or for the report heading (specified by the value included in the SECTION_TYPE_FLAG field). |
| 4 | `FONT_NAME` | VARCHAR(32) |  |  | This field contains the font that has been defined for the report text or for the report heading (specified by the value included in the SECTION_TYPE_FLAG field). |
| 5 | `FONT_SIZE` | DOUBLE | NOT NULL |  | This field contains the font size that has been defined for the report text or for the report heading (specified by the value included in the SECTION_TYPE_FLAG field). |
| 6 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to identify the accession prefix for which report presentation parameters have been defined. This value could be used to join to prefix information stored on the AP_PREFIX table. |
| 7 | `SECTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field contains a numeric field value identifying the type of report parameters included. The value of "1" indicates that the font and presentation parameters are associated with report text; the value "2" indicates that the parameters are associated with required report component headings; the value "3" indicates that the parameters are associated with optional report component headings. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the report section item. This value could be used to join to information stored in the DISCRETE_TASK_ASSAY table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

