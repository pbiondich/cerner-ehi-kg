# WP_TEMPLATE_TEXT

> This reference table contains the text associated with an individual template. The associated template parameters are stored on the WP_TEMPLATE table.

**Description:** Word Processing Template Text  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the Rich Text Format (RTF) template text stored on the LONG_TEXT table. |
| 2 | `PCS_RSLT_FRMT_VRSN_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a result format version within the template at the text position |
| 3 | `PCS_RSLT_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a result layout placed within the template at the text position |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a sequence value which is used when the associated template has more than one template text record included on the LONG_TEXT reference table. |
| 5 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value (identifying the template) that is used to join to template information stored on the WP_TEMPLATE reference table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PCS_RSLT_FRMT_VRSN_ID` | [PCS_RSLT_FRMT_VRSN](PCS_RSLT_FRMT_VRSN.md) | `PCS_RSLT_FRMT_VRSN_ID` |
| `PCS_RSLT_LAYOUT_ID` | [PCS_RSLT_LAYOUT](PCS_RSLT_LAYOUT.md) | `PCS_RSLT_LAYOUT_ID` |
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

